from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from userapp.forms import userForm,userForm1,UpdateForm,UpdateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form1 = userForm(request.POST)
        form2 = userForm1(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            profile = form2.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            # print("Validation Success")
            # print(form1.cleaned_data['username'])
            # print(form1.cleaned_data['password'])
            # print(form2.cleaned_data['address'])
    else:
        form1 = userForm()
        form2 = userForm1()

    context = {
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,'registration.html',context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # masked_password = password[0] + '*' * (len(password)-2) + password[-1]
        user = authenticate(username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse("<h1>User is Not Active</h1>")
        else:
            return HttpResponse("<h1>Please check your creds...!</h1>")
        
    return render(request,'login.html',{})

@login_required(login_url='login')
def home(request):
    return render(request,'home.html',{})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html',{})

@login_required(login_url='login')
def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST,instance=request.user)
        form1 = UpdateUserForm(request.POST,instance=request.user.usermodel) # request.FILES for image field
        if form.is_valid() and form1.is_valid():
            user = form.save() 
            
            profile = form1.save() # commit = 'FALSE' for image field
            profile.user = user
            profile.save()
            return redirect('dashboard')
    else:
       form = UpdateForm(instance=request.user)
       form1 = UpdateUserForm(instance=request.user.usermodel)

    return render(request,'update.html',{'form':form,'form1':form1})
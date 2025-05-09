from django.shortcuts import render,redirect
from taskmanager.models import TASK,TaskImage
from taskmanager.forms import TaskForm,EditTaskForm
from django.core.paginator import Paginator

# Create your views here.
def alltasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alltasks')
    else:
        data = TASK.objects.all()
        page_no = Paginator(data,5)
        page = request.GET.get('pg')
        data = page_no.get_page(page)
        form = TaskForm()
    context = {
        'data': data,
        'form': form
    }
    
    return render(request,'tasks/alltasks.html',context)

def edittask(request,id=0):
    data = TASK.objects.get(id=id)
    if request.method == "POST":
        form = EditTaskForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('alltasks')
    else:
        form = EditTaskForm(instance=data)
    return render(request,'tasks/edit_task.html',{'form':form})

def deletetask(request,id=0):
    data = TASK.objects.get(id=id)
    data.delete()
    return redirect('alltasks')

def description(request,id=0):
    item = TASK.objects.get(id=id)
    images = TaskImage.objects.filter(var=item)
    return render(request,'tasks/description.html',{'item':item,'images':images})
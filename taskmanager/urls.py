from django.urls import path
from taskmanager import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.alltasks,name='alltasks'),
    path('edit/<int:id>',views.edittask,name='edit'),
    path('delete/<int:id>',views.deletetask,name='delete'),
    path('description/<int:id>',views.description,name='description'),
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

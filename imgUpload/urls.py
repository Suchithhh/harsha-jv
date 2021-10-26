from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url('', views.imageProcess, name='imageUpload'),
    url('imageprocess/',views.imageProcess,name='imageprocess')
    
]
 
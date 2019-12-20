from django.urls import path
from .import views

app_name='task'
urlpatterns=[
path('',views.index,name='index'),
path('create',views.create,name='create'),
path('<int:task_id>/delete',views.delete,name='delete'),
]
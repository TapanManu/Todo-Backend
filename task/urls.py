from django.urls import path
from .import views
from django.contrib import auth

app_name='task'
urlpatterns=[
path('create/<username>',views.create,name='create'),
path('<int:task_id>/delete/<username>',views.delete,name='delete'),
]

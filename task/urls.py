from django.urls import path
from .import views

app_name='task'
urlpatterns=[
path('<username>/',views.index,name='index'),
path('create/<username>',views.create,name='create'),
path('<int:task_id>/delete/<username>',views.delete,name='delete'),
path('base',views.base,name='base'),
]

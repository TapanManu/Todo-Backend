from django.urls import path
from . import views

app_name='user'
urlpatterns=[
	path('register',views.register,name='register'),
	path('home',views.register,name='home'),
	path('logi',views.logi,name='logi'),
	path('logo',views.logo,name='logo'),
]	
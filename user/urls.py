from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='user'
urlpatterns=[
	path('register',views.register,name='register'),
	path('home',views.register,name='home'),
	path('logi',views.logi,name='logi'),
	path('logo',views.logo,name='logo'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
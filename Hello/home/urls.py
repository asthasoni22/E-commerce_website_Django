from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('login',views.login , name = 'Login'),
    path('logout',views.logout , name = 'Logout'),
    path('contact',views.contact , name = 'Contactus'),
    path('bottoms',views.bottoms , name = 'Bottoms'),
    path('tops',views.tops , name = 'Tops'),
    path('jwellery',views.jwellery , name = 'Jwellery'),
    path('traditionals',views.traditionals , name = 'Traditionals'),
    path('additional',views.additional,name="additional"),
    path('forgot',views.forgot,name = 'Forgot'),
    path('register',views.register,name = 'Register')   
]

from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('signup', views.signup, name='signup'),
    path('base', views.base, name='base'),

]
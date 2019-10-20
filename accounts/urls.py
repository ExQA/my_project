from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('calculator', views.calculator),
    path('weatherapp', views.index),
    path('myip', views.myip)

]

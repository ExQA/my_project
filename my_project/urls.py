from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('weatherapp/', views.index, name='weather'),
    path('myip/', views.myip, name='myip')

]

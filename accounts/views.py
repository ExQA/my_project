from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City
from .forms import CityForm
import requests

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

from .calc_oper import calc_object


@login_required(login_url='/accounts/login/')
def calculator(request):
    ctx = {}
    ctx['operations'] = calc_object.keys()
    if request.method == 'GET':
        print('GET!')
    elif request.method == 'POST':
        try:
            first_num = float(request.POST.get('first_num'))
            operation = request.POST.get('operation')
            second_num = float(request.POST.get('second_num'))
            result = calc_object[operation](first_num, second_num)
            ctx['result'] = result
        except (ValueError, ZeroDivisionError) as e:
            ctx['msg'] = e
    return render(request, 'calculator.html', ctx)


def index(request):
    appid = '2a04a7f416f8792391a8b74c3a2a3d88'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = None
        try:
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
        except KeyError as e:
            print(e)

        if city_info:
            all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}
    return render(request, 'weather.html', context)




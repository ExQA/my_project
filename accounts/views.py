from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse


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




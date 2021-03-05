from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def registratsiya(request):
    if request.POST:
        agro_user = AgroUser()
        agro_user.user_type = request.POST.get("user_type")
        agro_user.full_name = request.POST.get("full_name")
        agro_user.email = request.POST.get("email")
        agro_user.password = request.POST.get("password")
        agro_user.number = request.POST.get("number")
        agro_user.save()
    return render(request, 'registratsiya.html')


def form(request):
    return render(request, 'form.html')


def razdel(request):
    return render(request, 'razdel.html')
from django.urls import pathfrom . import viewsurlpatterns = [    path('index/',views.index,name='index'),    path('registratsiya/',views.registratsiya,name='registratsiya'),    path('form/',views.form,name='form'),    path('razdel/',views.razdel,name='razdel'),]
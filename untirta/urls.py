"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from data.views import data
from faperta.views import *
from feb.views import feb
from fh.views import fh
from fisip.views import fisip
from fk.views import fk
from fkip.views import fkip
from ft.views import ft
from pascasarjana.views import pascasarjana
from profil.views import profil
from faperta.models import dosen
from faperta.models import mahasiswa
from faperta.models import staff
from.import views

class dosenadmin(admin.ModelAdmin):
    pass

admin.site.register(dosen, dosenadmin)

class mahasiswaadmin(admin.ModelAdmin):
    pass

admin.site.register(mahasiswa, mahasiswaadmin)

class staffadmin(admin.ModelAdmin):
    pass

admin.site.register(staff, staffadmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data),
    path('faperta/', faperta),
    path('dosen/', dosenfaperta),
    path('mahasiswa/', mahasiswafaperta),
    path('staff/', stafffaperta),
    path('tambah-dosen/', tambah_dosen),
    path('tambah-mahasiswa/', tambah_mahasiswa),
    path('tambah-staff/', tambah_staff),
    path('dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('feb/', feb),
    path('fh/', fh),
    path('fisip/', fisip),
    path('fk/', fk),
    path('fkip/', fkip),
    path('ft/', ft),
    path('pascasarjana/', pascasarjana),
    path('profil/', profil),
    path('home/', views.untirta)
]

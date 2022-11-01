from multiprocessing import context
from django.shortcuts import render, redirect
from faperta.models import dosen
from faperta.models import mahasiswa
from faperta.models import staff
from faperta.forms import FormDosen
from faperta.forms import FormMahasiswa
from faperta.forms import FormStaff

# Create your views here.
def faperta(request):
    return render(request, 'indexfaperta.html')

def dosenfaperta(request):
    dosens = dosen.objects.all()

    konteks = {
        'dosens': dosens,
    }
    return render(request, 'dosen.html', konteks)

def mahasiswafaperta(request):
    mahasiswas = mahasiswa.objects.all()

    konteks = {
        'mahasiswas': mahasiswas,
    }
    return render(request, 'mahasiswa.html', konteks)

def stafffaperta(request):
    staffs = staff.objects.all()

    konteks = {
        'staffs': staffs,
    }
    return render(request, 'staff.html', konteks)
   
def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
    
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        
        form = FormMahasiswa()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-mahasiswa.html', konteks)

def tambah_staff(request):
    if request.POST:
        form = FormStaff(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaff()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staff.html', konteks)
    else:
        
        form = FormStaff()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-staff.html', konteks)

def ubah_dosen(request, id_dosen):
    dosen = dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)
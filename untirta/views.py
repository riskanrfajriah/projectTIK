from multiprocessing import context
from django.shortcuts import render

def untirta(request):
    context = {
        'title':'untirta',
        'heading':'Selamat Datang',
        'subheading':'di website Universitas Sultan Ageng Tirtayasa',  
    }
    return render(request, 'index.html', context)
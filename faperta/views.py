from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def faperta(request):
    return render(request, 'indexfaperta.html')
   

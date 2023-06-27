from django.shortcuts import render
from app.views import *
# Create your views here.
def bhavi(request):
    return render(request,'bhavi.html')

def janu(request):
    return render(request,'janu.html')

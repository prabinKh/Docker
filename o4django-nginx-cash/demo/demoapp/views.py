from django.shortcuts import render

# Create your views here.
from .models import *

def portfolio(request):
    
    return render(request, 'p1.html')


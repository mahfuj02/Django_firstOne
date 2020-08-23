from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    diction = {}
    return render(request,'myapp/index.html', context = diction)

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showout(request):
    return HttpResponse('Models project')
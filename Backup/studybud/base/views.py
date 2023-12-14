from django.shortcuts import render

# Create your views here.
def status(request):
    return render(request, 'base/status.html')

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def signup(request):
    context = {}
    return render(request, 'base/signup.html', context)

def signin(request):
    context = {}
    return render(request, 'base/signin.html', context)
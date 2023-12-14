from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupField
from django.contrib import messages
from .models import SignupModel

# Create your views here.
def status(request):
    return render(request, 'status.html')

def signup(request):
    global context
    context = {}
    context['forms'] = SignupField()
    formText = SignupField(request.POST)
    if request.method == "POST":
        if formText.is_valid():
            signupdata = (formText.cleaned_data['username'], formText.cleaned_data['email'], formText.cleaned_data['password'])
            context['username'] = signupdata[0]
            context['email'] = signupdata[1]
            context['password'] = signupdata[2]
            formText.save()
            messages.success(request, "signup successful")
            return redirect('signin')

    return render(request, 'signup.html', context)

def signin(request, *context):
    details = {}
    # details['SignupInput'] = SignupField()
    datas = SignupModel.objects.all().values()
    print(datas)
    details['datas'] = datas
    # print(context)
    # details = {}
    # details['context'] = context
    # # print(details['username'])

    return render(request, 'signin.html', details)

# def signin(request):
#     context ={}
#     inputField = SignupField() 
#     context['inputField'] = inputField
#     formfield = SignupField(request.POST)

#     if request.method == "POST":
#         if formfield.is_valid():
#             signupdata = (formText.cleaned_data['username'], formText.cleaned_data['password'])
#             context['username'] = signupdata[0]
#             context['password'] = signupdata[1]
#             messages.success(request, "login successful")
#             return redirect('home')

#     return render(request, 'signin.html', context)

def home(request):
    context ={}
    context['details'] = SigninField()
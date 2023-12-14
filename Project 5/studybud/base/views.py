from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, SigninForm
from .models import SignupModel
from django.contrib import messages

# Create your views here.
def signup(request):
    context = {}
    context['forms'] = SignupForm()
    inputForm = SignupForm(request.POST)
    if request.method == 'POST':
        if inputForm.is_valid():
            inputForm.save()
            return redirect('signin')
        
        details = (inputForm.cleaned_data['username'], inputForm.cleaned_data['firstname'], inputForm.cleaned_data['lastname'],inputForm.cleaned_data['email'], inputForm.cleaned_data['password'],  inputForm.cleaned_data['c_password'])
        context['user'] = details[1]
        context['lname'] = details[2]
        context['email'] = details[3]
        context['pass1'] = details[4]
        context['pass2'] = details[5]
        if pass1 == pass2:
            inputForm.save()
            messages.success(request, "signup successful")
        else:
            messages.info(request, "passwords doesn't match, \n please check and try again")
            
    return render(request, 'signup.html', context)

def signin(request):
    context = {}
    form = SigninForm()
    formText = SigninForm(request.POST)
    context['formText'] = formText
    if request.method == 'POST':
        query = SignupModel.objects.all().values()
        if formText.is_valid():
            details = (formText.cleaned_data['username'], formText.cleaned_data['password'])
            context['query']  = SignupModel.objects.all().values()
            context['user1'] = details[0]
            context['pass1'] = details[1]
            user1 = details[0]
            pass1 = details[1]
            mysql = SignupModel.objects.filter(username = user1).values()
            sql_stmt = SignupModel.objects.filter(username = user1, password = pass1).values()
            i = len(sql_stmt)-1
            if i < len(sql_stmt):
                for object in sql_stmt:
                    if object['password'] == pass1:
                        messages.success(request, "Login successful")
                        return redirect('home')
                        messages.success(request, "Login successful")
                        i +=1
                    else:
                        messages.error(request, "Login unsuccessful \n Please check if username and password is correct")
    return render(request, 'signin.html', context)

def home(request):
    return render(request, 'home.html')

# def create(request):
#     return render(request, 'createaccount.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignupForm, Signup, SigninForm
from .models import SignupModel

# Create your views here.
def status(request):
    context = {}
    
    return render(request, 'base/status.html', context)

def signin(request):
    context = {}
    context['formfield'] = SigninForm()
    forms = SigninForm(request.POST)
    if request.method == "POST":
        # if forms.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)

        except:
            messages(request, "No such user exists")
        
        print(user, password, username)

        if user is not None:
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            messages(request, "Username does not exist or password is not correct")

    return render(request, "base/signin.html", context)

def signup(request):
    context = {}
    context['formfield'] = Signup()
    form = Signup(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email').lower()
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            sql_stmt = User.objects.filter(username=username).first()
            sql_stmt2 = User.objects.filter(email=email).first()
            if sql_stmt is None and sql_stmt2 is None:
                form.save(commit=False)
                if password == confirm_password:
                    form.save()
                    return redirect('signin')
                else:
                    messages.error(request, "password doesn't match with confirm password")
            else:
                messages.error(request, "Username or email already exists")
    return render(request, 'base/signup.html', context)


# def signup(request):
#     context = {}
#     context['formfield'] = SignupForm()
#     form = SignupForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             username = request.POST.get('username')
#             email = request.POST.get('email').lower()
#             password = request.POST.get('password')
#             confirm_password = request.POST.get('confirm_password')
#             sql_stmt = SignupModel.objects.filter(username=username).first()
#             sql_stmt2 = SignupModel.objects.filter(email=email).first()
#             if sql_stmt is None and sql_stmt2 is None:
#                 form.save(commit=False)
#                 if password == confirm_password:
#                     form.save()
#                     return redirect('signin')
#                 else:
#                     messages.error(request, "password doesn't match with confirm password")
#             else:
#                 messages.error(request, "Username or email already exists")
#     return render(request, "base/signup.html", context)

# Substitute for signup
# def signup(request):
#     context = {}
#     context['formfield'] = UserCreationForm()
#     form = UserCreationForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             user = form.save(commit=False)
#             form.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             print(form.errors.items())
#             print('ERROR SEEN')
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"{field}: {error}")
#             return redirect('signup')
#     return render(request, "base/signup.html", context)


def home(request):
    context = {}
    return render(request, "base/home.html", context)
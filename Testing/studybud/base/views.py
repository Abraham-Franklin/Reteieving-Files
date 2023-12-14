from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import SignupForm, SigninForm, PostForm
from .models import AddPost
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def status(request):
    return render(request, 'base/status.html')

def signup(request):
    context = {}
    context['create_user'] = SignupForm()
    create_user = User(request.POST)
    if request.method == 'POST':
        password = request.POST.get('password'),
        confirm_password = request.POST.get('confirm_password'),
        if password == confirm_password:
            user = User.objects.create(
                username = request.POST.get('username'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                password = make_password(request.POST.get('password'))
            )
            messages.success(request, 'You have successfully created an account')
            return redirect('signin')
        else:
            messages.error(request, 'passwords dont match. Please check and try again')
    else:
        create_user = User(request.POST)
    return render(request, 'base/signup.html', context)

def signin(request):
    context = {}
    context['user_form'] = SigninForm()
    user_form = SigninForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            print('authenticated')
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully logged in')
            return redirect('home')
        else:
            print('unsucccessful')
            messages.error(request, 'There was an issue loggin you in')

    return render(request, 'base/signin.html', context)

def signup_admin(request):
    context = {}
    context['admin_user'] = SignupForm()
    admin_user = User(request.POST)
    if request.method == 'POST':
        password = request.POST.get('password'),
        confirm_password = request.POST.get('confirm_password'),
        if password == confirm_password:
            admin_user = User.objects.create(
                username = request.POST.get('username'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                password = make_password(request.POST.get('password')),
                is_staff = True,    # Give staff permissions
                is_superuser = True # Give superuser permissions
            )
            messages.success(request, 'You have successfully created a super account')
            return redirect('signin-admin')
        else:
            messages.error(request, 'passwords dont match. Please check and try again')
    else:
        admin_user = User(request.POST)
    return render(request, 'base/signup-admin.html', context)

def signin_admin(request):
    context = {}
    context['admin_user'] = SigninForm()
    admin_user = SigninForm(request.POST)
    if request.method == 'POST':
        if admin_user.is_valid():
            print('authenticated')
            username = admin_user.cleaned_data['username']
            password = admin_user.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully logged in')
            # return redirect('admin/auth/user')
            return redirect(reverse('admin:auth_user_changelist'))
        else:
            print('unsucccessful')
            messages.error(request, 'There was an issue loggin you in')

    return render(request, 'base/signin-admin.html', context)

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def addpost(request):
    context = {}
    context['post_form'] = PostForm()
    post_form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        new_post = post_form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        messages.success(request, "Post saved successfully")
        redirect('base/home')
    return render(request, 'base/addpost.html', context)


#  	UNIQUE constraint failed: auth_user.username
#  This password is too common.
# This password is entirely numeric.
# Error: Your passwords didn't match.
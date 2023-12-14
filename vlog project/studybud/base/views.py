from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SignupModel, Posts
from .forms import SignupForm, PostForm
from .forms import SigninForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def status(request):
    
    return render(request, "base/status.html")


def signup(request):
    context = {}
    context["Field"] = SignupForm()
    formField = SignupForm(request.POST)
    if request.method == 'POST':
        if formField.is_valid():
            inputContent = (formField.cleaned_data['username'], formField.cleaned_data['first_name'], formField.cleaned_data['last_name'], formField.cleaned_data['email'])
            context['username'] = inputContent[0]
            context['fname'] = inputContent[1]
            context['lname'] = inputContent[2]
            context['email'] = inputContent[3]
            # context['password'] = inputContent[4]
            formField.save()
            messages.success(request, "Account sucessfully created")
            return redirect('home')
        return render(request, "base/signup.html", context)


    return render(request, "base/signup.html", context)

def signin(request):
    context = {}
    context['signinForm'] = SigninForm()
    formfield = SigninForm(request.POST)
    modelfield = SignupModel(request.POST)
    if formfield.is_valid():
        if request.method == 'POST':
            username = formfield.cleaned_data['username']
            context['username'] = username
            firstname = formfield.cleaned_data['first_name']
            context['firstname'] =firstname

            mydata = SignupModel.objects.filter(username=username).values()
            for data in mydata:
                print(data['first_name'])
            # if mydata.count() > 0:
            if data['first_name'] == firstname:
                messages.success(request, "login success")
                # delete = SignupModel.objects.all()
                # delete.delete() 
                return redirect('home') 

    return render(request, 'base/signin.html', context)

def home(request):
    formField = SignupForm(request.POST)
    context = {}
    context['mydata'] = SignupModel.objects.all().values()
    return render(request, 'base/home.html', context) 


def posts(request):
    context = {}
    postmodel = Posts(request.POST)
    context['postform'] = PostForm()
    context['postmodel'] = Posts()
    if request.method == 'POST':
        mydata = Posts.objects.all().values()
        for datas in mydata:
            context['datas'] = datas
            postmodel.save()
    return render(request, 'base/posts.html', context)


def viewposts(request):
    context={}
    mydata = Posts.objects.all().values()
    # for datas in mydata:
    context['mydata'] = mydata 
    print(mydata)
    return render(request, 'base/viewposts.html', context)
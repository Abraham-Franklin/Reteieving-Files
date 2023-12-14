from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Posts
from .forms import SignupForm, PostForm
from .forms import SigninForm
# from .models import Posts
# from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Create your views here.
def status(request):
    
    return render(request, "base/status.html")


def signup(request):
    context = {}
    context["Field"] = SignupForm()
    formField = SignupForm(request.POST)
    if request.method == 'POST':
        if formField.is_valid():
            formField.save()
            messages.success(request, "Account sucessfully created")
            return redirect('home')
        return render(request, "base/signup.html", context)


    return render(request, "base/signup.html", context)

def signin(request):
    context = {}
    context['signinForm'] = SigninForm()
    formfield = SigninForm(request.POST)
    modelfield = User(request.POST)
    if formfield.is_valid():
        if request.method == 'POST':
            username = formfield.cleaned_data['username']
            context['username'] = username
            password = formfield.cleaned_data['password']
            def hash_password(password):
                salt = 'random_string'  # This should be a unique string for each user
                hash_obj = hashlib.sha256()
                hash_obj.update((password + salt).encode('utf-8'))
                return hash_obj.hexdigest()
                
            context['password'] =password

            mydata = User.objects.filter(username=username).values()
            for data in mydata:
                print(data['first_name'])
            if check_password(password, data['password']) == True:
                print('True')
                messages.success(request, "login success")
                return redirect('home') 
            else:
                print(make_password(data['password']))
                print(make_password(password))

    return render(request, 'base/signin.html', context)

def home(request):
    formField = SignupForm(request.POST)
    context = {}
    context['mydata'] = User.objects.all().values()
    return render(request, 'base/home.html', context) 


def posts(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('post_detail', pk=new_post.pk)
    else:
        post_form = PostForm()
    return render(request, 'base/posts.html', {'post_form': post_form})



# def posts(request):
#     context = {}
#     postmodel = Posts(request.POST)
#     context['postform'] = PostForm()
#     context['postmodel'] = Posts()
#     if request.method == 'POST':
#         postmodel.save()
#     return render(request, 'base/posts.html', context)


# def posts(request):
#     context = {}
#     context['postform'] = PostForm()
#     if request.method == 'POST':
#         postmodel = Posts(user=request.user, **request.POST)
#         postmodel.save()
#     context['postmodel'] = Posts()
#     return render(request, 'base/posts.html', context)


# def posts(request):
#     context = {}
#     context['postform'] = PostForm()
#     if request.method == 'POST':
#         postmodel = Posts(request.POST, user='franklin')
#         postmodel.save()
#     context['postmodel'] = Posts()
#     return render(request, 'base/posts.html', context)


# def posts(request):
#     context = {}
#     if request.method == 'POST':
#         postform = PostForm(request.POST)
#         if postform.is_valid():
#             post = postform.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('home')
#         else:
#             postform = PostForm()
#             context['postform'] = postform
#             context['posts'] = Posts.objects.all()
#     return render(request, 'base/posts.html', context)


def viewposts(request):
    context={}
    mydata = Posts.objects.all().values()
    # for datas in mydata:
    context['mydata'] = mydata 
    print(mydata)
    return render(request, 'base/viewposts.html', context)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import SignupForm, SigninForm, PostForm
from .models import AddPost, Comments, Reaction
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage as fs

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

def view_post(request):
    context = {}
    works = AddPost.objects.all()
    context['works'] = works
    return render(request, 'base/view-post.html', context)

def read_more(request, pk):
    context = {}

    update = AddPost.objects.get(id=pk)
    context['update'] = update


    if request.method == "POST":
        postValue = request.POST.get('readmoreBtn')
        if postValue == "reaction":
            # checker = Reaction.objects.filter(post_id = update.id, user_id = request.user.id).values()
            # print(checker)
            # print(request.user.id, update.id)
            # for i in checker:
            #     liked = i['like']
            # context['liked'] = liked
            # if len(checker) <= 0:
            #     reaction = Reaction.objects.create(
            #     user = request.user,
            #     post = update,
            #     like = True
            # )
            #     print("this page was just liked")
            # elif liked == False:
            #     print("about to unlike")
            #     Reaction.objects.filter(post_id = update.id, user_id = request.user.id).update(like = True)
            # elif liked == True:
            #     print("about to unlike")
            #     Reaction.objects.filter(post_id = update.id, user_id = request.user.id).update(like = False)
            return render(request, 'base/readmore.html', context)

        if postValue == "comment":
            message = Comments.objects.create(
                user = request.user,
                post = update,
                comment = request.POST.get('comment_input')
            )
        return redirect('readmore', pk=update.id)

        
    comments = update.comments_set.all().order_by("-created_at")
    context['comments'] = comments

    context['numberOfLikes'] = len(Reaction.objects.filter(post_id = update.id, like = True).values())


    return render(request, 'base/readmore.html', context)

def addpost(request):
    context = {}
    context['post_form'] = PostForm()
    post_form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        new_post = post_form.save(commit=False)
        new_post.author = request.user
        new_post.category = request.POST.get('category').lower()
        new_post.save()
        messages.success(request, "Post saved successfully")
        redirect('base/home')
    return render(request, 'base/addpost.html', context)

def category(request):
    context = {}
    if request.method == "POST":
        print(request.POST.get('search'))
        search = request.POST.get('search').lower()
        print(search)
        datas = AddPost.objects.filter(category=search)
        context['datas'] = datas
        print(datas)
    return render(request, "base/category.html", context)

def edit_post(request, pk):
    context = {}
    post = AddPost.objects.get(id=pk)
    context['post'] = PostForm(instance=post)
    return render(request, "base/edit-post.html", context)

def delete_post(request, pk):
    context = {}
    post = AddPost.objects.get(id=pk)
    context['post'] = post
    if request.method == 'POST':
        post.delete()
    return render(request, 'base/delete.html', context)
    
def delete_comment(request, pk):
    context = {}
    post = Comments.objects.get(id=pk)
    context['post'] = post
    if request.method == 'POST':
        post.delete()
    return render(request, 'base/deletecomment.html', context)




#  	UNIQUE constraint failed: auth_user.username
#  This password is too common.
# This password is entirely numeric.
# Error: Your passwords didn't match.
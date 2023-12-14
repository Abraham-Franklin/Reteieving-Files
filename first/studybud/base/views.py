from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import AddPost, Comments, Reaction
from .forms import SignupForm, SigninForm, AddPostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.core.files.storage import FileSystemStorage as fs
import random

# Create your views here.
def status(request):
    return render(request, 'base/status.html')
    
def signup(request):
    context = {}
    context['formfield'] = SignupForm()
    formfield = SignupForm(request.POST)
    if request.method == "POST":
        if formfield.is_valid():
            print(request.POST.get('username'))
            print(request.POST.get('password'))
            user = formfield.save(commit = False)
            query = User.objects.all().values()
            for name in query:
                print(name['username'])
                if user.username == name['username']:
                    messages.error(request, "Username already exist")
                else:
                    print('user creation successful')
            messages.success(request, 'User creation successful')
            user.save()
            return redirect('signin')
    
    return render(request, 'base/signup.html', context)

def signin(request):
    context = {}
    context['formfield'] = SigninForm()
    formfield = SigninForm(request.POST)
    if request.method == "POST":
        # username = formfield.cleaned_data['username']
        print(request.POST.get('username'))
        password = request.POST.get('password')
        username = request.POST.get('username')

        try:
            ### You can try thid method or the lower one
            # query = User.objects.filter(username = f"{username}").values()
            # print(query)
            # for data in query:
            #     if query:
            #         if data['password'] == password:
            #             print(True)

            user = authenticate(request, username=username, password=password)
            print(user, username, password)

            if user is not None:
                messages.success(request, 'You have been successfully logged in')
                login(request, user)
            return redirect('home')


        except:
            messages.error(request, "user doesn't exist!")

    return render(request, 'base/signin.html', context)


def user_profile(request, id):
    context = {}
    user = User.objects.get(id=id)
    context['user'] = user
    return render(request, 'base/profile.html', context)


def addpost(request):
    context = {}
    context['formfield'] = AddPostForm()
    form = AddPostForm(request.POST, request.FILES)
    if request.method == 'POST':
        context['form'] = form
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # Additional processing or redirection
            messages.success(request, "Post created successfully")
            return redirect('home')
    else:
        form = AddPost()
    return render(request, 'base/addpost.html', context)


def home(request):
    context = {}
    
    recentAnimePost = AddPost.objects.filter(category = 'Anime').values()
    recentEntertainmentPost = AddPost.objects.filter(category = 'Entertainment').values()
    recentSportsPost = AddPost.objects.filter(category = 'Sports').values()
    recentTechPost = AddPost.objects.filter(category = 'Tech').values()

    animeLength = len(recentAnimePost) - 1
    randomAnime = random.randint(0, animeLength)
    anime_list = list((recentAnimePost))
    print(anime_list[randomAnime]['id'])
    recentAnimePost = AddPost.objects.get(id = anime_list[randomAnime]['id'])
    context['recentAnimePost'] = recentAnimePost

    

    EntertainmentLength = len(recentEntertainmentPost) - 1
    randomEntertainment = random.randint(0, EntertainmentLength)
    entertainment_list = list((recentEntertainmentPost))
    recentEntertainmentPost = AddPost.objects.get(id = entertainment_list[randomEntertainment]['id'])
    context['recentEntertainmentPost'] = recentEntertainmentPost


    sportLength = len(recentSportsPost) - 1
    randomSports = random.randint(0, sportLength)
    sports_list = list((recentSportsPost))
    recentSportsPost = AddPost.objects.get(id = sports_list[randomSports]['id'])
    context['recentSportsPost'] = recentSportsPost


    sportsLength = len(recentTechPost) - 1
    randomTech = random.randint(0, sportsLength)
    tech_list = list((recentTechPost))
    recentTechPost = AddPost.objects.get(id = tech_list[randomTech]['id'])
    context['recentTechPost'] = recentTechPost

    return render(request, 'base/index.html', context)


def anime(request):
    context = {}
    updates = AddPost.objects.filter(category='Anime')
    context['updates'] = updates
    return render(request, 'base/anime.html', context)


def readmore(request, id):
    context = {}

    update = AddPost.objects.get(id=id)
    context['update'] = update


    if request.method == "POST":
        postValue = request.POST.get('readmoreBtn')
        if postValue == "reaction":
            checker = Reaction.objects.filter(post_id = update.id, user_id = request.user.id).values()
            print(checker)
            print(request.user.id, update.id)
            for i in checker:
                liked = i['like']
            context['liked'] = liked
            if len(checker) <= 0:
                reaction = Reaction.objects.create(
                user = request.user,
                post = update,
                like = True
            )
                print("this page was just liked")
            elif liked == False:
                print("about to unlike")
                Reaction.objects.filter(post_id = update.id, user_id = request.user.id).update(like = True)
            elif liked == True:
                print("about to unlike")
                Reaction.objects.filter(post_id = update.id, user_id = request.user.id).update(like = False)
            return render(request, 'base/readmore.html', context)

        if postValue == "comment":
            message = Comments.objects.create(
                user = request.user,
                post = update,
                comment_body = request.POST.get('comment_input')
            )
        return redirect('readmore', id=update.id)

        
    comments = update.comments_set.all().order_by("-created")
    context['comments'] = comments

    context['numberOfLikes'] = len(Reaction.objects.filter(post_id = update.id, like = True).values())


    return render(request, 'base/readmore.html', context)


def delete_comment(request, id):
    context = {}

    comment = Comments.objects.get(id=id)
    context['obj'] = comment

    if request.user != comment.user:
        return HttpResponse("You're not allowed to delete this!!!")

    if request.method == "POST":
        comment.delete()
        return redirect('readmore', id=id)
    return render(request, 'base/delete.html', context)


def sports(request):
    context = {}
    updates = AddPost.objects.filter(category='Sports')
    context['updates'] = updates
    return render(request, 'base/sports.html', context)



def tech(request):
    context = {}
    updates = AddPost.objects.filter(category='Tech')
    context['updates'] = updates
    return render(request, 'base/tech.html', context)



def entertainment(request):
    context = {}
    updates = AddPost.objects.filter(category='Entertainment')
    context['updates'] = updates
    return render(request, 'base/entertainment.html', context)
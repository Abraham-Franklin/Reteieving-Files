from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import UserProfileForm
from blog.models import Post, Category, Comment, Like, Follow
from blog.forms import PostForm, CommentForm, LikeForm

# User Authentication Views

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile', username=request.user.username)
    else:
        user_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'user_form': user_form})

# Blog Views

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    likes = post.likes.all()
    is_liked = Like.objects.filter(user=request.user, post=post).exists() if request.user.is_authenticated else False
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        like_form = LikeForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
        
        if like_form.is_valid() and not is_liked:
            like = like_form.save(commit=False)
            like.user = request.user
            like.post = post
            like.save()
            is_liked = True
    
    else:
        comment_form = CommentForm()
        like_form = LikeForm()
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'likes': likes,
        'comment_form': comment_form,
        'like_form': like_form,
        'is_liked': is_liked,
    })

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})
    else:
        return redirect('post_detail', pk=post.pk)

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('post_list')

# Category Views

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(categories=category).order_by('-created_at')
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

# User Profile Views

def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = user.userprofile
    posts = Post.objects.filter(author=user).order_by('-created_at')
    is_following = Follow.objects.filter(follower=request.user, following=user).exists() if request.user.is_authenticated else False
    return render(request, 'accounts/profile.html', {
        'user_profile': user_profile,
        'posts': posts,
        'is_following': is_following,
    })

@login_required
def follow_user(request, username):
    following_user = get_object_or_404(User, username=username)
    if request.user != following_user:
        follow, created = Follow.objects.get_or_create(follower=request.user, following=following_user)
    return redirect('profile', username=username)

@login_required
def unfollow_user(request, username):
    following_user = get_object_or_404(User, username=username)
    if request.user != following_user:
        Follow.objects.filter(follower=request.user, following=following_user).delete()
    return redirect('profile', username=username)


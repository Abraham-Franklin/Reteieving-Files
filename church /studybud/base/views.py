from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadImage, UploadVideo
from .forms import ImageForm, VideoForm
from django.core.files.storage import FileSystemStorage as fs

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

# def upload(request):
#     context = {}
#     image_form = ImageForm(request.POST, request.FILES)
#     context["image_form"] = ImageForm()
#     video_form = VideoForm(request.POST, request.FILES)
#     context["video_form"] = VideoForm()
#     if request.method == "POST":
#         get_value = request.POST.get("submit_btn")
#         if get_value == "images":
#             if image_form.is_valid():
#                 image_form.save()
#                 return render(request, 'base/upload.html', context)

#         elif get_value == "videos":
#             image_form.save()
#             return render(request, 'base/upload.html', context)

#     return render(request, 'base/upload.html', context)

def upload(request):
    context = {}
    context['formfield'] = ImageForm()
    form = ImageForm(request.POST, request.FILES)
    context['formvideo'] = VideoForm()
    formvideo = VideoForm(request.POST, request.FILES)
    if request.method == 'POST':
        receive = request.POST.get('submit-btn')
        if receive == "image-btn":
            context['form'] = form
            if form.is_valid():
                form.save()
        elif receive == "video-btn":
            context['formvideo'] = formvideo
            if formvideo.is_valid():
                formvideo.save()
    else:
        receive = request.POST.get('submit-btn')
        if receive == "image-btn":
            form = ImageForm()
        elif receive == "video-btn":
            form = VideoForm()
            
    return render(request, 'base/upload.html', context)

def download(request):
    context = {}
    imgs = UploadImage.objects.all()
    context['imgs'] = imgs

    # [img.image.url for img in imgs]
    print(imgs)
    return render(request, 'base/download.html', context)

def help(request):
    return render(request, 'base/help.html')
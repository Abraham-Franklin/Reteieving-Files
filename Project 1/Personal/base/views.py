from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SchoolName

# Create your views here.
def printout(request):
    context = {}
    if request.method == 'POST':
        show = request.POST['first_name']
        context['show'] = show
        # print(show)
        # return redirect('printout')
    return render(request, 'Home.html', context)


def showcase(request):
    context = {}
    context['form'] = SchoolName()
    formText = request.POST('school')
    # if request.mathod == "POST":
    if form.is_valid():
        context['formText'] = formText

    return render(request, 'Home.html', context)












# def showcase(request):
#     context ={}
#     context['form']= SchoolName()
#     formText = SchoolName(request.POST)
#     if formText.is_valid():
#         text = form.cleaned_data['school']
#     return render(request, 'Home.html', context)




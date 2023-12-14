from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))



Nigeria = [
    {
        "state" : 'Delta',
        "capital" : "Asaba"
    },
    {
        "state" : 'Cross-River',
        "capital" : "Calabar"
    },
    {
        "state" : 'Edo',
        "capital" : "Benin"
    },
    {
        "state" : 'Rivers',
        "capital" : "Port-Harcourt"
    },
    {
        "state" : 'Bayelsa',
        "capital" : "Yenogua"
    },
    {
        "state" : 'Kaduna',
        "capital" : "Kaduna"
    },
    {
        "state" : 'Plateau',
        "capital" : "Jos"
    }
]

def viewers(request):
    
    context = {"Nigeria" : Nigeria}
    return render(request, 'second.html', context)


def tester(request):
    return render(request, 'homePage.html')
from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm
from .forms import PhoneSearch

# Create your views here.
def showout(request):
    return HttpResponse("Studybud's active")


Phones = [
    {
        "brand" : 'Infinx',
        "name" : 'Infinx Hot 8 Lite',
        "specs" : '2GB Ram, 32GB Rom, 5500mAh, 3G Lte',
        "price" : '42,000'
    },
    {
        "brand" : 'Tecno',
        "name" : 'Tecno Camon 19',
        "specs" : '6GB Ram, 128GB Rom, 5000mAh, 4G Lte',
        "price" : '178,000'
    },
    {
        "brand" : 'Xiamo Redmi',
        "name" : 'Redmi Note 8',
        "specs" : '4GB Ram, 64GB Rom, 5000mAh, 4G Lte',
        "price" : '68,000'
    },
    {
        "brand" : 'Vivo',
        "name" : 'Vivo Y93s',
        "specs" : '6GB Ram, 128GB Rom, 4800mAh, 4G Lte',
        "price" : '78,000'
    },
    {
        "brand" : 'Samsung',
        "name" : 'Samsung Galaxy A32',
        "specs" : '6GB Ram, 128GB Rom, 4800mAh, 4G Lte',
        "price" : '210,000'
    },
    {
        "brand" : 'Iphone',
        "name" : 'Iphone 7',
        "specs" : '2GB Ram, 32GB Rom, 4000mAh, 4G Lte',
        "price" : '75,000'
    },

    {
        "brand" : 'Google Pixel',
        "name" : 'Google Pixel 4',
        "specs" : '6GB Ram, 128GB Rom, 5000mAh, 4G Lte',
        "price" : '178,000'
    },
    {
        "brand" : 'Infinx',
        "name" : 'Infinx S4',
        "specs" : '4GB Ram, 64GB Rom, 5000mAh, 4G Lte',
        "price" : '64,000'
    },
    {
        "brand" : 'Xiamo Redmi',
        "name" : 'Redmi Note 10 Pro',
        "specs" : '6GB Ram, 225GB Rom, 4800mAh, 4G Lte',
        "price" : '176,000'
    },
    {
        "brand" : 'Samsung',
        "name" : 'Samsung Galaxy S10',
        "specs" : '6GB Ram, 128GB Rom, 4500mAh, 4G Lte',
        "price" : '198,000'
    },
    
]

def testing(request):
    context = {}
    context['formText'] = PhoneSearch()
    context['Phones'] = Phones
    formText = PhoneSearch(request.POST)
    if formText.is_valid():
        inputValue = formText.cleaned_data['search']
    # inputValue = formText.cleaned_data['search']
        context['inputValue'] = inputValue
        # index = 0

        
        # for Phone in Phones:
        #     if index < len(Phones):
        #         print(Phone['brand'])
    return render(request, 'test.html', context)


def home_view(request):
    context = {}
    context['form']= InputForm()
    form = InputForm(request.POST)
    if form.is_valid():
        text_list = (form.cleaned_data['first_name'], form.cleaned_data['last_name'])
        # text = form.cleaned_data['first_name']
        context['text1'] = text_list[0]
        context['text2'] = text_list[1]
    return render(request, "djangoforms.html", context)


# def home_view(request):
#     context = {}
    
#     return render(request, "djangoforms.html", context)

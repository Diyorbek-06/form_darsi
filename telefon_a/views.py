from django.shortcuts import render

from .models import Phone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def phone_list(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/phone_list.html', context=context)

def phone_details(request, pk):
    phone = Phone.objects.get(id=pk)
    context = {'phone': phone}
    return render(request, 'phones/phone_details.html', context=context)
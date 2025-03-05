from django.shortcuts import render, redirect
from .forms import PhoneForm, ContactForm
from .models import Phone




# from django.shortcuts import render, redirect
# from django.template.context_processors import request



# from django.urls import reverse_lazy
# from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
# from django.views import View
# from .forms import PhoneForm, ContactForm
# from .models import Phone


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

# def phone_create(request):
#     if request.method == 'POST':
#         phone = Phone()
#         phone.brand = request.POST.get('brand', '')
#         phone.model = request.POST.get('model', '')
#         phone.year = request.POST.get('year', 0)
#         phone.color = request.POST.get('color', '')
#         phone.price = request.POST.get('price', 0)
#         phone.ishlatilingan_vaqt = request.POST.get('ishlatilingan_vaqt', 0)
#         phone.update_at = request.POST.get('update_at', '')
#         phone.created_at = request.POST.get('created_at', '')
#         phone.image = request.FILES.get('image', '')
#         phone.save()
#         return redirect('phone-list')
#
#     return render(request, 'phones/phone_create.html')



def phone_create_form(request):
   form = PhoneForm(request.POST, request.FILES)
   if form.is_valid():
       form.save()
       return redirect('phone-list')
   return render(request, 'phones/phone_create.html', {'form': form})






def phone_update(request, pk):
    phone = Phone.objects.get(id=pk)
    if request.method == 'POST':
        phone.brand = request.POST.get('brand', phone.brand)
        phone.model = request.POST.get('model', phone.model)
        phone.year = request.POST.get('year', phone.year)
        phone.color = request.POST.get('color', phone.color)
        phone.price = request.POST.get('price', phone.price)
        phone.ishlatilingan_vaqt = request.POST.get('ishlatilingan_vaqt', phone.ishlatilingan_vaqt)
        phone.image = request.FILES.get('image', phone.image)
        phone.save()
        return redirect('phone-detail', pk=pk)
    return render(request, 'phones/phone_update.html', {'phone': phone})



from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone

def phone_delete(request, pk):
    phone = get_object_or_404(Phone, id=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone-list')
    return render(request, 'phones/phone_delete.html', {'phone': phone})


def contact_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        print(f'Name: {name}, Phone: {phone_number}, Email: {email}, Message: {message}')
        return redirect('home')
    return render(request, 'contact.html', {'form': form})


# class PhoneList(ListView):
#     model = Phone
#     template_name = 'phones/phone_list.html'
#     context_object_name = 'phones'


# class PhoneDetail(DetailView):
#     model = Phone
#     template_name = 'phones/phone_details.html'
#     context_object_name = 'phone'


# class PhoneDelete(DeleteView):
#     model = Phone
#     success_url = reverse_lazy('phone-list')
#     template_name = 'phones/phone_delete.html'


# class PhoneCreate(CreateView):
#     model = Phone
#     form_class = PhoneForm
#     success_url = reverse_lazy('phone/list')
#     template_name = 'phones/phone_create.html'

# class PhoneCreate(View):
#     def get(self, request):
#         form = PhoneForm()
#         return render(request, 'phones/phone_create.html', {'form':form})


# #
#     def post(sel):
#         form = Phone(request.Post, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('phone-list')
#         return render(request, 'phones/phone_create.html', {'form':form})




# class PhoneUpdate(UpdateView):
#     model = Phone
#     form_class = PhoneForm
#     template_name = 'phones/phone_update.html'
#     context_object_name = 'phone'
#
#     def get_success_url(self):
#         return reverse_lazy('phone-detail', kwargs={'pk': self.object.pk})




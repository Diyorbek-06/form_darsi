from django.urls import path
from .views import home, phone_list, phone_details

urlpatterns = [
    path('', home, name='home'),
    path('phone-list', phone_list, name='phone-list'),
    path('phone/<int:pk>', phone_details, name='phone-detail'),
]
from django.urls import path
# from .views import home, PhoneDetail, \
#     contact_form, PhoneList, PhoneDelete, PhoneCreate, PhoneUpdate
from .views import home, phone_list, phone_details, phone_create_form, phone_update, phone_delete, \
    contact_form

urlpatterns = [
    path('', home, name='home'),
    path('phone-list', phone_list, name='phone-list'),
    path('phone/<int:pk>', phone_details, name='phone-detail'),
    path('phone-create/', phone_create_form, name='phone-create'),
    path('phone-update/<int:pk>/', phone_update, name='phone-update'),
    path('car-delete/<int:pk>/', phone_delete, name='phone-delete'),
    path('contact/', contact_form, name='contact'),
]







# urlpatterns = [
#     path('', home, name='home'),
#     path('phone-list', PhoneList.as_view(), name='phone-list'),
#     path('phone/<int:pk>', PhoneDetail.as_view(), name='phone-detail'),
#     path('phone-create/', PhoneCreate.as_view(), name='phone-create'),
#     path('phone-update/<int:pk>/', PhoneUpdate.as_view(), name='phone-update'),
#     path('car-delete/<int:pk>/', PhoneDelete.as_view(), name='phone-delete'),
#     path('contact/', contact_form, name='contact'),
# ]
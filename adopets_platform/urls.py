from . import views 
from django.urls import path
from .views import update_status , my_posted_pets,success_page, add_pet,delete_adoption_request,my_adoption_requests, edit_pet, delete_pet
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('adopt_request/<int:pet_id>/', views.adopt_request, name='adopt_request'),
    path('success/', success_page, name='success_page'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('my_adoption_requests/', my_adoption_requests, name='my_adoption_requests'),
    path('delete_adoption_request/<int:request_id>/', delete_adoption_request, name='delete_adoption_request'),
    path('received_adoption_requests/', views.received_adoption_requests, name='received_adoption_requests'),
    path('update_status/<int:request_id>/', update_status, name='update_status'),
    path('my-posted-pets/', my_posted_pets, name='my_posted_pets'),
    path('add-pet/', add_pet, name='add_pet'),
    path('edit_pet/<int:pet_id>/', edit_pet, name='edit_pet'),
    path('delete_pet/<int:pet_id>/', delete_pet, name='delete_pet'),
    path('update_status/<int:request_id>/', views.update_status, name='update_status'),

] 






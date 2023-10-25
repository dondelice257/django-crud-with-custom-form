from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.merchandises, name='list'),
    path('<int:id>', views.merchandises_details, name="details"),
    path('contact/', views.contact, name='contact'),
    path('add/', views.merchant_create, name='add'),
    path('<int:id>/change/', views.merchant_update, name='change'),
    path('<int:id>/delete/', views.merchant_delete, name='change'),
    
    
    
    
]

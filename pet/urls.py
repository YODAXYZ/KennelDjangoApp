from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from pet import views

app_name = 'pet'
urlpatterns = [
    path('', views.PetListView.as_view(), name='index'),
    path('about/', views.AboutUsVies.as_view(), name='about'),
    path('contact/', views.ContactsView.as_view(), name='contact'),
    path('pets/<str:pk>/', views.PetView.as_view()),
]

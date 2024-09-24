from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('create_person/', views.create_person, name='create_person'),
    path('persons/', views.PersonListView.as_view(), name='list_persons'),
    path('delete/<int:person_id>/', views.delete_person, name='delete_person'), 
     ]
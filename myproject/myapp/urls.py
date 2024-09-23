from django.urls import path
from . import views 


urlpatterns = [
    path('index/', views.index, name='index'),
    path('create_person/', views.create_person, name='create_person'),
    path('list_persons/', views.list_persons, name='list_persons'),
]
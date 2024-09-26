from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view()),
    path('indexTemplate', views.indexTemplate.as_view()),
    path('users/', views.user_list.as_view(), name='user-list'),
    path('user_form/', views.user_form.as_view(), name='user_form-list'),
    path('inherit_view/', views.inherit_view.as_view(), name='inherit_view'),
]


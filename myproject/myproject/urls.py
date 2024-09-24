from django.contrib import admin
from django.urls import include, path
from myapp import views
#Customizing the admin
admin.site.site_header = "Code with Bhushan" 
admin.site.site_title = "Welcome to the world of Bhushan"
admin.site.index_title = "Welcome to the world of Bhushan"



urlpatterns = [
    path('', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
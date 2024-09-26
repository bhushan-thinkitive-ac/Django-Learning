from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import User
from django.views.generic.base import View
from .forms import UserForm

# Create your views here.

""" Function Based View """
# def index(request):
#     return HttpResponse("This is my app")

""" Class Based Views """
class index(View):
    def get(self, request):
        return render(request, 'index.html')
    
class indexTemplate(View):
    def get(self, request):
        context = {"Notice": "You might have came to the localhost page. By the way it is class based view which is parsing the context"}
        return render(request, 'index.html', context)

class user_list(View):
    Name = "Bhushan Chaudhari"
    def get(self, request):
        users = list(User.objects.values())
        return JsonResponse(users, safe=False)

class inherit_view(user_list):
    def get(self, request):
        return HttpResponse(self.Name)


class user_form(View):
    def get(self, request):
        form = UserForm()
        return render(request,'form.html', {'form':form})
    
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your form has been successfully created. ")
        else:
            return render(request, 'form.html', {'form': form})
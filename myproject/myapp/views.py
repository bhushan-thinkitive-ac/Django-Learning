from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from myapp.models import Person



# Create your views here.


def home(request):
    templates = loader.get_template('home.html')
    return HttpResponse(templates.render())

def index(request):
    templates = loader.get_template('index.html')
    return HttpResponse(templates.render())

    
def create_person(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if first_name and last_name: 
            person = Person(first_name=first_name, last_name=last_name)
            person.save()
            return HttpResponse("Person created!")
        else:
            return HttpResponse("Please provide both first name and last name.")
    
    return render(request, 'form.html')



class PersonListView(ListView):
    model = Person
    template_name = 'list.html'  
    context_object_name = 'persons'  


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('list_persons')  # Redirect to the list of persons after deletion
    return HttpResponse("Invalid request method.", status=405)

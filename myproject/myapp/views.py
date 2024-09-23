from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from myapp.models import Person



# Create your views here.


def index(request):
    templates = loader.get_template('index.html')
    return HttpResponse(templates.render())

    
def create_person(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if first_name and last_name:  # Basic validation
            person = Person(first_name=first_name, last_name=last_name)
            person.save()
            return HttpResponse("Person created!")
        else:
            return HttpResponse("Please provide both first name and last name.")
    
    return render(request, 'form.html')



def list_persons(request):
    persons = Person.objects.all()  # Retrieve all Person instances
    return render(request, 'list.html', {'persons': persons})

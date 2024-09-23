from django import forms
from myapp.models import Person
from django.http import HttpResponse
from django.shortcuts import render



class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

# In your view
def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Person created!")
    else:
        form = PersonForm()
    
    return render(request, 'your_template.html', {'form': form})

from django.contrib import admin

from .models import Person, User, Dean, Teacher, Student, Subject

# Register your models here.

admin.site.register(Person)
admin.site.register(User)
admin.site.register(Dean)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
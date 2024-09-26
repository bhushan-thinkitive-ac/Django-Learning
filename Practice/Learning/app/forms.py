from django import forms
from .models import User, Person, Dean, Teacher, Subject, Student

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Email', 'Password']

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'gender']

class DeanForm(forms.ModelForm):
    class Meta:
        model = Dean
        fields = ['dean_name', 'dean_email']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'teacher_email', 'teacher_sub']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name', 'subject_code', 'subject_teacher']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'student_email', 'course', 'dean', 'teacher']

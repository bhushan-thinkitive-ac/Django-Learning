from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200, default = 'example@django.com', primary_key = True)
    Password = models.CharField(max_length=200)
    class Meta:
        db_table = 'User'
    
    def __str__(self):
        return f"{self.Username} | {self.Email}"

class Person(models.Model):
    first_name = models.CharField(max_length=200, null= True)
    last_name = models.CharField(max_length=200, blank = True)
    GENDER_CHOICES = (
        ('M', 'Male'),('F', 'Female') ,('O', 'Trans'),
    )
    gender = models.CharField(max_length=1, choices = GENDER_CHOICES, null=True)

    def __str__(self):
        return f"{self.first_name} | {self.last_name} | {self.gender}"


class Dean(models.Model):
    dean_name = models.CharField(max_length=200)
    dean_email = models.EmailField(max_length=200, default = 'example@django.com', unique= True)

    class Meta():
        db_table = 'Dean'

    dean = models.Manager()
    
    def __str__(self):
        return f"{self.dean_name}"

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=200)
    teacher_email = models.EmailField(max_length=200, default = 'example@django.com', unique=True)
    teacher_sub = models.CharField(max_length=200, null = True)

    teacher = models.Manager()


    class Meta():
        ordering = ['teacher_name']
        verbose_name = "Teacher's list"
        db_table = 'Teacher'



    def __str__(self):
        return f"{self.teacher_name} | {self.teacher_sub}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=200, null = True)
    subject_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null = True)

    class Meta():
        ordering = ['subject_code']
        verbose_name = "List of Subjects"
        db_table = 'Subject'

    def __str__(self):
        return f"{self.subject_code} | {self.subject_name}"


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length=200, default = 'example@django.com', unique=True)
    course = models.JSONField(max_length = 200, default = 'Computer Science', null = True)
    

    dean = models.ForeignKey(Dean, on_delete=models.CASCADE, null=True)
    teacher = models.ManyToManyField(Teacher)

    class Meta():
        db_table = 'Student'
    
    def __str__(self):
        return f"{self.student_name} | {self.student_email} | {self.course}"
    



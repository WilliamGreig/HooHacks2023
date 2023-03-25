from django.db import models

# Create your models here.
class Student(models.Model):
    computing_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.computing_id + ": " + self.first_name + " " + self.last_name

class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    link = models.CharField(max_length=200)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title + ": " + self.due_date

class Course(models.Model):
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=30)
    assignments = models.ManyToManyField(Assignment)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.department + ": " + self.title

class Instructor(models.Model):
    computing_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.computing_id + ": " + self.first_name + " " + self.last_name

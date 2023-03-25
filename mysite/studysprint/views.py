from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# main page
def index(request):
    return render(request, "index.html")


# specific course information
def course_page(request, id):
    course = Course.objects.get(id=id)
    return render(request, "course.html", {'course': course})


# general courses -- your courses and link to join more courses (another page)
def courses(request):
    course_list = Course.objects.all()
    return render(request, "courses.html", {'course_list': course_list})


def assignment(request):
    return render(request, "assignment.html")

# general assignments page
def assignments(request):
    return render(request, "assignments.html")

def create_course(request):
    if request.method == "POST":
        course = Course(title=request.POST['title'], department=request.POST['department']  )
        course.save()
    return render(request, "addcourse.html")

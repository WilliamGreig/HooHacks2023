from django.shortcuts import render
from django.http import HttpResponse

# main page
def index(request):
    return render(request, "index.html")


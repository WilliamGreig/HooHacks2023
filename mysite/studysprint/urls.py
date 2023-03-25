from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses),
    path('course/create', views.create_course),
    path('course/<int:id>/', views.course_page)
]

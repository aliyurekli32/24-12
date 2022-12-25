from django.urls import path
from .views import (
    home,
    students_list,
    student_create,
) 

urlpatterns = [
    path("", home),
    path("student-list/", students_list, name='list'),
    path("student-create/", student_create, name='create'),
]

from django.views.generic import ListView
from django.shortcuts import render

from .models import Student



class Students_list(ListView):
    model = Student
    template_name = 'school/students_list.html'

    def get_queryset(self):
        return Student.objects.all().prefetch_related('teacher')

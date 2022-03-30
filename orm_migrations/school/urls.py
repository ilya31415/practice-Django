from django.urls import path

# from school.views import students_list
from school.views import Students_list

urlpatterns = [
    path('', Students_list.as_view(), name='students'),
]

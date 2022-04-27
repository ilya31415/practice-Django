from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course, Student



class  StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("birth_date", "name")

    def count_all_objects_class(self):
        return Student.objects.all().count()

    def validate(self, attrs):
        len_course = self.count_all_objects_class()
        if self.context['request'].method == 'POST':
            if len_course >= MAX_STUDENTS_PER_COURSE:
                raise ValidationError('Превышено количество студентов на курсе')

        return attrs

class CourseSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")
        read_onle_fields = ("students")




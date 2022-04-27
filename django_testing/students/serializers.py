from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_testing.settings import MAX_STUDENTS_PER_COURSE
from students.models import Course, Student



class  StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ("birth_date", "name")





class CourseSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True)

    class Meta:
        model = Course
        fields = ("id", "name", "students")


    #

    def create(self, validated_data):
        students = validated_data.pop('students')
        сourse = Course.objects.create(**validated_data)
        for student in students:
            сourse.students.create(**student)
        return сourse

    def len_student_course(self, students):
        return len(students)


    def validate_students(self, students):
        len_objects_student_in_course = self.len_student_course()

        if self.context['request'].method == 'POST':
            if len_objects_student_in_course >= MAX_STUDENTS_PER_COURSE:
                raise ValidationError('Превышено количество студентов на курсе')

        return students


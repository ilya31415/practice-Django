from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from students.models import Student, Course
from students.serializers import StudentsSerializer


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture()
def method_post():
    class Request():
        def __init__(self):
            self.method = 'POST'

    return Request()

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_api_one_course(client, course_factory):
    # arrange
    course = course_factory(_quantity=1)
    course_id = course[0].id

    # act
    response = client.get(f'/api/v1/courses/{course_id}/')
    # assert

    assert response.status_code == 200
    data = response.json()

    assert data['name'] == course[0].name


@pytest.mark.django_db
def test_api_many_course(client, course_factory):
    # arrange
    course = course_factory(_quantity=10)
    # act
    response = client.get('/api/v1/courses/')
    # assert

    assert response.status_code == 200
    data = response.json()

    for index, obj_cours in enumerate(data):
        assert obj_cours['name'] == course[index].name


@pytest.mark.django_db
def test_api_course_filter_id(client, course_factory):
    # arrange

    course = course_factory(_quantity=5)
    id_course = course[3].id
    # act
    response = client.get(f'/api/v1/courses/?id={id_course}')
    # assert

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == id_course


@pytest.mark.django_db
def test_api_course_filter_name(client, course_factory):
    # arrange
    course = course_factory(_quantity=10)
    name_course = course[5].name
    # act
    response = client.get(f'/api/v1/courses/?name={name_course}')
    # assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == name_course


@pytest.mark.django_db
def test_api_create_course(client, course_factory):
    # arrange
    count = Course.objects.count()
    # act
    response = client.post('/api/v1/courses/', data={'name': 'Python-developer'})
    # assert
    assert response.status_code == 201
    assert count + 1 == Course.objects.count()


@pytest.mark.django_db
def test_api_update_course(client, course_factory):
    # arrange

    course = course_factory(_quantity=1)
    id_course = course[0].id
    new_name = 'Java-developer'
    # act
    response = client.patch(f'/api/v1/courses/{id_course}/', data={'name': new_name})
    # assert
    assert response.status_code == 200
    actual_name = Course.objects.all()[0].name
    assert actual_name == new_name


@pytest.mark.django_db
def test_api_delete_course(client, course_factory):
    # arrange

    course = course_factory(_quantity=1)
    count = Course.objects.count()
    id_course = course[0].id
    new_name = 'Java-developer'
    # act
    response = client.delete(f'/api/v1/courses/{id_course}/')
    # assert
    assert response.status_code == 204

    assert count - 1 == Course.objects.count()


@pytest.mark.django_db
def test_api_create_students(client, student_factory):
    # arrange
    students = student_factory(_quantity=20)
    count = Student.objects.all().count()
    # act
    response = client.post(f'/api/v1/students/', data={'name': 'Poll'})
    # assert
    assert response.status_code == 400
    assert count == Student.objects.all().count()





@pytest.mark.parametrize('real_db, result', [(19, True), (20, False)])
def test_api_create_students_on_settings(result, real_db, method_post, monkeypatch):

    def mock_len_course(*args, **kwargs):
        return real_db

    monkeypatch.setattr('students.serializers.StudentsSerializer.count_all_objects_class',  mock_len_course)

    serializ = StudentsSerializer(data={'name': 'Poll'}, context={'request': method_post})

    assert serializ.is_valid() == result
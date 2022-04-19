from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorRetrieve, SensorChange

urlpatterns = [

    path('sensors/', SensorView.as_view()),  # список датчиков get и создать датчик при post
    path('sensors/<pk>/', SensorChange.as_view()),  # изменить датчик/получить информацию по конкретному датчику
    path('measurements/', MeasurementView.as_view()),  # Добавить измерение post и вывести все измерения get

]

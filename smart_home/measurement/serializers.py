from rest_framework import serializers
from .models import Measurement, Sensor


class SensorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'data_measurement']



class FullInfoSensor(serializers.ModelSerializer):
    sensor = SensorSerializer()

    class Meta:
        model = Measurement
        fields = ['sensor',  'temperature', 'data_measurement']

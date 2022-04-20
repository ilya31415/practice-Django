from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, FullInfoSensor


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response({'get': ser.data})

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data})
        else:
            return Response({'post': 'невалидные данные'})


class MeasurementView(APIView):
    def get(self, request):
        sensors = Measurement.objects.all()
        ser = MeasurementSerializer(sensors, many=True)
        return Response({'get': ser.data})

    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data})
        else:
            return Response({'post': 'невалидные данные'})


class SensorChange(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieve(RetrieveAPIView):
    queryset = Measurement.objects.all()
    serializer_class = FullInfoSensor

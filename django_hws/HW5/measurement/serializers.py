from rest_framework import serializers
from .models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(allow_empty_file=True, allow_null=True)

    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at', 'picture']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']

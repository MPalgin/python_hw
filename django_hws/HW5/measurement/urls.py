from django.urls import path
from .views import CreateSensorView, SensorChange, MeasurementCreate
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>', SensorChange.as_view()),
    path('measurements/', MeasurementCreate.as_view())
]

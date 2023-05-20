from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from machinelearning import mlmodel

from .models import Sensor, SensorLog, Actuator, ActuatorLog

class SensorTemplateView(APIView):
    sensor_name = ""
    graph_name = ""
    def get(self, request, format=None):
        sensor = Sensor.objects.get(name=self.sensor_name)
        raw_data = reversed(SensorLog.objects.filter(name__name__exact=self.sensor_name).order_by('-id')[:10])
        time_data = []
        log_data = []
        chart_label = self.graph_name
        for log in raw_data:
            time_data.append(log.time.strftime("%x %X"))
            log_data.append(log.value)
        data = {
            "value": sensor.value,
            "time_data": time_data,
            "chart_data": log_data,
            "chart_label": chart_label
        }
        return Response(data)

class ActuatorTemplateView(APIView):
    actuator_name = ""
    sensor1_name = ""
    sensor2_name = ""
    sensor3_name = ""
    model = ""
    graph_name = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1 = Sensor.objects.get(name=self.sensor1_name)
        sensor2 = Sensor.objects.get(name=self.sensor2_name)
        sensor3 = Sensor.objects.get(name=self.sensor3_name)
        prediction = self.model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        actuator_log = ActuatorLog(name=actuator, state=actuator.state)
        actuator_log.save()
        
        raw_data = reversed(ActuatorLog.objects.filter(name__name__exact=self.actuator_name).order_by('-id')[:10])
        time_data = []
        log_data = []
        chart_label = self.graph_name
        for log in raw_data:
            time_data.append(log.time.strftime("%x %X"))
            log_data.append(log.state)
        data = {
            "state": actuator.state,
            "time_data": time_data,
            "chart_data": log_data,
            "chart_label": chart_label
        }
        return Response(data)
    

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


class TemperatureView(SensorTemplateView):
    sensor_name = "Temperature"
    
class SoilMoistureView(SensorTemplateView):
    sensor_name = "Soil Moisture"

class LightIntensityView(SensorTemplateView):
    sensor_name = "Light Intensity"
    
class IrrigationView(ActuatorTemplateView):
    actuator_name = "Irrigation System"
    sensor1_name = "Temperature"
    sensor2_name = "Soil Moisture"
    sensor3_name = "Light Intensity"
    model = mlmodel.irrigation_model
from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    path('sensor/temperature', views.TemperatureView.as_view()),
    path('sensor/moisture', views.SoilMoistureView.as_view()),
    path('sensor/light', views.LightIntensityView.as_view()),
    path('actuator/irrigation', views.IrrigationView.as_view()),
]
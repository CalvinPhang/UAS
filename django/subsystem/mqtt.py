import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

def on_connect(client, userdata, rc, result):
    client.subscribe('smartfarm/#')

on_message_temperature = on_message_mqtt('Temperature')
on_message_moisture = on_message_mqtt('Soil Moisture')
on_message_light = on_message_mqtt('Light Intensity')

client = mqtt.Client()

client.message_callback_add('smartfarm/temperature', on_message_temperature)
client.message_callback_add('smartfarm/soil', on_message_moisture)
client.message_callback_add('smartfarm/light', on_message_light)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)

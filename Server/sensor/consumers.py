from channels.consumer import SyncConsumer
import json
from .models import Sensor, SensorData
from datetime import datetime


class SensorConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Accept")
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        sensor_name = self.scope['url_route']['kwargs']['sensor']
        sensor_data_raw = event['text']
        sensor_data = json.loads(sensor_data_raw)
        print(sensor_data)
        for i, value in enumerate(sensor_data["values"]):
            queried_sensor = Sensor.objects.get(name=sensor_name)
            s = SensorData(
                sensor=queried_sensor,
                value=value,
                timestamp=datetime.fromtimestamp((int(sensor_data["timestamp"])+i*int(sensor_data["delay"]))/1000)
            )
            s.save()

        self.send({
            "type": "websocket.send",
            "text": "thanks: " + sensor_name,
        })
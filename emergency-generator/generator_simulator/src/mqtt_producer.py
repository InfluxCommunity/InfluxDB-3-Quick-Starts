import paho.mqtt.client as mqtt
import json


class mqtt_publisher:
    def __init__(self, address, port, clientID) -> None:
       
        self.mqttBroker = address
        self.port = port
        self.clientID = clientID
        self.client = None

    

    def connect_client(self):
        MQTT_KEEPALIVE_INTERVAL = 45
        self.client = mqtt.Client(self.clientID)
        self.client.connect(host=self.mqttBroker,port=self.port, keepalive=MQTT_KEEPALIVE_INTERVAL)

    def connect_client_secure(self, username, password):
        MQTT_KEEPALIVE_INTERVAL = 60
        self.client = mqtt.Client(self.clientID)
        self.client.connect(host=self.mqttBroker,port=self.port, keepalive=MQTT_KEEPALIVE_INTERVAL)
        self.client = mqtt.Client(self.clientID)
        self.client.connect(self.mqttBroker)
        self.client.tls_set()  # <--- even without arguments
        self.client.username_pw_set(username=username, password=password)


    def publish_to_topic(self, topic: str, data: dict):
        topic = topic +"/"+ str(data["generatorID"])
        message = json.dumps(data)
        self.client.publish(topic, message)
        print("succcesfully delivered message to MQTT topic")
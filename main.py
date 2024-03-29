from mqtt import *
import time
import random

def mqtt_callback(msg):
    print("Main.py  ---", msg)

def mqtt_publish(mqttobj, topic, msg):
    mqttobj.publish(topic, msg)


mqttObject = MQTTHelper()
mqttObject.setRecvCallBack(mqtt_callback)

time.sleep(5)
mqtt_publish(mqttObject, mqttObject.MQTT_TOPIC, 2)

while True:
    value = random.randint(15,28)
    print("Update: ", value)
    mqtt_publish(mqttObject, mqttObject.MQTT_TOPIC_TEMP, value)
    time.sleep(30)
    pass

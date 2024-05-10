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
    temp = random.randint(15,28)
    humid = random.randint(40,80)
    co2 = random.randint(40,80)
    print("Temp: ", temp)
    print("Humid: ", humid)
    print("CO2: ", co2)
    mqtt_publish(mqttObject, mqttObject.MQTT_TOPIC_TEMP, temp)
    mqtt_publish(mqttObject, mqttObject.MQTT_TOPIC_HUMID, humid)
    mqtt_publish(mqttObject, mqttObject.MQTT_TOPIC_CO2, co2)

    time.sleep(10)

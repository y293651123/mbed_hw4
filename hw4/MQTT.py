import paho.mqtt.client as paho
import matplotlib.pyplot as plt
import numpy as np
import time

mqttc = paho.Client()

t = np.arange(0, 20, 0.1)
x = np.arange(0, 1, 1 / 200)
y = np.arange(0, 1, 1 / 200)
z = np.arange(0, 1, 1 / 200)
log = np.arange(0, 1, 1 / 200)

host = "localhost"
topic= "Mbed"
port = 1883

def on_connect(self, mosq, obj, rc):
    print("Connected rc: " + str(rc))

def on_message(mosq, obj, msg):
    data = str(msg.payload)
    data = data.split()
    x[0] = 0
    for i in range(1, 200):
        x[i] = float(data[i])
    for i in range(0, 200):
        y[i] = float(data[i + 200])
    for i in range(0, 200):
        z[i] = float(data[i + 400])
    for i in range(0, 200):
        log[i] = float(data[i + 600])

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t,x, color = "blue", linewidth = 1, linestyle = "-", label = "x")
    ax[0].plot(t,y, color = "red", linewidth = 1, linestyle = "-", label = "y")
    ax[0].plot(t,z, color = "green", linewidth = 1, linestyle = "-", label = "z")
    ax[0].set_ylabel('Acc Vector')
    ax[0].set_xlabel('Time')
    ax[0].legend()
    ax[1].stem(t, log, use_line_collection = True)
    ax[1].set_ylabel('Tilt')
    ax[1].set_xlabel('Time')
    plt.show()

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed OK")

def on_unsubscribe(mosq, obj, mid, granted_qos):
    print("Unsubscribed OK")

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_unsubscribe = on_unsubscribe

print("Connecting to " + host + "/" + topic)
mqttc.connect(host, port=1883, keepalive=60)
mqttc.subscribe(topic, 0)

mqttc.loop_forever()
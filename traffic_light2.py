import  RPi.GPIO    as  GPIO
import  time
import  paho.mqtt.client    as  mqtt
hostname    =   "iot.eclipse.org"
port    =   1883
topic_state =   "3030044347/newer"
red_led =   3
green_led   =   4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led,   GPIO.OUT)
#   Define  Paho    MQTT    client  callback    functions
def on_connect(client,  userdata,   flags,  rc):
    #   Successful  connection  is  '0'
    print("[MQTT]   Connection  result: "   +   str(rc))

def on_publish(client,  userdata,   mid):
    print("[MQTT]   Sent:   "   +   str(mid))
def on_disconnect(client,   userdata,   rc):
    if  rc  !=  0:
        print("[MQTT]   Disconnected    unexpectedly")

#   Define  a   function    to  control the traffic light
def light_state(red_state,  green_state):
    GPIO.output(red_led,    red_state)
    GPIO.output(green_led,  green_state)

print("Traffic    Light   Simulation")
mqttc   =   mqtt.Client()
mqttc.on_connect    = on_connect
mqttc.on_publish    =   on_publish
mqttc.on_disconnect =   on_disconnect
mqttc.connect(hostname, port=port,  keepalive=60,   bind_address="")
mqttc.loop_start()
#   Main    loop
try:
    while   True:
        #   starts  at  Green   light
        print("State    1   - Green Light")
        mqttc.publish(topic_state,  1,  qos=0,  retain=False)
        light_state(0,  1)
        time.sleep(5)
        #   blink   the Green   light
        print("State    2   - Blinking  Green   Light")
        mqttc.publish(topic_state,  2,  qos=0,  retain=False)
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        light_state(0,  0)
        time.sleep(0.5)
        light_state(0,  1)
        time.sleep(0.5)
        #   change  to  Red light
        print("State    3   - Red   Light")
        mqttc.publish(topic_state,  3,  qos=0,  retain=False)
        light_state(1,  0)
        time.sleep(5)

except  KeyboardInterrupt:
    print("Ctrl+C pressed.    Terminating...")

finally:
    GPIO.cleanup()
    print("GPIO   pins    cleaned up  successfully.")

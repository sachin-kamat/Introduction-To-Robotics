import network
import machine
from time import sleep

wlan = network.WLAN()

def connect_to_wifi(ssid, password):
    wlan.active(True)
    print("start")
    while True:
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(ssid, password)
            if not wlan.isconnected():
                machine.idle()
                sleep(1)
            print('network config: ', wlan.ipconfig('addr4'))
    

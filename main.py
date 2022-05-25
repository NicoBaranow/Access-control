import NFC_PN532 as nfc
import PN532
from machine import Pin
import time
import utime 

led = Pin(2,Pin.OUT)
iman = Pin(15,Pin.OUT)
but = Pin(4,Pin.OUT)
profesores = ["abc","abcc","aaccas"]

iman.value(0)
intTime = 0
debTime = 100


#Interrupcion apertura desde dentro
def abrir(Pin):
    global intTime
    if utime.ticks_diff(utime.ticks_ms(), intTime) > debTime:
        led.value(1)
        iman.value(1)
        print("Funcion abrir")
        time.sleep(3)
        print("Funcion abrir terminada")
        led.value(0)
        iman.value(0)
        intTime = utime.ticks_ms()

but.irq(handler=abrir, trigger=Pin.IRQ_FALLING)

#PN532 initiation
PN532.init()

print("Waiting for RFID/NFC card...")

uid = PN532.access() 

if uid in 
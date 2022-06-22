# import NFC_PN532 as nfc
import PN532
from machine import Pin, PWM, Timer
import time
# from timeit import default_timer as timer

led = Pin(19,Pin.OUT)
led1 = Pin(18,Pin.OUT)
iman = Pin(12,Pin.OUT)
but = Pin(33,Pin.IN, Pin.PULL_DOWN)
speaker = PWM(Pin(5))
# tim = Timer()
# tim.init(period = 1000, mode=Timer.PERIODIC, callback = temporizador)

sentido = True
contador = 0

led.value(0)
led.value(0)
speaker.freq(1)
speaker.duty(0)
iman.value(0)

intTime = 0
debTime = 100

profesores = ["51:75:24:d9", "b6:71:61:5e", "82:f5:97:4", "4:5a:10:b2:73:57:80", "c2:8a:dc:29", "4:8c:71:82:73:57:80", "a2:89:69:dd", "cf:5e:4e:38", "2f:5:26:4", "af:f3:33:59", "c3:7c:44:19", "4:73:1f:52:4b:5f:80", "b3:3b:99:14", "4:8a:26:52:4e:5f:80", "ef:e5:11:34", "4:69:c:2:7c:56:80"]

#apertura
def puerta():
        led.value(1)
        led1.value(1)
        iman.value(1)
        speaker.freq(2000)
        speaker.duty(900)
        time.sleep(2)
        speaker.freq(1)
        speaker.duty(0)
        led.value(0)
        led1.value(0)
        iman.value(0)

#Handler interrupcion
def abrir(Pin):
    print("6")
    global intTime
    if time.ticks_diff(time.ticks_ms(), intTime) > debTime and but.value() == 1:
        print("interrupcion ejecutada")
        puerta()
        intTime = time.ticks_ms()

#interrupcion boton
but.irq(handler=abrir, trigger=Pin.IRQ_RISING)

#PN532 iniciacion
PN532.init()

print("Esperando un tag RFID/NFC...")

while True:
    uid = ""
    uid = PN532.access()
    if uid in profesores:
        print("tarjeta habilitada")
        puerta()


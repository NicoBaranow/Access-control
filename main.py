# import NFC_PN532 as nfc
import PN532
from machine import Pin
import time
import utime 
# from timeit import default_timer as timer

led = Pin(2,Pin.OUT)
iman = Pin(12,Pin.OUT)
but = Pin(33,Pin.IN, Pin.PULL_DOWN)
profesores = []

intTime = 0
debTime = 100

iman.value(0)

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

print("Esperando un tag RFID/NFC...")

while True:
    uid = ""
    imp = ""
    uid = PN532.access() 
    inp = input()

    while inp == "":
                
        if uid in profesores:
            start = timer()
            
            while start <= 3000000:
                iman.value(1)
                
            iman.value(0)
            
        else:
            print("El tag no está registrado")
            
    while inp == "1":
        print("Apoye un tag para agregar a los tags autorizados")
        if uid != "": #no va a llegar a leer el tag por lo que va a aparecer como que nunca se apoya, tal vez la solucion es no inicializarlo en "" al principio,
                      #lo mismo para el inp
            profesores.append(uid)
            print("Accion completada con exito! los tags autorizados son: " + profesores)
        else:
            print("Error! No se ha encontrado un tag")
            
    while inp == "0":
        print("Apoye un tag para remover de los tags autorizados")
        if uid != "": #no va a llegar a leer el tag por lo que va a aparecer como que nunca se apoya, tal vez la solucion es no inicializarlo en "" al principio,
                      #lo mismo para el inp
            profesores.remove(uid)
            print("Accion completada con exito! los tags autorizados son: " + profesores)
        else:
            print("Error! No se ha encontrado un tag")


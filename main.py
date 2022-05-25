from tkinter.tix import InputOnly
import NFC_PN532 as nfc
import PN532
from machine import Pin
import time
import utime 
from timeit import default_timer as timer

led = Pin(2,Pin.OUT)
iman = Pin(15,Pin.OUT)
but = Pin(4,Pin.OUT)
profesores = []

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

print("Esperando un tag RFID/NFC...")

while True:
    uid = ""
    imp = ""
    uid = PN532.access() 
    inp = input()

    if uid in profesores:
        start = timer()
        iman.value(1)
        #time.sleep(300)
        #iman.value(0)
        if start >= 3000000: #supongo que siempre quedara abierto
            iman.value(0)
    else:
        print("El tag no está registrado")

    if inp == "1":
        print("Apoye un tag para agregar a los tags autorizados")
        if uid != "": #no va a llegar a leer el tag por lo que va a aparecer como que nunca se apoya, tal vez la solucion es no inicializarlo en "" al principio,
                      #lo mismo para el inp
            profesores.append(uid)
            print("Accion completada con exito! los tags autorizados son: " + profesores)
        else:
            print("Error! No se ha encontrado un tag")
        
    if inp == "0":
        print("Apoye un tag para remover de los tags autorizados")
        if uid != "": #no va a llegar a leer el tag por lo que va a aparecer como que nunca se apoya, tal vez la solucion es no inicializarlo en "" al principio,
                      #lo mismo para el inp
            profesores.remove(uid)
            print("Accion completada con exito! los tags autorizados son: " + profesores)
        else:
            print("Error! No se ha encontrado un tag")

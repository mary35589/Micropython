# boot.py -- run on boot-up
from time import sleep
from machine import Pin
from machine import mem32

rojopeatonal=Pin(36,Pin.OUT)
verdepeatonal=Pin(39,Pin.OUT)
verdevehicular=Pin(32,Pin.OUT)
amarillovehicular=Pin(35,Pin.OUT)
rojovehicular=Pin(34,Pin.OUT)


global variable
variable=0

def interrupcion(Pin):
    global variable
    print("Entre a la función interrupción")
    variable=1
       
pulsador= Pin(23, Pin.IN,Pin.PULL_DOWN)
pulsador.irq(trigger=Pin.IRQ_FALLING, handler=interrupcion)

GPIO_SET=const(0x3FF44004)

while True:
    mem32[GPIO_SET]=0b0001000100000000000000000000000000000000 #enciende rojopeatonal y verdevehicular
    sleep(5)
    mem32[GPIO_SET]=0B0001000000000000000000000000000000000000 #inicia parpadeo de verdevehicular
    sleep(0.5)
    mem32[GPIO_SET]=0B0001000100000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B0001000000000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B0001000100000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B0001000000000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B0001100000000000000000000000000000000000 # amariilo y rojo peatonal
    sleep(2)
    mem32[GPIO_SET]=0B0001000000000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B1000010000000000000000000000000000000000 # se enciende rojovehicular y verdepeatonal
    sleep(5)
    mem32[GPIO_SET]=0B1000010000000000000000000000000000000000 #parpadeo verdepeatonal
    sleep(0.5)
    mem32[GPIO_SET]=0B0000010000000000000000000000000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B1000010000000000000000000000000000000000
    sleep(0.5)
    #mem32[GPIO_SET]=0B010000000010000 # se enciende verde peatonal (opcional)
    sleep(0.5)
    if variable==1:
        mem32[GPIO_SET]=0b10000000000100
        sleep(10)
        variable=0
   
        #sleep(0.5) #yo lo añadi
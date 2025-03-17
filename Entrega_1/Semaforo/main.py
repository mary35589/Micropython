from time import sleep
from machine import Pin
from machine import mem32

rojopeatonal=Pin(2,Pin.OUT)
verdepeatonal=Pin(4,Pin.OUT)
verdevehicular=Pin(13,Pin.OUT)
amarillovehicular=Pin(12,Pin.OUT)
rojovehicular=Pin(14,Pin.OUT)


global variable
variable=0

def interrupcion(Pin):
    global variable
    print("Entre a la función interrupción")
    variable=1

pulsador=Pin(23,Pin.IN)
pulsador.irq(trigger=Pin.IRQ_RISING,handler=interrupcion)

GPIO_SET=const(0x3FF44004)

while True:
    mem32[GPIO_SET]=0b010000000000100 #enciende rojopeatonal y verdevehicular
    sleep(5)
    mem32[GPIO_SET]=0B000000000000100 #inicia parpadeo de verdevehicular
    sleep(0.5)
    mem32[GPIO_SET]=0B010000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B000000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B010000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B000000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B001000000000100 # amariilo y rojo peatonal
    sleep(2)
    mem32[GPIO_SET]=0B000000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B100000000010000 # se enciende rojovehicular y verdepeatonal
    sleep(5)
    mem32[GPIO_SET]=0B100000000000000 #parpadeo verdepeatonal
    sleep(0.5)
    mem32[GPIO_SET]=0B100000000010000 
    sleep(0.5)
    mem32[GPIO_SET]=0B100000000000000 
    sleep(0.5)
    mem32[GPIO_SET]=0B010000000010000 # se enciende verde peatonal (opcional)
    sleep(0.5)
    if variable==1:
        mem32[GPIO_SET]=0b10000000000100
        sleep(10)
        variable=0
        #sleep(0.5) #yo lo añadi
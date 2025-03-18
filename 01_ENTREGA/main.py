from time import sleep
from machine import Pin
from machine import mem32

#Orden de los semaforos

#Semaroro_1: Semaforo especial
vv_especial= Pin(15, Pin.OUT)
av_especial= Pin(2, Pin.OUT)
rv_especial= Pin(0, Pin.OUT)

#Semaforo_5: semaforo_vehicular_01 y semaforo_peatonal_01
vv_01= Pin(4, Pin.OUT)
av_01= Pin(5, Pin.OUT)
rv_01= Pin(18, Pin.OUT)

vp_01= Pin(19, Pin.OUT)
rp_01= Pin(21, Pin.OUT)

#Semaforo_2: semaforo_vehicular_02 y semaforo_peatonal_02
vv_02= Pin(13, Pin.OUT)
av_02= Pin(12, Pin.OUT)
rv_02= Pin(14, Pin.OUT)

vp_02= Pin(22, Pin.OUT)
rp_02= Pin(23, Pin.OUT)

#Semaforo_4: semaforo_peatonal_04
vp_04= Pin(27, Pin.OUT)
rp_04= Pin(26, Pin.OUT)

#Semaforo_3: semaforo_vehicular_03 y semaforo_peatonal_03
vv_03= Pin(25, Pin.OUT)
av_03= Pin(33, Pin.OUT)
rv_03= Pin(32, Pin.OUT)

vp_03= Pin(35, Pin.OUT)
rp_03= Pin(34, Pin.OUT)


global variable
variable=0

def interrupcion(Pin):
    global variable
    print("Entre a la función interrupción")
    variable=1

pulsador=Pin(39,Pin.IN)
pulsador.irq(trigger=Pin.IRQ_RISING,handler=interrupcion)

GPIO_SET=const(0x3FF44004)

while True:
   #CICLO 1  LISTO
    mem32[GPIO_SET]=0b100100000100100011000010000000000100 #semaforo_2 en verde. 1,3,4 y 5 en rojo
    sleep(5)
    mem32[GPIO_SET]=0B000100000100100001000000000000000100 #inicia parpadeo vv
    sleep(0.5)
    mem32[GPIO_SET]=0B100100000100100011000010000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B000100000100100001000000000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B100100000100100011000010000000000100
    sleep(0.5)
    mem32[GPIO_SET]=0B000100000100100001000000000000000100
    sleep(0.5)  
    mem32[GPIO_SET]=0B010100000100101001000001000000000100 # amariilo y rojo peatonal
    sleep(2)
    mem32[GPIO_SET]=0B010100000100101001000000000000000100
    sleep(0.5)
   #CICLO 2 LISTO
    mem32[GPIO_SET]=0B010000001011011001001100000000000000 # se enciende rojovehicular y verdepeatonal
    sleep(5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000 #inicia parpadeo vv
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001011011001001100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001011011001001100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000
    sleep(0.5)  
    mem32[GPIO_SET]=0B011000001001111001001100000000000000 # amariilo y rojo peatonal
    sleep(2)
    mem32[GPIO_SET]=0B010100000100101001000000000000000100
    sleep(0.5)
    #CICLO 3 TERMINAR
   #mem32[GPIO_SET]=0b543210987654321098765432109876543210  
    mem32[GPIO_SET]=0B010000001011011001001100000000000000 # se enciende rojovehicular y verdepeatonal
    sleep(5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000 #inicia parpadeo vv
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001011011001001100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001011011001001100000000000000
    sleep(0.5)
    mem32[GPIO_SET]=0B010000001001001001000100000000000000
    sleep(0.5)  
    mem32[GPIO_SET]=0B011000001001111001001100000000000000 # amariilo y rojo peatonal
    sleep(2)
    mem32[GPIO_SET]=0B010100000100101001000000000000000100
    sleep(0.5)
    #mem32[GPIO_SET]=0B010000000010000 # se enciende verde peatonal (opcional)
    sleep(0.5)
    if variable==1:
        mem32[GPIO_SET]=0b10000000000100
        sleep(10)
        variable=0
        #sleep(0.5) #yo lo añadi
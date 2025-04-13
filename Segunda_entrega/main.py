from machine import Pin, Timer, TouchPad
from time import sleep

segmentos=[17,5,16,4,0,2,15]
pin_display1=Pin(18,Pin.OUT) #Pin del display 1
pin_display2=Pin(19,Pin.OUT) #Pin del display 2

for a in range(0,7):
    Pin(segmentos[a],Pin.OUT)
#display_2=[[a,b,c,d,e,f,g]
display_2=[[0,0,0,0,0,0,1], #0 DISPLAYS DE ANODO COMUN
          [1,0,0,1,1,1,1], #1
          [0,0,1,0,0,1,0], #2
          [0,0,0,0,1,1,0], #3
          [1,0,0,1,1,0,0], #4
          [0,1,0,0,1,0,0], #5
          [0,1,0,0,0,0,0], #6
          [0,0,0,1,1,1,1], #7
          [0,0,0,0,0,0,0], #8
          [0,0,0,0,1,0,0]] #9

temp_1 = Timer(0)
Touch1=TouchPad(Pin(12))
Touch2=TouchPad(Pin(14))

global contador
contador=79

print("inicio del programa")

def LLAMADO1(temp_1):
    global contador
    contador=contador-1
    if contador == 18:
        contador = 0  # Establecer contador a 0 cuando llegue a 30
        temp_1.deinit()
    print(contador)

valor=0

while True:
    start=Touch1.read()  
    #print(start)
    if start<300:
        temp_1.init(period=1000, mode=Timer.PERIODIC, callback=LLAMADO1)
    stop=Touch2.read()
    if stop<300:
        temp_1.deinit()

    unidades=contador%10
    decenas=int(contador/10)
    for i in range(0,7):
        Pin(segmentos[i], value=display_2[unidades][i])
        pin_display1.on()
        pin_display2.off()
    sleep(0.01)
    for i in range(0,7,):
        Pin(segmentos[i], value=display_2[decenas][i])
        pin_display1.off()
        pin_display2.on()
    sleep(0.01)
    
   
    
        
    #print(contador)
    




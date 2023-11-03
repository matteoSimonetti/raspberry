from gpiozero import LED       
from time import sleep          
                                
print("Inizializzazione Led")   
led = LED(26)                   

print("Inizio lampeggio Led")   
while True:                      
    print("Led Acceso")
    led.on()                   
    sleep(1)                
    print("Led Spento")
    led.off()                  
    sleep(1)                    
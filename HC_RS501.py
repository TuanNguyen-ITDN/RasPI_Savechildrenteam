  
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor         
GPIO.setup(3, GPIO.OUT)         #LED output pin
import SG90

def control():    
        i=GPIO.input(11)
        while True:
                if i==0:                 
                        print "No intruders",i
                        GPIO.output(3, 0)  #Turn OFF LED
                        time.sleep(0.1)
                        return 0
                       
                elif i==1:               #When output from motion sensor is HIGH
                            
                        print "Intruder detected",i
                        GPIO.output(3, 1)  #Turn ON LED
                        time.sleep(0.1)
                        return 1
                
def main():                
        control()                 

        while True:
                
                if control() == 0:
                        pass
                if control() == 1:
                        SG90.run()
                
                
                
                
               
        
                    
                    


        
     

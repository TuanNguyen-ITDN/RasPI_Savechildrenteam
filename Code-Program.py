import RPi.GPIO as GPIO
import time
import HC_RS501

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN)

i = GPIO.input(29)
while True:
        if i == 0:
                pass
        if i == 1:
                time.sleep(10)
                HC_RS501.main()
                time.sleep(60)
                break

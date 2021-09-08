import time
import grovepi

potentiometer = 2
led = 5

grovepi,pinMode(led, "OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        i = grovepi.analogRead(potentiometer)
        print(i)

        grovepi.analogWrite(led,i/4)
    except IOError:
        print("Error")
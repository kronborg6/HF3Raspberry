import time
import grovepi

potentiometer = 2
led = 5

grovepi.pinMode(led,"OUTPUT")
time.sleep(1)
i = 0

while True:
    try:
        i = grovepi.analogRead(potentiometer)
        print(i)
        if i > 100:
            grovepi.analogWrite(led, i / 4)

        grovepi.analogWrite(led,0)
    except IOError:
        print("Error")
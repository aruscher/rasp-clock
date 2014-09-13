import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import threading
import os
#Sound + on port 8 

class Sound_Handler(threading.Thread):

    def __init__(self,begin,rest):
        threading.Thread.__init__(self)
        self.begin = begin
        self.beeper_port = 8
        self.setup()
        self.rest = rest
        print(rest)
        self.STOP = False
     

    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.beeper_port, GPIO.OUT)


    def run(self):
        start = datetime.now() 
        now = datetime.now() 
        delta = now-start
        self.STOP = False
        while ((now-self.begin).seconds <= self.rest) and not self.STOP:
            if delta.seconds >=1:
                print("Beep")
                GPIO.output(self.beeper_port,True)
                start = now
                if (now-self.begin).seconds <= self.rest-1:
                    os.system("aplay /home/pi/rasp-clock/match0.wav")
                if (now-self.begin).seconds >= self.rest:
                    os.system("aplay /home/pi/rasp-clock/match1.wav")
                    GPIO.output(self.beeper_port,False)
                GPIO.output(self.beeper_port,False)
                print("BOOp")
            else:
                now = datetime.now()
            delta = now-start

    def stop(self):
        self.STOP = True

    def play(self):
        os.system("aplay /home/pi/rasp-clock/match1.wav")

        



import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import threading
import os
#Sound + on port 8 

class Sound_Handler(threading.Thread):

    def __init__(self,begin):
        threading.Thread.__init__(self)
        self.begin = begin
        self.beeper_port = 8
        self.setup()
        self.STOP = False
     

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.beeper_port, GPIO.OUT)


    def run(self):
        start = datetime.now() 
        now = datetime.now() 
        delta = now-start
        self.STOP = False
        while ((now-self.begin).seconds <10) and not self.STOP:
            if delta.seconds >=1:
                GPIO.output(self.beeper_port,True)
                os.system("aplay /home/pi/rasp-clock/match0.wav")
                start = now
                GPIO.output(self.beeper_port,False)
                if (now-self.begin).seconds >= 10:
                    return 
            else:
                now = datetime.now()
            delta = now-start

    def stop(self):
        self.STOP = True

        



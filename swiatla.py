import RPi.GPIO as IO
from time import sleep

class swiatla():
    def __init__(self, R, G, B):
        print("Klasa init od światel")
        self.R = R
        self.G = G
        self.B = B
        IO.setup(self.R, IO.OUT)
        IO.setup(self.G, IO.OUT)
        IO.setup(self.B, IO.OUT)
        self.pwmR = IO.PWM(self.R,100)
        self.pwmR.start(0)
        self.pwmG = IO.PWM(self.G,100)
        self.pwmG.start(0)
        self.pwmB = IO.PWM(self.B,100)
        self.pwmB.start(0)
        
    def CzerwonyOn(self):
        print("Czerwony ON")
        self.pwmR.ChangeDutyCycle(100)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        
    def ZielonyOn(self):
        print("zielony On")
        self.pwmR.ChangeDutyCycle(0)
        self.pwmG.ChangeDutyCycle(100)
        self.pwmB.ChangeDutyCycle(0)
        
    def AllOff(self):
        print("AllOff")
        self.pwmR.ChangeDutyCycle(0)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
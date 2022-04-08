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
        self.pwmR = IO.PWM(self.R,4)
        self.pwmR.start(0)
        self.pwmG = IO.PWM(self.G,4)
        self.pwmG.start(0)
        self.pwmB = IO.PWM(self.B,4)
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

    def NiebieskiOn(self):
        print("zielony On")
        self.pwmR.ChangeDutyCycle(0)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(100)

    def WhiteOn(self):
        self.pwmR.ChangeDutyCycle(100)
        self.pwmG.ChangeDutyCycle(100)
        self.pwmB.ChangeDutyCycle(100)

    def OrangeBlink(self):
        self.pwmR.ChangeDutyCycle(50)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(50)

    def AllOff(self):
        #print("AllOff")
        self.pwmR.ChangeDutyCycle(0)
        self.pwmG.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
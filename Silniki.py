import RPi.GPIO as IO
from time import sleep

class silnik():
    def __init__(self,WlaczA,Wyjscie1A,Wyjscie2A, WlaczB,Wyjscie1B,Wyjscie2B):
        self WlaczA = WlaczA
        self WlaczB = WlaczB
        self Wyjscie1A = Wyjscie1A
        self Wyjscie1B = Wyjscie1B
        self Wyjscie2A = Wyjscie2A
        self Wyjscie2B = Wyjscie2B 
        IO.setup(self.WlaczA,IO.OUT)
        IO.setup(self.Wyjscie1A,IO.OUT)
        IO.setup(self.Wyjscie2A,IO.OUT)
        IO.setup(self.WlaczB,IO.OUT)
        IO.setup(self.Wyjscie1B,IO.OUT)
        IO.setup(self.Wyjscie2B,IO.OUT)
        self.pwmA = IO.PWM(self.WlaczA,100)
        self.pwmA.start(0)
        self.pwmB = IO.PWM(self.WlaczB,100)
        self.pwmB.start(0)
        
    def Ruch(self, predkosc=0.5, skret=0, czas=0):
        predkosc *= 100
        skret *= 100
        predkoscLewego = predkosc - skret
        predkoscPrawego = predkosc + skret
        
        if predkoscLewego > 100: predkoscLewego=100
        elif predkoscLewego <-100: predkoscLewego=-100
        if predkoscPrawego > 100: predkoscPrawego=100
        elif predkoscPrawego <-100: predkoscPrawego=-100
        
        self.pwmA.ChangeDutyCycle(abs(predkoscLewego))
        self.pwmB.ChangeDutycycle(abs(predkoscPrawego))
        
        if predkoscLewego > 0: IO.output(self.Wyjscie1A,IO.HIGH); IO.output(self.Wyjscie2A,IO.LOW)
        else: IO.output(self.Wyjscie1A,IO.LOW); IO.output(self.Wyjscie2A,IO.HIGH)
        if predkoscPrawego >0: IO.output(self.Wyjscie1B,IO.HIGH); IO.output(self.Wyjscie2B,IO.LOW)
        else: IO.output(self.Wyjscie1B,IO.LOW); IO.output(self.Wyjscie2B,IO.HIGH)
        
    def doPrzodu(self,Wypelnienie=50,Czas=0):
        IO.output(self.Wyjscie1,IO.HIGH)
        IO.output(self.Wyjscie2,IO.LOW)
        self.pwm.ChangeDutyCycle(Wypelnienie)
        sleep(Czas)
    def doTylu(self,Wypelnienie=50,Czas=0):
        IO.output(self.Wyjscie1,IO.LOW)
        IO.output(self.Wyjscie2,IO.HIGH)
        self.pwm.ChangeDutyCycle(Wypelnienie)
        sleep(Czas)
    def stop(self,Czas=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(Czas)
        
LewyPrzod = silnik(2,3,4)
PrawyPrzod = silnik(17,22,25)

while True:
    LewyPrzod.doPrzodu(30,2)
    LewyPrzod.stop(2)
    LewyPrzod.doTylu(100,2)
    LewyPrzod.stop(2)
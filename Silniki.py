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
        

class silnik():
    def __init__(self,WlaczA,Wyjscie1A,Wyjscie2A, WlaczB,Wyjscie1B,Wyjscie2B):
        print("Init silnika")
        self.WlaczA = WlaczA
        self.WlaczB = WlaczB
        self.Wyjscie1A = Wyjscie1A
        self.Wyjscie1B = Wyjscie1B
        self.Wyjscie2A = Wyjscie2A
        self.Wyjscie2B = Wyjscie2B
        IO.setmode(IO.BCM)
        IO.setup(self.WlaczA,IO.OUT)
        IO.setup(self.Wyjscie1A,IO.OUT)
        IO.setup(self.Wyjscie2A,IO.OUT)
        IO.setup(self.WlaczB,IO.OUT)
        IO.setup(self.Wyjscie1B,IO.OUT)
        IO.setup(self.Wyjscie2B,IO.OUT)
        print("start PWMA")
        self.pwmA = IO.PWM(self.WlaczA,50)
        self.pwmA.start(0)
        print("start PWMB")
        self.pwmB = IO.PWM(self.WlaczB,50)
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
        self.pwmB.ChangeDutyCycle(abs(predkoscPrawego))
        print("Prędkość Lewego:"+str(predkoscLewego))
        print("Prędkość Prawego:"+str(predkoscPrawego))
        sleep(czas)
        
        if predkoscLewego > 0: IO.output(self.Wyjscie1A,IO.HIGH); IO.output(self.Wyjscie2A,IO.LOW)
        else: IO.output(self.Wyjscie1A,IO.LOW); IO.output(self.Wyjscie2A,IO.HIGH)
        if predkoscPrawego >0: IO.output(self.Wyjscie1B,IO.HIGH); IO.output(self.Wyjscie2B,IO.LOW)
        else: IO.output(self.Wyjscie1B,IO.LOW); IO.output(self.Wyjscie2B,IO.HIGH)
        
    def doPrzodu(self,Wypelnienie=50,Czas=0):
        IO.output(self.Wyjscie1B,IO.HIGH)
        IO.output(self.Wyjscie2B,IO.LOW)
        self.pwmB.ChangeDutyCycle(Wypelnienie)
        sleep(Czas)
    def doTylu(self,Wypelnienie=50,Czas=0):
        IO.output(self.Wyjscie1B,IO.LOW)
        IO.output(self.Wyjscie2B,IO.HIGH)
        self.pwmB.ChangeDutyCycle(Wypelnienie)
        sleep(Czas)
    def stop(self,Czas=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)
        sleep(Czas)
print("Inicjacja silnika")        
LewyPrzod = silnik(23,24,25,22,17,27)
print("Inicjacja lamp")
lamps = swiatla(26,19,13)

try:
    while True:
        lamps.CzerwonyOn()
        #LewyPrzod.doPrzodu(50,2)
        LewyPrzod.Ruch(0.6,0.2,2)
        lamps.AllOff()
        LewyPrzod.stop(2)
        lamps.ZielonyOn()
        #LewyPrzod.doTylu(50,2)
        LewyPrzod.Ruch(-0.6,-0.2,2)
        lamps.AllOff()
        LewyPrzod.stop(2)
    
except KeyboardInterrupt:
    LewyPrzod.stop()
    lamps.AllOff()
    IO.cleanup()
    
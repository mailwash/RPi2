import RPi.GPIO as IO
from time import sleep

class silnik():
    def __init__(self,Wlacz,Wyjscie1,Wyjscie2):
        self Wlacz = Wlacz
        self Wyjscie1 = Wyjscie1
        self Wyjscie2 = Wyjscie2
        IO.setup(self.Wlacz,IO.OUT)
        IO.setup(self.Wyjscie1,IO.OUT)
        IO.setup(self.Wyjscie2,IO.OUT)
        self.pwm = IO.pwm(self.Wyjscie,100)
        self.pwm.start(0)
        
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
        self.pwm.ChangeDutyCycle(0)
        sleep(Czas)
        
LewyPrzod = silnik(2,3,4)
PrawyPrzod = silnik(17,22,25)

while True:
    LewyPrzod.doPrzodu(30,2)
    LewyPrzod.stop(2)
    LewyPrzod.doTylu(100,2)
    LewyPrzod.stop(2)
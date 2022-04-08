import RPi.GPIO as IO
import cv2
import mediapipe as mp
import time
import math
from cameraModule import WykrywanieReki
from swiatla import swiatla
from keyboard import Klawiatura
import pygame
from Silniki import silnik

print("Inicjalizacja....")
cam = cv2.VideoCapture(0)
sukces, img = cam.read()
wykrywacz = WykrywanieReki(img,False)
motor = silnik(23,24,25,22,17,27)
lamps = swiatla(13,19,26)
print("Start")
try:
    #klaw = Klawiatura()
    kierunek = 'stop'
    while True:
        sukces, img = cam.read()
        img = wykrywacz.znajdzDlon(img)
        listaWynikow = wykrywacz.ZnajdzPozycje(img,False)

        # print(listaWynikow)
        if len(listaWynikow) != 0:
            id1, x1, y1 = listaWynikow[5]
            id2, x2, y2 = listaWynikow[17]
            #print("x1-x2: " + str(abs(x1-x2)) + " y1-y2: " + str(abs(y1-y2)))
            odleglosc = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            cv2.putText(img, str(int(abs(x1-x2))) + " " + str(int(abs(y1-y2))),(10,70),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),3)
            cv2.putText(img, str(odleglosc), (10,150), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            img, sterowanieX = wykrywacz.Koordynaty(img, listaWynikow[9])
            if sterowanieX > 120:
                skret = 0.25
            elif sterowanieX > 50:
                skret = 0.15
            elif sterowanieX < -50:
                skret = -0.15
            elif sterowanieX < -120:
                skret = -0.25
            else:
                skret = 0
            cv2.putText(img, "skret" + str(skret), (10,250), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
            if odleglosc > 100:
                lamps.CzerwonyOn()
                motor.Ruch(0.4,skret,0.1)
                #motor.stop(0.01)
            elif odleglosc < 70:
                lamps.ZielonyOn()
                motor.Ruch(-0.4,skret,0.1)
                #motor.stop(0.01)
            else:
                lamps.NiebieskiOn()
                motor.stop()
        else:
            lamps.AllOff()
            motor.stop()

        img = wykrywacz.RysujWskazniki(img)
        cv2.imshow("Zdjecie",img)
        cv2.waitKey(2)


        #klawisz = klaw.KeyLatch()




finally:
    #del klaw
    motor.stop()
    lamps.AllOff()
    IO.cleanup()
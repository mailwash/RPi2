import cv2
import mediapipe as mp
import time
import math

class WykrywanieReki():
    def __init__(self, img, tryb = False, liczbaDloni = 1, progWykrycia=0.5, progSledzenia=0.5):
        self.tryb = tryb
        self.liczbaDloni = liczbaDloni
        self.progWykrycia = progWykrycia
        self.progSledzenia = progSledzenia
        self.dlonie = mp.solutions.hands
        self.dlon = self.dlonie.Hands(self.tryb, self.liczbaDloni, self.progWykrycia, self.progSledzenia)
        self.rys = mp.solutions.drawing_utils
        self.s,self.w,self.c = img.shape #szerkość/ wysokość / liczba kanałów - kolory

    def znajdzDlon(self, img, rysuj=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.wyniki = self.dlon.process(imgRGB)
        #print(self.wyniki.multi_hand_landmarks)
        if self.wyniki.multi_hand_landmarks:
            if rysuj:
                self.rys.draw_landmarks(img, self.wyniki.multi_hand_landmarks[0], self.dlonie.HAND_CONNECTIONS)

        return img

    def ZnajdzPozycje(self, img, rysuj=True):
        listaPunktow=[]
        if self.wyniki.multi_hand_landmarks:    #wykonuje się tylko jeżeli zostaną wykryte jakies punkty.
            for id, punkt in enumerate(self.wyniki.multi_hand_landmarks[0].landmark):
                cx, cy = int(punkt.x*self.w), int(punkt.y*self.s) #kordynaty punktu na obrazku w pikselach
                listaPunktow.append([id,cx,cy])
                if rysuj:
                    cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),1)

        return listaPunktow

    def RysujWskazniki(self, img):
        cv2.line(img, (int(self.w/2),0),(int(self.w/2),self.s),(255,0,0),1)
        cv2.line(img, (0,int(self.s/2)),(self.w,int(self.s/2)),(255,0,0),1)

        return img

    def Koordynaty(self,img, punkt):
        idp, kx, ky = punkt
        x = int(self.w/2)-kx
        cv2.putText(img,str(int(self.w/2)),(int(self.w/2),10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),1)
        cv2.putText(img,str(x),(10,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

        return img, x

def main():
    cam = cv2.VideoCapture(0)
    success, img = cam.read()
    wykrywacz = WykrywanieReki(img,False)
    while True:
        success, img = cam.read()
        img = wykrywacz.znajdzDlon(img)
        listaWynikow = wykrywacz.ZnajdzPozycje(img,False)

        # print(listaWynikow)
        if len(listaWynikow) != 0:
            id1, x1, y1 = listaWynikow[5]
            id2, x2, y2 = listaWynikow[17]
            print("x1-x2: " + str(abs(x1-x2)) + " y1-y2: " + str(abs(y1-y2)))
            odleglosc = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            cv2.putText(img, str(int(abs(x1-x2))) + " " + str(int(abs(y1-y2))),(10,70),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),3)
            cv2.putText(img, str(odleglosc), (10,100), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            img, sterowanieX = wykrywacz.Koordynaty(img, listaWynikow[9])

        img = wykrywacz.RysujWskazniki(img)
        cv2.imshow("Zdjecie",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
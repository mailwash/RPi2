import cv2
import mediapipe as mp
import time

class WykrywanieReki():
    def __init__(self, tryb = False, liczbaDloni = 1, progWykrycia=0.5, progSledzenia=0.5):
        self.tryb = tryb
        self.liczbaDloni = liczbaDloni
        self.progWykrycia = progWykrycia
        self.progSledzenia = progSledzenia

        self.dlonie = mp.solutions.hands
        self.dlon = self.dlonie.Hands(self.tryb, self.liczbaDloni, self.progWykrycia, self.progSledzenia)
        self.rys = mp.solutions.drawing_utils

    def znajdzDlon(self, img, rysuj=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.wyniki = self.dlon.process(imgRGB)
        #print(self.wyniki.multi_hand_landmarks)

        if self.wyniki.multi_hand_landmarks:
            #for wykrytaDlon in self.wyniki.multi_hand_landmarks:
#
#                         cv2.circle(img, (cx,cy), 25, (140,140,0), cv2.FILLED)
            if rysuj:
                self.rys.draw_landmarks(img, self.wyniki.multi_hand_landmarks[0], self.dlonie.HAND_CONNECTIONS)
        return img

    def ZnajdzPozycje(self, img, draw=True):
        listaPunktow=[]
        if self.wyniki.multi_hand_landmarks:


            for id, punkt in enumerate(self.wyniki.multi_hand_landmarks[0].landmark):
    #             print(id,punkt)
                w,s,g = img.shape
                cx, cy = int(punkt.x*s), int(punkt.y*w) #central place
                #print('id: ' + str(id) + ' CX = '+str(cx)+' CY = '+str(cy))
                listaPunktow.append([id,cx,cy])
                cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(255,200,0),1)
        return listaPunktow

    #cTime = time.time()
    #fps = 1/(cTime-pTime)
    #pTime = cTime

    #cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),3)
#     cv2.imshow("Zdjecie",img)
#     cv2.waitKey(1)

def main():
    pTime = 0
    cTime = 0
    cam = cv2.VideoCapture(0)
    wykrywacz = WykrywanieReki()
    while True:
        success, img = cam.read()
        img = wykrywacz.znajdzDlon(img)
        listaWynikow = wykrywacz.ZnajdzPozycje(img)

        # print(listaWynikow)
        if len(listaWynikow) != 0:
            id1, x1, y1 = listaWynikow[5]
            id2, x2, y2 = listaWynikow[17]
            print("x1-x2: " + str(abs(x1-x2)) + " y1-y2: " + str(abs(y1-y2)))
        #     for i in range(len(listaWynikow)):
        #         print(listaWynikow[i])
        #cTime = time.time()
        #fps = 1/(cTime-pTime)
        #pTime = cTime

        #cv2.putText(img, str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),3)
        cv2.imshow("Zdjecie",img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
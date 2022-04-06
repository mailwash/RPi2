import pygame

class Sterowanie():
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((200,200))
        
    def SprawdzKlawisz(self, klawisz):
        byl = False
        for event in pygame.event.get():pass
        keyInput = pygame.key.get_pressed()
        mojKlawisz = getattr(pygame,'K_{}'.format(klawisz))
        if keyInput [mojKlawisz]:
            byl = True
        pygame.display.update()
        
        return byl

try:
    klaw = Sterowanie()
    LC = 0
    RC = 0
    flagaWyjscia = True
    while flagaWyjscia:
        if klaw.SprawdzKlawisz('LEFT'):
            LC += 1
            print('Wcisnieta strzałka w lewo ' + str(LC) + ' razy')
        if klaw.SprawdzKlawisz('RIGHT'):
            RC += 1
            print('Wcisnieta strzałka w prawo ' + str(RC) + ' razy')
        if klaw.SprawdzKlawisz('q'):
            print('Zamknij apke')
            flagaWyjscia=False
            
finally:
    pygame.quit()
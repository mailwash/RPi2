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
        if klawisz [mojKlawisz]:
            byl = True
        pygame.display.update()
        
        return byl

try:
    klaw = Sterowanie()
    while True:
        if klaw.SprawdzKlawisz('LEFT'):
            print('Wcisnieta strzałka w lewo')
        if klaw.SprawdzKlawisz('RIGHT'):
            print('Wcisnieta strzałka w prawo')
            
finally:
    
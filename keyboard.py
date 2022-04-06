import pygame
      
class Klawiatura():
    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((200,200))
    
    def __del__(self):
        print('quit pygame')
        pygame.quit()
    
    def sprawdzKlawisz(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))
                if event.key == pygame.K_q:
                    print('q pressed')
                    return 'q'
                if event.key == pygame.K_LEFT:
                    print('L arrow pressed ')
                    return 'LEFT'
                if event.key == pygame.K_RIGHT:
                    print('R arrow pressed')
                    return 'RIGHT'
                if event.key == pygame.K_UP:
                    print('U arrow pressed')
                    return 'UP'
                if event.key == pygame.K_DOWN:
                    print('D arrow pressed')
                    return 'DOWN'
    def KeyLatch(self):
        key = self.sprawdzKlawisz()
        if key == 'LEFT' or 'RIGHT' or 'UP' or 'DOWN' or 'q':
            latched = key    
        return latched
# try:
#     klaw = Klawiatura()
#     LC = 0
#     RC = 0
#     flagaWyjscia = True
#     while flagaWyjscia:
#         klawisz = klaw.sprawdzKlawisz()
#         if klawisz == 'LEFT':
#             LC += 1
#             print('Wcisnieta strzałka w lewo ' + str(LC) + ' razy')
# #         if klaw.SprawdzKlawisz('RIGHT'):
# #             RC += 1
# #             print('Wcisnieta strzałka w prawo ' + str(RC) + ' razy')
#         if klawisz == 'q':
#             print('Zamknij apke')
#             flagaWyjscia=False

# the error_check 1.0 system  is a very shitty way to check if somthing is wrong
import time
import pygame
# 0 = success 1 = fail
# THIS IS A SCRIPT
errorCHECK = int(input('is somthing wrong? For yes type 1, For No type 0:'))
if errorCHECK == 1:
    print("1 FOUND SOMETHING IS WRONG")
if errorCHECK == 0:
    print("0 CODE SUCCESS NOTHING IS WRONG")
if errorCHECK != 1 and errorCHECK != 0:
    # HALF LIFE GORDON FREEEEMON
    for count in range(10):
        pygame.init()
        pygame.mixer.music.load("half life explode 2.wav")
        pygame.mixer.music.play()
        time.sleep(0.50)
        pygame.mixer.music.load("half life explode 1.wav")
        pygame.mixer.music.play()
        time.sleep(0.50)
        pygame.mixer.music.load("half life explode 3.wav")
        pygame.mixer.music.play()
        time.sleep(0.50)
    print("SYSTEM OVERLOAD ANSWERS NOT HELPING.")
    print("PLEASE WAIT FOR SYSTEM REPAIR UNIT TO RESPOND")
    time.sleep(20)
    print("S.R.U: expected actual answers instead got ", errorCHECK, " Next time Input 1 or 0. THANK YOU")
    # I made this entire shit for a goof, so I made a more very nice way of saying Hey dumb ass put an actual answer
# 6A-61-79-20-62-65-61-6E this is nothing :>

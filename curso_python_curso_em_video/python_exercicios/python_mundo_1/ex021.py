# Ex021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# [Exemplo] QUANDO O PROGRAMA FOR EXECUTADO A MÚSICA INFORMADA COMEÇARÁ A TOCAR

<<<<<<< Updated upstream
import pygame
=======
from pygame import init, mixer, event
mixer.init()
init()
mixer.music.load('ex021.mp3')
mixer.music.play()
event.wait()
'''import pygame
>>>>>>> Stashed changes
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(-1)#Colocando o valor -1 ficará em looping infinito
pygame.event.wait()

'''import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(-1)#Colocando o valor -1 ficará em looping infinito
input()
pygame.event.wait()'''
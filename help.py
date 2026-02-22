import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("sejaex.mp3") # usei essa musica pq oq o python ta fazendo na minha vida é putaria
pygame.mixer.music.play()
while pygame.mixer.music.get_busy(): time.sleep(1)
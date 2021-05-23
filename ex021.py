# Tocando MP3
import pygame

# Procurar outro modulo mais recente!
pygame.init()
pygame.mixer.music.load('ex-021.wav')
pygame.mixer.music.play()
pygame.event.wait()
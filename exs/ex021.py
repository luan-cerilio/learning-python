import pygame
print('Olá! Vamos escutar uma música! :)')
pygame.init()
pygame.mixer.music.load('exs/ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
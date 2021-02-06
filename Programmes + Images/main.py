
import pygame
import time
from tkinter import *

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE) #Définition de la Surface qu'on va manipuler
white_color = (255, 255, 255)

helvetica = pygame.font.Font("Helvetica.ttf", 32)
text_helvetica = helvetica.render("{}".format(window_surface), True, white_color)
window_surface.blit(text_helvetica, (10, 10))

pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched = False
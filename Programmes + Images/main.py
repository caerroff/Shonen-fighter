
import pygame
import time
from tkinter import *

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)

pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution) #Définition de la Surface qu'on va manipule

arial_font = pygame.font.SysFont("arial", 22)

pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched = False
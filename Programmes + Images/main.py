
import pygame
import time
from tkinter import *

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
blank = (255, 255, 255)
black = (0, 0, 0)

pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution) #Définition de la Surface qu'on va manipule

arial_font = pygame.font.SysFont("arial", 32)
hello_text_surface = arial_font.render(" 0.80 € La Chocolatine", True, blank)  # Renvoie une surface
window_surface.blit(hello_text_surface, (10, 10))
pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched = False
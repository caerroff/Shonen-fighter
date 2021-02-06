
import pygame
import time
from tkinter import *

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
blank = (255, 255, 255)
black = (0, 0, 0)

pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution) #Définition de la Surface qu'on va manipule

helvetica_font = pygame.font.Font("Helvetica.ttf", 32) #Arguments : La police (téléchargée), Taille de la police
helvetica_text = helvetica_font.render("Bonsoir les zamis", True, blank) #Args : Text, Anti-aliasing (Bool), Color
window_surface.blit(helvetica_text, (10, 10)) #Affiche la surface ; Args : Surface (Text), Coords(x, y)
pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched = False
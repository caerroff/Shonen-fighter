
import pygame
import time

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
black_color = (0, 0, 0)
red_color = (255, 0, 0)
i = 0

pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution) #Définition de la Surface qu'on va manipuler

myrect = pygame.Rect(10, 10, 250, 80)
pygame.draw.rect(window_surface, red_color, myrect)
pygame.display.flip()

while i < 100:
    time.sleep(.050)
    window_surface.fill(black_color)
    myrect.x += 1
    myrect.y += 1
    pygame.draw.rect(window_surface, red_color, myrect)
    pygame.display.flip()
    i += 1

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched= False

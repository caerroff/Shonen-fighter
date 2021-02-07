from typing import Tuple

import pygame
import time

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE) #Définition de la Surface qu'on va manipuler
white_color = (255, 255, 255)
black_color = (0, 0, 0)
green_color = (0, 255, 0)
red_color = (255, 0, 0)
blue_color = (0, 0, 255)
colorDef = (255, 255, 255)

helvetica = pygame.font.Font("Helvetica.ttf", 32)
text_helvetica = helvetica.render("{}".format(window_surface), True, white_color)
window_surface.blit(text_helvetica, (10, 10))

monRect = pygame.Rect(10, 100, 100, 50)
pygame.draw.rect(window_surface, colorDef, monRect)

liste = [red_color, green_color, blue_color]
i = True

pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Haut")
                window_surface.fill(black_color)
                monRect.y += -5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_DOWN:
                print("Bas")
                window_surface.fill(black_color)
                monRect.y += 5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_LEFT:
                print("Gauche")
                window_surface.fill(black_color)
                monRect.x += -5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_RIGHT:
                print("Droit")
                window_surface.fill(black_color)
                monRect.x += 5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_RETURN:
                launched = False
            elif event.key == pygame.K_1:
                print("Green")
                colorDef = green_color
                window_surface.fill(black_color)
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_2:
                print("Red")
                colorDef = red_color
                window_surface.fill(black_color)
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_3:
                print("Blue")
                colorDef = blue_color
                window_surface.fill(black_color)
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_5:
                print("YOLOOOOOOOOOOOOOOOOOOOO")
                for c in liste:
                    time.sleep(1)
                    colorDef = c
                    window_surface.fill(black_color)
                    pygame.draw.rect(window_surface, colorDef, monRect)
                    pygame.display.flip()
            else:
                print("Autre Touche")
#coding:utf-8
import pygame

window_resolution = (640, 480)

pygame.init()
pygame.display.set_caption("python #40")
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Haut")
            elif event.key == pygame.K_DOWN:
                print("Bas")
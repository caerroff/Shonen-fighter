#coding:utf-8
import pygame

pygame.init()
window_resolution = (640,480)

pygame.display.set_caption("python #40")
window_surface = pygame.display.set_mode(window_resolution)
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
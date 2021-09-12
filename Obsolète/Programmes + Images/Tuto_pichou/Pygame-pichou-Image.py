#coding:utf-8
import pygame

pygame.init()
window_resolution = (1000,600)

pygame.display.set_caption("python #37")
window_surface = pygame.display.set_mode(window_resolution)

naruto_bg = pygame.image.load("naruto_bg.png")
naruto_bg.convert() #optimise l'image pour pygame

launched = True
while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False

        window_surface.blit(naruto_bg, [10,10]) #blit superpose naruto_bg sur window surface
        pygame.display.flip()
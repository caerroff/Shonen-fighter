#coding:utf-8
import pygame

pygame.init() #initialisation de pygame

window_resolution = (640, 480) #resolution
blue_color = (89, 152, 255)
black_color = (0, 0, 0)


pygame.display.set_caption("First Surface") #Nom de la surface
window_surface = pygame.display.set_mode(window_resolution) #cretion de la surface et de ses parametres
window_surface.fill(blue_color)

pygame.draw.line(window_surface, black_color, [10,40], [100,100], 5)
rect_form = pygame.Rect(10, 10, 150, 65)
pygame.draw.rect(window_surface, black_color, rect_form, 5)
circle_center = (150,250)
pygame.draw.circle(window_surface, black_color, circle_center, 50, 35)
coords = [(300,4), (200,5), (600,100)]
pygame.draw.polygon(window_surface, black_color, coords)

pygame.display.flip()

launched = True

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

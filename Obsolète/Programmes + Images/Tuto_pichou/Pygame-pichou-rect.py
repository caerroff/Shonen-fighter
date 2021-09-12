#coding:utf-8
import pygame
import time

pygame.init()
window_resolution = (640,480)
blue = (0, 0, 255)
black = (0, 0, 0)
i = 0

pygame.display.set_caption("python #38)
window_surface = pygame.display.set_mode(window_resolution)

myrect = pygame.Rect(10, 10, 250, 80)
pygame.draw.rect(window_surface, blue, myrect)

pygame.display.flip()

while i < 25:
    time.sleep(.050)
    window_surface.fill(black)
    myrect.x += 10
    myrect.y += 10
    pygame.draw.rect(window_surface, blue, myrect)
    pygame.display.flip()
    i += 1

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
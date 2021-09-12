#coding:utf-8
import pygame

pygame.init()
window_resolution = (640,480)

pygame.display.set_caption("python #39")
window_surface = pygame.display.set_mode(window_resolution)
pygame.display.flip()

arial_font = pygame.font.SysFont("arial", 20)
hello_text = arial_font.render("Hello world!", False)

print(pygame.font.get_fonts())

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
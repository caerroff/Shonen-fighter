import pygame

pygame.init()

main = pygame.display.set_mode((300, 200))

image = pygame.image.load("logo.png").convert()
pygame.display.set_icon(image)

pygame.display.flip()

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()

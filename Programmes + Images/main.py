
import pygame, time

window_resolution = (640, 480)
blue_color = (132, 180, 255)
red_color = (255, 0, 0)
launched = True

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Yes Man On Fait Du Pygame")
window_surface = pygame.display.set_mode(window_resolution)
helevetica_font = pygame.font.Font("Helvetica.ttf", 36)
text = helevetica_font.render("On dit Chocolatine !", True, blue_color)
window_surface.blit(text, [50, 50]) #Affichage du texte --> Texte, Coordonnées (Tuple)
pygame.display.flip()

pygame.time.delay(5000)

text = helevetica_font.render("On dit Chocolatine !", True, red_color)
window_surface.blit(text, [50, 50]) #Affichage du texte --> Texte, Coordonnées (Tuple)
pygame.display.flip()

while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    clock.tick()
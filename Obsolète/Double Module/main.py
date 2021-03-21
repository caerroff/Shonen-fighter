
import pygame, time

window_resolution = (640, 480)
blue_color = (132, 180, 255)
red_color = (255, 0, 0)
black_color = (0, 0, 0)
blank_color = (255, 255, 255)
launched = True

pygame.init()

clock = pygame.time.Clock() #Récupère dans une variable (clock) un objet de temps --> Manipulable avec les méthodes

pygame.time.set_timer(pygame.USEREVENT, 2000) #Définit un Timer, 2000 --> 2 Secondes (2000 Millisecondes)

pygame.display.set_caption("Yes Man On Fait Du Pygame")
window_surface = pygame.display.set_mode(window_resolution)
helevetica_font = pygame.font.Font("Helvetica.ttf", 36)
text = helevetica_font.render("Je suis une licorne ! (Cé fo)", True, blue_color)
window_surface.blit(text, [50, 50]) #Affichage du texte --> Texte, Coordonnées (Tuple)
pygame.display.flip()

while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            launched = False
        elif event.type == pygame.USEREVENT: #Après le timer, on met à jour l'affichage des fps
            window_surface.fill(black_color)  # On affiche à l'écran (blit) le nombre de fps (get_fps)
            clockText = helevetica_font.render(f"{clock.get_fps():.2f} FPS", True, blank_color)  #:.2f --> 2 Décimales
            window_surface.blit(clockText, [75, 75])
            pygame.display.flip()


    clock.tick(60) #60 Fps (Taux de raffraichissement), Setup le nombre de raffraichissement



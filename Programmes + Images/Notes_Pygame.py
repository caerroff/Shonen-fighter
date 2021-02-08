
import pygame

"""Surface, Rect
Rect(left, right, width, height) --> Décalage en x par rapport à la surface, Idem en Y, Largeur, Hauteur
pygame.Rect(x, y, width, height)
mynewrect = myrect.copy() -> Rect (Nouveau Rectangle, copie)
Rect.move() | Rect.move_ip()s
/// Font
arial_font.set_bold() --> Gras
arial_font.set_italic() --> Italique
arial_font.set_underline() --> Sous-ligner
"""

pygame.init()

window_resolution = (640, 480) #Resolution de la fenêtre (Window)
blue_color = (89, 152, 255) #Création d'une couleur, utilisé comme background
black_color = (0, 0, 0)
blank_color = (255, 255, 255)

pygame.display.set_caption("My Game") #Titre de la fenêtre

window_surface = pygame.display.set_mode(window_resolution) #Définition de la Surface qu'on va manipuler
window_surface.fill(blue_color) #Fill = Remplissage de la fenêtre, couleur donnée en argument

rect_form = pygame.Rect(10, 10, 150, 65) #Constructeur d'objet --> Rectangle, Arg: x, y, w, h
pygame.draw.rect(window_surface, black_color, rect_form) #Surface, Couleur (Bg), Rectangle, Remplissage-Optionnel

coords = [(10, 10), (100, 10), (10, 50), (100, 50)] #Coordonnées polygone, ensemble de tuple, chaque tuple = 1 pt
pygame.draw.polygon(window_surface, black_color, coords)

logo_image = pygame.image.load("uchiha_2.png") #Retourne une Surface
logo_image.convert() #Converti l'image au bon format, convert_alpha si image transparente
#logo_image.set_colorkey(blank_color) #Transparence d'une couleur sur une image non png

""" Boucle permettant de déplacer un rectangle
while i < 100:
    time.sleep(.050)
    window_surface.fill(black_color)
    myrect.x += 1
    myrect.y += 1
    pygame.draw.rect(window_surface, red_color, myrect)
    pygame.display.flip()
    i += 1
"""

arial_font = pygame.font.SysFont("arial", 32) #Afficher du texte avec police système --> Arial
hello_text_surface = arial_font.render(" 0.80 € La Chocolatine", True, blank)  # Renvoie une surface
window_surface.blit(hello_text_surface, (10, 10))

helvetica_font = pygame.font.Font("Helvetica.ttf", 32) #Arguments : La police (téléchargée), Taille de la police
helvetica_text = helvetica_font.render("Bonsoir les zamis", True, blank) #Args : Text, Anti-aliasing (Bool), Color
window_surface.blit(helvetica_text, (10, 10)) #Affiche la surface ; Args : Surface (Text), Coords(x, y)

"""
print(pygame.time.get_ticks())
pygame.time.wait(5000) --> Sleep le processus
pygame.time.delay(5000) --> Stop carrément le processus 
"""

pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            launched= False

    # Corps du programme
    #window_surface.fill(blank_color)
    #window_surface.blit(logo_image, (12, 12))  # Charge l'image --> Image, Position du coin haut gauche
    """
    while not myrect.colliderect(myblock): #Ajout de premières collisions
    time.sleep(.010) #Chaque itérations de la boucle est effectuée après ce délai
    window_surface.fill(black_color) #
    myrect.x += 1
    pygame.draw.rect(window_surface, red_color, myrect)
    pygame.draw.rect(window_surface, blue_color, myblock)
        if myrect.colliderect(myblock): #Permet de faire changer le cube de couleur à l'impact
            time.sleep(.010)
            window_surface.fill(black_color)
            pygame.draw.rect(window_surface, green, myrect)
            pygame.draw.rect(window_surface, blue_color, myblock)
    pygame.display.flip()
    """
    """
    elif event.type == pygame.VIDEORESIZE: #Lorsque la fenêtre est redimensionnée
        window_surface.fill(black_color)
        helvetica = pygame.font.Font("Helvetica.ttf", 32) #Réactualise les infos en réaffichant le text
        text_helvetica = helvetica.render("{}x{}".format(event.w, event.h), True, white_color)
        window_surface.blit(text_helvetica, (10, 10))
        pygame.display.flip()
    """
    pygame.display.flip()  # Joue un rôle d'update de la fenêtre --> De l'affichage --> Display


pygame.quit()

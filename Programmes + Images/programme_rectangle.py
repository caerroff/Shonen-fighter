
import pygame
import time
from tkinter import *

#Création de la fênetre de lancement du jeu
main = Tk()
main.title("Shonen Fighter")
main.geometry("1023x682")
main.minsize(1023, 682)
main.maxsize(1023, 682)

white_color = (255, 255, 255)
black_color = (0, 0, 0)
red_color = (255, 0, 0)
green_color = (0, 255, 0)
blue_color = (0, 0, 255)
colorDef = (255, 255, 255)

print(colorDef)

def changeRect(var):
    global colorDef
    if var == 1:
        colorDef = blue_color
    if var == 2:
        colorDef = red_color
    if var == 3:
        colorDef = green_color

    print(colorDef)
    #return colorDef

def settings():
    frameSettings = Frame(main, bg="grey", width=450, height=450, bd=3, relief=SUNKEN)
    frameSettings.place(relx=0.25, rely=0.1, anchor=N)

    buttonClose = Button(frameSettings, text="Fermer",bg="lightgrey", font=("Helvetica", 10), width=15, command=frameSettings.destroy)
    buttonClose.place(relx=0.66, rely=0.9)

#Importation et affichage de l'image de fond d'écran de la fênetre
shonen = PhotoImage(file='naruto_bg.png')
labelShonen = Label(main, image=shonen)
labelShonen.place(x=0, y=0, relwidth=1, relheight=1)

#Bouton Jouer
buttonJouer = Button(main, text="Bleu", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=lambda: changeRect(1))
buttonJouer.place(x=120, y=85)

#Bouton Settings
buttonSettings = Button(main, text="Rouge", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=lambda: changeRect(2))
buttonSettings.place(x=120, y=175)

#Bouton Settings2
buttonSettings2 = Button(main, text="Vert", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=lambda: changeRect(3))
buttonSettings2.place(x=120, y=265)

#Bouton Quitter
buttonLeave = Button(main, text="Quitter", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=main.destroy)
buttonLeave.place(x=120, y=355)

main.mainloop()

pygame.init()
window_resolution = (640, 480) #Resolution de la fenêtre (Window)
pygame.display.set_caption("My Game") #Titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE) #Définition de la Surface qu'on va manipuler

liste = [red_color, green_color, blue_color]
i = True

helvetica = pygame.font.Font("Helvetica.ttf", 32)
text_helvetica = helvetica.render("{}".format(window_surface), True, white_color)
window_surface.blit(text_helvetica, (10, 10))

monRectX = 300
monRectY = 300
monRectL = 100
monRectH = 50

monRect = pygame.Rect(monRectX, monRectY, monRectL, monRectH)
pygame.draw.rect(window_surface, colorDef, monRect)
rgbRect = pygame.Rect(monRectX, monRectY, monRectL, monRectH)
pygame.draw.rect(window_surface, colorDef, rgbRect)

pygame.display.flip()

launched = True
while launched: #Boucle permettant de garder la fenêtre ouverte tant qu'une touche (kewdown) n'est pas pressée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Haut")
                window_surface.fill(black_color)
                monRect.y += -5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_DOWN:
                print("Bas")
                window_surface.fill(black_color)
                monRect.y += 5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_LEFT:
                print("Gauche")
                window_surface.fill(black_color)
                monRect.x += -5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_RIGHT:
                print("Droit")
                window_surface.fill(black_color)
                monRect.x += 5
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_RETURN:
                launched = False
            elif event.key == pygame.K_g:
                print("Green")
                colorDef = green_color
                window_surface.fill(black_color)
                pygame.draw.rect(window_surface, colorDef, monRect)
                pygame.display.flip()
            elif event.key == pygame.K_SPACE:
                while i:
                    for c in liste:
                        window_surface.fill(black_color)
                        colorDef = c
                        pygame.draw.rect(window_surface, colorDef, monRect)
                        pygame.display.flip()
            else:
                print("Autre Touche")
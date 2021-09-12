from tkinter import *


#Création de la fênetre de lancement du jeu
main = Tk()
main.title("Shonen Fighter")
main.geometry("1023x682")
main.minsize(1023, 682)
main.maxsize(1023, 682)

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
buttonJouer = Button(main, text="Jouer", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10)
buttonJouer.place(x=120, y=85)

#Bouton Settings
buttonSettings = Button(main, text="Options", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=settings)
buttonSettings.place(x=120, y=175)

#Bouton Quitter
buttonLeave = Button(main, text="Quitter", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=main.destroy)
buttonLeave.place(x=120, y=265)

main.mainloop()
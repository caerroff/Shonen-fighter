from tkinter import *

def main():
    #Création de la fenêtre main --> Lancement du jeu, Options
    global mainWin
    mainWin = Tk()
    mainWin.title("Narrative Story")
    mainWin.geometry("1280x720+128+72")
    mainWin.config(bg="#8E8482")
    mainWin.minsize(700, 500)
    mainWin.iconbitmap("yinyang.ico")

    buttonStart = Button(mainWin, text="Nouvelle Partie", font=("Helvetica"\
    , 22), bg="lightgrey", width=20, command=game)
    buttonStart.place(relx=0.5, rely=0.2, anchor=S)

    buttonContinueGame = Button(mainWin, text="Continuer une partie"\
    , font=("Helvetica", 22), bg="lightgrey", width=20, command=game)
    buttonContinueGame.place(relx=0.5, rely=0.35, anchor=S)

    buttonOptions = Button(mainWin, text="Options", font=("Helvetica"\
    , 22), bg="lightgrey", width=10, command=settings)
    buttonOptions.place(relx=0.5, rely=0.5, anchor=S)

    buttonLeaveMenu = Button(mainWin, text="Quitter", font=("Helvetica"\
    , 22), bg="lightgrey", width=10, command=quitMenu)
    buttonLeaveMenu.place(relx=0.5, rely=0.7, anchor=S)

    mainWin.mainloop()

def settings():
    #Création de l'onglet options
    frameSettings = Frame(mainWin, bg="grey", bd=1, relief=RAISED, width=600, height=300)
    frameSettings.place(relx=0.5, rely=0.3, anchor=N)

    buttonTest = Button(frameSettings, text="Test", font=("Helvetica"\
    , 22), bg="lightgrey", width=8)
    buttonTest.place(relx=0.15, rely=0.29, anchor=S)

    buttonLanguage = Button(frameSettings, text="Langue", font=("Helvetica"\
    , 22), bg="lightgrey", width=8, command=language)
    buttonLanguage.place(relx=0.15, rely=0.57, anchor=S)

    buttonClose = Button(frameSettings, text="Fermer", font=("Helvetica"\
    , 22), bg="lightgrey", command=frameSettings.destroy)
    buttonClose.place(relx=0.85, rely=0.9, anchor=S)

def language():
    #Onglet permettant de changer la langue du programme
    frameLanguage = Frame(mainWin, bg="grey", bd=1, relief=RAISED, width=800, height=300)
    frameLanguage.place(relx=0.5, rely=0.3, anchor=N)

    buttonFrench = Button(frameLanguage, text="Français", font=("Helvetica", 22), bg="lightgrey", bd=2.5, relief=RAISED)
    buttonFrench.place(relx=0.12, rely=0.29, anchor=S, width=130)

    buttonEnglish = Button(frameLanguage, text="Anglais", font=("Helvetica", 22), bg="lightgrey", bd=2.5, relief=RAISED)
    buttonEnglish.place(relx=0.12, rely=0.6, anchor=S, width=130)

    frameCheck = Frame()

    buttonClose = Button(frameLanguage, text="Fermer", font=("Helvetica"\
    , 22), bg="lightgrey", command=frameLanguage.destroy)
    buttonClose.place(relx=0.85, rely=0.9, anchor=S)

def game():
    #Création de la fenetre de jeu
    global gameWin, mainWin
    gameWin = Tk()
    gameWin.title("Jeu")
    gameWin.geometry("1280x720")
    gameWin.config(bg="#49403E")
    gameWin.attributes("-fullscreen", True)

    frameGame = Frame(gameWin, bg="grey", bd=1, relief=RAISED, width=1300, height=700)
    frameGame.place(relx=0.5, rely=0.5, anchor=CENTER)

    labelWelcome = Label(frameGame, text=dicoText.get("Page_1"), \
    font=("Helvetica", 22), bg="lightgrey")
    labelWelcome.place(relx=0.5, rely=0.15, anchor=N)

    labelExplaination = Label(frameGame, text=dicoText.get("Page_1_2"), \
    font=("Helvetica", 22), bg="lightgrey", wraplength=1000, justify="left")
    labelExplaination.place(relx=0.5, rely=0.3, anchor=N)

    buttonLeaveGame = Button(frameGame, text="Quitter la partie", font=("Helvetica"\
    , 22), bg="lightgrey", command=quitGame)
    buttonLeaveGame.place(relx=0.10, rely=0.95, anchor=S)

    gameWin.mainloop()

#Création de tout les champs de textes
#global monDico
dicoText = {"Page_1" : "Bienvenu dans Light & Shadow : Resistence", "Page_1_2" \
: "Dans Light & Shadow : Resistence, vous incarnez [?],\n une jeune avanturière \
en quête de réponses concernant le monde qui l'entoure. BlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlabla\
BlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlablaBlabla"}


def quitGame():
    #Création de l'ui permettant de quitter ou non le partie en cours
    frameQuit = Frame(gameWin, bg="grey", bd=1, relief=RAISED, width=800, height=300)
    frameQuit.place(relx=0.5, rely=0.37, anchor=N)

    labelCheck = Label(frameQuit, text="Voulez-vous quitter la partie et \
retourner au menu principal ?", font=("Helvetica", 22), bg="lightgrey", bd=2.5, relief=RAISED)
    labelCheck.place(relx=0.5, rely=0.5, anchor=S)

    buttonYes = Button(frameQuit, text="Oui", font=("Helvetica", 22), bg="lightgrey", width=7,command=gameWin.destroy)
    buttonYes.place(relx=0.3, rely=0.65, anchor=N)

    buttonNo = Button(frameQuit, text="Non", font=("Helvetica", 22), bg="lightgrey", width=7, command=frameQuit.destroy)
    buttonNo.place(relx=0.7, rely=0.65, anchor=N)

def quitMenu():
    mainWin.destroy()

main()
import pygame
from tkinter import *

#Création de la fênetre de lancement du jeu
main = Tk()
main.title("Shonen Fighter")
main.geometry("1023x682")
main.minsize(1023, 682)
main.maxsize(1023, 682)

bg = pygame.image.load('../Sprite/bg.jpg')
bg_1 = pygame.image.load('../Sprite/bg_1.jpg')
bg2 = pygame.image.load('../Sprite/Bg_2.jpg')
bg3 = pygame.image.load('../Sprite/Bg_3.jpg')
bg4 = pygame.image.load('../Sprite/Bg_4.jpg')
background = bg

rounds = 3
current_round = 1

player1Character = 4
player2Character = 3

isHitbox = False
soundActivated = False

def soundsFunction():
    """Function that imports the differents sounds of the game """
    global kunaiSound, kunaiImpactSound
    kunaiSound = pygame.mixer.Sound("../Sprite/Sounds/kunai_flying.wav")
    kunaiImpactSound = pygame.mixer.Sound("../Sprite/Sounds/kunai_impact.wav")

    pygame.mixer.music.load('../Sprite/Music/naruto_theme.mp3')
    pygame.mixer.music.play(-1)

def isSoundActivated():
    """Function that check if sounds are activated, and so can call the SoundsFunction"""
    global soundActivated
    soundActivated = True
    soundsFunction()

def settings():
    """Settings Menu for the Gui"""
    frameSettings = Frame(main, bg="grey", width=450, height=450, bd=3, relief=SUNKEN)
    frameSettings.place(relx=0.25, rely=0.1, anchor=N)

    buttonClose = Button(frameSettings, text="Fermer",bg="lightgrey", font=("Helvetica", 10), width=15, command=frameSettings.destroy)
    buttonClose.place(relx=0.66, rely=0.9)

def player1ChooseCharacter(value):
    """Function that return (to use after) which character the Player 1 chose"""
    global player1Character
    player1Character = value
    return player1Character

def player2ChooseCharacter(value):
    """Function that return (to use after) which character the Player 2 chose"""
    global player2Character
    player2Character = value

def chooseNumberRounds(value):
    """Function, in the Gui, that allows to change the number of rounds of the game"""
    global rounds
    rounds = value

def chooseBackground(value):
    """Function, in the Gui, that allows to change the background (Map) of the game"""
    global background
    if value == 1:
        background = bg
    if value == 2:
        background = bg2
    if value == 3:
        background = bg4
    #else:
    #    background = bg

def showHitbox():
    global isHitbox
    isHitbox = True

def selectCharacter():
    """Function, in the Gui, that allows to select a character for each player and the number of rounds for the game"""
    global winSelect, player1Character, player2Character
    main.destroy()

    winSelect = Tk()
    winSelect.title("Shonen Fighter - Select Character")
    winSelect.geometry("1023x682")
    winSelect.minsize(1023, 682)
    winSelect.maxsize(1023, 682)

    frame = Frame(winSelect, bg='white', width=5000, height=5000)

    # Frame that prints the icons of characters for Player 1
    image_player1_frame = Frame(frame, bg="white")
    image_player1_frame.grid(row=0, column=0, sticky=W, pady=10)

    # Frame that allows to select a character for the Player 1
    select_player1_frame = Frame(frame, bg="white")  # bd=1, relief=SUNKEN
    select_player1_frame.grid(row=1, column=0, sticky=W)

    # Frame that prints the icons of characters for Player 2
    image_player2_frame = Frame(frame, bg="white")
    image_player2_frame.grid(row=2, column=0, sticky=W, pady=10)

    # Frame that allows to select a character for the Player 1
    select_player2_frame = Frame(frame, bg="white")  # bd=1, relief=SUNKEN
    select_player2_frame.grid(row=3, column=0, sticky=W)

    # Frame that allows to select the number of Rounds
    rounds_frame = Frame(frame, padx=500, pady=50, bg='white')
    rounds_frame.grid(row=4, column=0, sticky=W)

    # Frame that allows to choose the background
    background_frame = Frame(frame, padx=500, pady=10, bg='white')
    background_frame.grid(row=5, column=0, sticky=W)

    # Frame that allows to Start the game
    bottomButtons = Frame(frame, padx=500, pady=50, bg='white')
    bottomButtons.grid(row=6, column=0, sticky=W)

    # Invisible Label To Use Grid / Place
    invisibleLabel = Label(bottomButtons, text='')
    invisibleLabel.grid()

    # Invisible Label To Use Grid / Place
    invisibleLabel2 = Label(rounds_frame, text='')
    invisibleLabel2.grid()

    # Invisible Label To Use Grid / Place
    invisibleLabel3 = Label(background_frame, text='')
    invisibleLabel3.grid()

    # Label Background
    labelBackground = Label(background_frame, text='Background', bg='lightgrey', font=("Helvetica", 10), width=15, border=1)
    labelBackground.place(x=-470, y=0)

    # Label Background 1 (Normal / Day)
    buttonBackground_1 = Button(background_frame, text='Day', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseBackground(1))
    buttonBackground_1.place(x=-307, y=0)

    # Label Background 2 (Forest)
    buttonBackground_2 = Button(background_frame, text='Forest', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseBackground(2))
    buttonBackground_2.place(x=-120, y=0)

    # Label Background 3 (Night)
    buttonBackground_3 = Button(background_frame, text='Night', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseBackground(3))
    buttonBackground_3.place(x=70, y=0)

    # Label Rounds
    labelRounds = Label(rounds_frame, text='Rounds (To Win)', bg='lightgrey', font=("Helvetica", 10), width=15, border=1)
    labelRounds.place(x=-470, y=0)

    # Button Rounds = 1
    buttonRounds1 = Button(rounds_frame, text='1 Round', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseNumberRounds(1))
    buttonRounds1.place(x=-307, y=0)

    # Button Rounds = 2
    buttonRounds2 = Button(rounds_frame, text='3 Rounds', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseNumberRounds(3))
    buttonRounds2.place(x=-120, y=0)

    # Button Rounds = 3
    buttonRounds3 = Button(rounds_frame, text='5 Rounds', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: chooseNumberRounds(5))
    buttonRounds3.place(x=70, y=0)

    # Button Sounds
    buttonSounds = Button(bottomButtons, text='Sounds', bg='white', font=("Helvetica", 10), width=15, border=1, command=isSoundActivated)
    buttonSounds.place(x=-100, y=0)

    # Button Hitbox
    buttonHitbox = Button(bottomButtons, text='Hitbox', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=showHitbox)
    buttonHitbox.place(x=100, y=0)

    # Button Play
    buttonPlay = Button(bottomButtons, text='Play', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=launchGame)
    buttonPlay.place(x=300, y=0)

    # Icon Naruto Player 1
    iconNaruto = PhotoImage(file='../Sprite/Naruto/Icon/Sprite 1.png')
    labelIconNaruto = Label(image_player1_frame, image=iconNaruto)
    labelIconNaruto.grid(row=0, column=1, sticky=W, padx=10)

    # Icon Naruto Player 2
    iconNaruto2 = PhotoImage(file='../Sprite/Naruto/Icon/Sprite 1.png')
    labelIconNaruto2 = Label(image_player2_frame, image=iconNaruto2)
    labelIconNaruto2.grid(row=0, column=1, sticky=W, padx=10)

    # Icon Sasuke Player 1
    iconSasuke = PhotoImage(file='../Sprite/Sasuke/Icon/Sprite 2.png')
    labelIconSasuke = Label(image_player1_frame, image=iconSasuke)
    labelIconSasuke.grid(row=0, column=2, sticky=W, padx=40)

    # Icon Sasuke Player 2
    iconSasuke2 = PhotoImage(file='../Sprite/Sasuke/Icon/Sprite 2.png')
    labelIconSasuke2 = Label(image_player2_frame, image=iconSasuke2)
    labelIconSasuke2.grid(row=0, column=2, sticky=W, padx=40)

    # Icon Itachi Player 1
    iconItachi = PhotoImage(file='../Sprite/Itachi/Icon/Sprite 1.png')
    labelIconItachi = Label(image_player1_frame, image=iconItachi)
    labelIconItachi.grid(row=0, column=3, sticky=W, padx=20)

    # Icon Itachi Player 2
    iconItachi2 = PhotoImage(file='../Sprite/Itachi/Icon/Sprite 1.png')
    labelIconItachi2 = Label(image_player2_frame, image=iconItachi2)
    labelIconItachi2.grid(row=0, column=3, sticky=W, padx=20)

    # Player 1 Label (Void)
    labelPlayer1Image = Label(image_player1_frame, text='', bg='white', font=("Helvetica", 10), width=15, border=1)
    labelPlayer1Image.grid(row=0, column=0, sticky=W, padx=30)

    # Player 1 Label
    labelPlayer1 = Label(select_player1_frame, text='Player 1 Character :', bg='lightgrey', font=("Helvetica", 10), width=15, border=1)
    labelPlayer1.grid(row=0, column=0, sticky=W, padx=30)

    # Player 2 Label (Void)
    labelPlayer2Image = Label(image_player2_frame, text='', bg='white', font=("Helvetica", 10), width=15, border=1)
    labelPlayer2Image.grid(row=0, column=0, sticky=W, padx=30)

    # Player 2 Label
    labelPlayer2 = Label(select_player2_frame, text='Player 2 Character :', bg='lightgrey', font=("Helvetica", 10), width=15, border=1)
    labelPlayer2.grid(row=0, column=0, sticky=W, padx=30)

    # Button Naruto Player 1
    player1Naruto = Button(select_player1_frame, text='Naruto', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player1ChooseCharacter(1))
    player1Naruto.grid(row=0, column=1, sticky=W, padx=10)

    # Button Sasuke Player 1
    player1Sasuke = Button(select_player1_frame, text='Sasuke', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player1ChooseCharacter(2))
    player1Sasuke.grid(row=0, column=2, sticky=W, padx=50)

    # Button Itachi Player 1
    player1Itachi = Button(select_player1_frame, text='Itachi', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player1ChooseCharacter(3))
    player1Itachi.grid(row=0, column=3, sticky=W, padx=10)

    # Button Naruto Player 2
    player2Naruto = Button(select_player2_frame, text='Naruto', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player2ChooseCharacter(1))
    player2Naruto.grid(row=0, column=4, sticky=W, padx=10)

    # Button Sasuke Player 2
    player2Sasuke = Button(select_player2_frame, text='Sasuke', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player2ChooseCharacter(2))
    player2Sasuke.grid(row=0, column=5, sticky=W, padx=50)

    # Button Itachi Player 2
    player2Itachi = Button(select_player2_frame, text='Itachi', bg='lightgrey', font=("Helvetica", 10), width=15, border=1, command=lambda: player2ChooseCharacter(3))
    player2Itachi.grid(row=0, column=6, sticky=W, padx=10)

    # Affichage de toute la frame (l'ensemble de ce qu'il faut afficher)
    frame.grid(ipadx=50, ipady=50)

    winSelect.mainloop()

launched = False
def launchGame():
    """Function that allows to launch the game"""
    global launched
    launched = True
    winSelect.destroy()

#Importation et affichage de l'image de fond d'écran de la fênetre
shonen = PhotoImage(file='../Sprite/naruto_bg.png')
labelShonen = Label(main, image=shonen)
labelShonen.place(x=0, y=0, relwidth=1, relheight=1)

# Button Play
buttonJouer = Button(main, text="Jouer", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=selectCharacter)
buttonJouer.place(x=120, y=85)

# Button Settings
buttonSettings = Button(main, text="Options", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=settings)
buttonSettings.place(x=120, y=175)

# Button Leave
buttonLeave = Button(main, text="Quitter", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=main.destroy)
buttonLeave.place(x=120, y=265)

main.mainloop()
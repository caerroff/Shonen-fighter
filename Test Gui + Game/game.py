# -*- coding: utf-8 -*-
import pygame, time
from perso_os import *
from random import *
from tkinter import *
#from gui import *

#Création de la fênetre de lancement du jeu
main = Tk()
main.title("Shonen Fighter")
main.geometry("1023x682")
main.minsize(1023, 682)
main.maxsize(1023, 682)

player1Character = 1
player2Character = 1

def settings():
    frameSettings = Frame(main, bg="grey", width=450, height=450, bd=3, relief=SUNKEN)
    frameSettings.place(relx=0.25, rely=0.1, anchor=N)

    buttonClose = Button(frameSettings, text="Fermer",bg="lightgrey", font=("Helvetica", 10), width=15, command=frameSettings.destroy)
    buttonClose.place(relx=0.66, rely=0.9)

def player1ChooseCharacter(value):
    global player1Character
    player1Character = value
    return player1Character

def player2ChooseCharacter(value):
    global player2Character
    player2Character = value

def selectCharacter():
    global winSelect, player1Character
    main.destroy()

    winSelect = Tk()
    winSelect.title("Shonen Fighter - Select Character")
    winSelect.geometry("1023x682")
    winSelect.minsize(1023, 682)
    winSelect.maxsize(1023, 682)

    player1Naruto = Button(winSelect, text='Naruto', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player1ChooseCharacter(1))
    player1Naruto.place(relx=0.2, rely=0.2)

    player1Sasuke = Button(winSelect, text='Sasuke', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player1ChooseCharacter(2))
    player1Sasuke.place(relx=0.4, rely=0.2)

    player1Itachi = Button(winSelect, text='Itachi', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player1ChooseCharacter(3))
    player1Itachi.place(relx=0.6, rely=0.2)

    player2Naruto = Button(winSelect, text='Naruto', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player2ChooseCharacter(1))
    player2Naruto.place(relx=0.2, rely=0.4)

    player2Sasuke = Button(winSelect, text='Sasuke', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player2ChooseCharacter(2))
    player2Sasuke.place(relx=0.4, rely=0.4)

    player2Itachi = Button(winSelect, text='Itachi', bg='lightgrey', font=("Helvetica", 10), width=15, command=lambda: player2ChooseCharacter(3))
    player2Itachi.place(relx=0.6, rely=0.4)

    buttonPlay = Button(winSelect, text='Play', bg='lightgrey', font=("Helvetica", 10), width=15, command=launchGame)
    buttonPlay.place(relx=0.8, rely=0.7)

    #buttonSounds = Button(winSelect, text='Sounds', bg='lightgrey', font=("Helvetica", 10), width=15, command=soundsFunction)
    #buttonSounds.place(relx=0.6, rely=0.7)

    winSelect.mainloop()

global launched
launched = False
def launchGame():
    global launched
    launched = True
    winSelect.destroy()

#Importation et affichage de l'image de fond d'écran de la fênetre
shonen = PhotoImage(file='naruto_bg.png')
labelShonen = Label(main, image=shonen)
labelShonen.place(x=0, y=0, relwidth=1, relheight=1)

#Bouton Jouer
buttonJouer = Button(main, text="Jouer", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=selectCharacter)
buttonJouer.place(x=120, y=85)

#Bouton Settings
buttonSettings = Button(main, text="Options", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=settings)
buttonSettings.place(x=120, y=175)

#Bouton Quitter
buttonLeave = Button(main, text="Quitter", font=("Helvetica", 22), bg="white", bd=3, relief=SUNKEN, width=10, command=main.destroy)
buttonLeave.place(x=120, y=265)

main.mainloop()

# /////////// PYGAME ///////////

pygame.init()
pygame.font.init()

win_res = (700, 400)
win = pygame.display.set_mode(win_res)
pygame.display.set_caption("Shonen Fighter")
clock = pygame.time.Clock()

soundActivated = False

def soundsFunction():
    global kunaiSound, kunaiImpactSound
    kunaiSound = pygame.mixer.Sound("kunai_flying.wav")
    kunaiImpactSound = pygame.mixer.Sound("kunai_impact.wav")

    pygame.mixer.music.load('naruto_theme.mp3')
    pygame.mixer.music.play(-1)

font = pygame.font.Font("Helvetica.ttf", 30)  # Font importé pour le score
player2Score = 0
player1Score = 0

rect1 = pygame.Rect(250, 70, 65, 65)  # Constructeur d'objet --> Rectangle, Arg: x, y, w, h
rect2 = pygame.Rect(350, 70, 65, 65)  # Constructeur d'objet --> Rectangle, Arg: x, y, w, h

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (109, 111, 111)
blue_mana = (0, 186, 240)
yellow = (255, 232, 1)
purple = (66, 0, 255)

kunaiSpriteRight = pygame.image.load('../Sprite/Kunai/sprite.png')
kunaiSpriteLeft = pygame.transform.flip(kunaiSpriteRight, True, False)
bg = pygame.image.load('../Sprite/bg.jpg')
bg2 = pygame.image.load('../Sprite/bg2.jpg')

spawnEffect = False
nextAnim = False
nextAnim2 = False

class Player(object):
    def __init__(self, x, y, width, height, playerNumber, characterNumber):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJumping = False
        self.isFalling = False
        self.isBlock = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.combo1 = False
        self.throw = False
        self.spell1 = False
        self.spell2 = False
        self.standing = True
        self.standingRight = False
        self.standingLeft = False
        self.facingLeft = False
        self.facingRight = False
        self.hitbox = (self.x, self.y, 47, 60)
        self.health = 100
        self.dealable = False
        self.damaged = False
        self.mana = 200
        self.molding = False
        self.awakening = 0
        self.awaken = False
        self.transforming = False
        self.isContact = False
        self.playerNumber = playerNumber
        self.characterNumber = characterNumber
        self.current_sprite = 0
        self.current_sprite2 = 0
        self.counter = 0

    def animator(self, list, increm, iter = 0):
        global spawnEffect
        if iter == 1:
            if self.current_sprite >= len(list):
                if self.spell1:
                    self.spell1 = False
                    self.dealable = False
                    self.standing = True
                if self.spell2:
                    self.spell2 = False
                    spawnEffect = True
                self.standing = True
                if self.combo1:
                    self.combo1 = False
                    self.dealable = False
                    self.counter += 1
                if self.damaged:
                    self.damaged = False
                if self.transforming:
                    self.transforming = False
                    self.awaken = True
                    self.standing = True
                if self.facingLeft:
                    self.standingLeft = True
                if self.facingRight:
                    self.standingRight = True
                return
            else:
                win.blit(list[int(self.current_sprite)], (self.x, self.y))
                self.current_sprite += increm
        else:
            if self.current_sprite >= len(list):
                self.current_sprite = 0
            win.blit(list[int(self.current_sprite)], (self.x, self.y))
            self.current_sprite += increm

    def doubleAnimation(self, listA, listB, increm = 1, increm2 = 0.35):
        global nextAnim, nextAnim2
        nextAnim, nextAnim2 = False, False

        if self.playerNumber == 1:
            if self.current_sprite < len(listA):
                win.blit(listA[int(self.current_sprite)], (self.x, self.y))
                self.current_sprite += increm
            if self.current_sprite >= len(listA):
                nextAnim = True
            if nextAnim:
                if self.current_sprite2 >= len(listB):
                    self.spell1 = False
                    self.spell2 = False
                    self.dealable = False
                    self.standing = True
                else:
                    self.dealable = True
                    if self.awaken:
                        if self.facingLeft and self.x > self.vel:
                            self.x -= 20
                        if self.facingRight and self.x < 700 - self.width - self.vel:
                            self.x += 20
                    win.blit(listB[int(self.current_sprite2)], (self.x, self.y))
                    self.current_sprite2 += increm2
                    if self.current_sprite2 >= len(listB):
                        self.spell1 = False
                        self.spell2 = False
                        self.dealable = False
                        self.standing = True
                        self.current_sprite2 = 0

        if self.playerNumber == 2:
            if self.current_sprite < len(listA):
                win.blit(listA[int(self.current_sprite)], (self.x, self.y))
                self.current_sprite += increm
            else:
                nextAnim2 = True
            if nextAnim2:
                if self.current_sprite >= len(listA):
                    if self.current_sprite >= len(listB):
                        self.spell1 = False
                        self.spell2 = False
                        self.dealable = False
                        self.standing = True
                    else:
                        self.dealable = True
                        if self.facingLeft and self.x > self.vel:
                            self.x -= 20
                        if self.facingRight and self.x < 700 - self.width - self.vel:
                            self.x += 20
                        win.blit(listB[int(self.current_sprite)], (self.x, self.y))
                        self.current_sprite += increm2
                        if self.current_sprite >= len(listB):
                            self.spell1 = False
                            self.spell2 = False
                            self.dealable = False
                            self.standing = True

    def character(self):
        if self.characterNumber == 1:
            self.draw_naruto(win)
        elif self.characterNumber == 2:
            self.draw_sasuke(win)
        elif self.characterNumber == 3:
            self.draw_itachi(win)

    def draw_ath_player1(self, win):
            pygame.draw.rect(win, red, (20, 22, 200, 10))
            pygame.draw.rect(win, green, (20, 22, 200 - (2 * (100 - self.health)), 10))
            pygame.draw.rect(win, grey, (20, 35, 200, 10))
            pygame.draw.rect(win, blue_mana, (20, 35, 0 + self.mana, 10))
            pygame.draw.rect(win, grey, (20, 50, 200, 10))
            pygame.draw.rect(win, yellow, (20, 50, 0 + self.awakening, 10))

    def draw_ath_player2(self, win):
            pygame.draw.rect(win, red, (475, 22, 200, 10))
            pygame.draw.rect(win, green, (475, 22, 200 - (2 * (100 - self.health)), 10))
            pygame.draw.rect(win, grey, (475, 35, 200, 10))
            pygame.draw.rect(win, blue_mana, (475, 35, 0 + self.mana, 10))
            pygame.draw.rect(win, grey, (475, 50, 200, 10))
            pygame.draw.rect(win, yellow, (475, 50, 0 + self.awakening, 10))

    def draw_naruto(self, win):
        if not self.standing:
            if self.left:
                if self.isJumping and self.isFalling:
                    self.animator(Naruto['FallingLeft'], 1)
                elif self.isJumping:
                    self.animator(Naruto['JumpingLeft'], 0.3)
                else:
                    self.animator(Naruto['RunLeft'], 0.5)
            elif self.right:
                if self.isJumping and self.isFalling:
                    self.animator(Naruto['FallingRight'], 1)
                elif self.isJumping:
                    self.animator(Naruto['JumpingRight'], 0.3)
                else:
                    self.animator(Naruto['RunRight'], 0.5)
        elif self.isBlock:
            if self.left or self.facingLeft:
                self.animator(Naruto['BlockLeft'], 1)
            elif self.right or self.facingRight:
                self.animator(Naruto['BlockRight'], 1)
            else:
                self.animator(Naruto['BlockRight'], 1)
            self.isBlock = False
        elif self.combo1:
            if self.facingRight:
                self.animator(Naruto['Combo1Right'], 0.4)
            elif self.facingLeft:
                self.animator(Naruto['Combo1Left'], 0.4)
            self.combo1 = False
        elif self.throw:
            if self.facingRight:
                self.animator(Naruto['ThrowRight'], 1)
            if self.facingLeft:
                self.animator(Naruto['ThrowLeft'], 1)
            self.throw = False
        elif self.spell1:
            if self.facingRight:
                self.animator(Naruto['Spell1Right'], 1)
            if self.facingLeft:
                self.animator(Naruto['Spell1Left'], 1)
        elif self.awaken:
            if self.facingRight:
                self.animator(Sasuke['AwakeningRight'], 0.2)
            if self.facingLeft:
                self.animator(Sasuke['AwakeningLeft'], 0.2)
            self.awaken = False
        elif self.molding:
            if self.facingRight:
                self.animator(Naruto['BlockRight'], 1)
            if self.facingLeft:
                self.animator(Naruto['BlockRight'], 1)
            self.molding = False
        elif self.damaged:
            if self.facingRight:
                self.animator(Naruto['DamagedRight'], 1)
            if self.facingLeft:
                self.animator(Naruto['DamagedLeft'], 1)
            self.damaged = False
        elif self.isJumping:
            if self.facingRight:
                if self.isFalling:
                    self.animator(Naruto['FallingRight'], 1)
                else:
                    self.animator(Naruto['JumpingRight'], 1)
            if self.facingLeft:
                if self.isFalling:
                    self.animator(Naruto['FallingLeft'], 1)
                else:
                    self.animator(Naruto['JumpingLeft'], 1)
        elif self.playerNumber == 1:
            if self.right:
                self.animator(Naruto['StandRight'], 1)
                self.facingRight = True
            elif self.left:
                self.animator(Naruto['StandLeft'], 1)
                self.facingLeft = True
            else:
                self.animator(Naruto['StandRight'], 1)
                self.facingRight = True
        elif self.playerNumber == 2:
            if self.right:
                self.animator(Naruto['StandRight'], 1)
                self.facingRight = True
            elif self.left:
                self.animator(Naruto['StandLeft'], 1)
                self.facingLeft = True
            else:
                self.animator(Naruto['StandLeft'], 1)
                self.facingLeft = True
        else:
            if self.right:
                self.animator(Naruto['StandRight'], 1)
                self.standingRight = True
            elif self.left:
                self.animator(Naruto['StandLeft'], 1)
                self.standingLeft = True
            else:
                self.animator(Naruto['StandRight'], 1)
                self.standingRight = True

        if not self.awaken:
            self.hitbox = (self.x, self.y, 47, 54)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        else:
            self.hitbox = (self.x, self.y, 65, 80)
            pygame.draw.rect(win, red, self.hitbox, 2)

    def draw_sasuke(self, win):
        if not self.awaken:
            if not self.standing:
                if self.left:
                    if self.isJumping and self.isFalling:
                        self.animator(Sasuke['FallingLeft'], 1)
                    elif self.isJumping:
                        self.animator(Sasuke['JumpingLeft'], 0.3)
                    else:
                        self.animator(Sasuke['RunLeft'], 0.5)
                elif self.right:
                    if self.isJumping and self.isFalling:
                        self.animator(Sasuke['FallingRight'], 1)
                    elif self.isJumping:
                        self.animator(Sasuke['JumpingRight'], 0.3)
                    else:
                        self.animator(Sasuke['RunRight'], 0.5)
            elif self.isBlock:
                if self.left or self.facingLeft:
                    self.animator(Sasuke['BlockLeft'], 1)
                elif self.right or self.facingRight:
                    self.animator(Sasuke['BlockRight'], 1)
                else:
                    self.animator(Sasuke['BlockRight'], 1)
            elif self.combo1:
                if self.facingRight:
                    self.animator(Sasuke['Combo1Right'], 0.4, 1)
                elif self.facingLeft:
                    self.animator(Sasuke['Combo1Left'], 0.4, 1)
            elif self.throw:
                if self.facingRight:
                    self.animator(Sasuke['ThrowRight'], 1)
                if self.facingLeft:
                    self.animator(Sasuke['ThrowLeft'], 1)
                self.throw = False
            elif self.spell1:
                if self.facingRight:
                    self.doubleAnimation(Sasuke['Spell1ChargeRight'], Sasuke['Spell1AttackRight'], 0.5, 0.5)
                if self.facingLeft:
                    self.doubleAnimation(Sasuke['Spell1ChargeLeft'], Sasuke['Spell1AttackLeft'], 0.5, 0.5)
            elif self.spell2:
                if self.facingRight:
                    self.animator(Sasuke['Spell2Right'], 0.2, 1)
                if self.facingLeft:
                    self.animator(Sasuke['Spell2Left'], 0.2, 1)
            elif self.molding:
                if self.facingRight:
                    self.animator(Sasuke['MoldingRight'], 0.2)
                if self.facingLeft:
                    self.animator(Sasuke['MoldingLeft'], 0.2)
                self.molding = False
            elif self.damaged:
                if self.facingRight:
                    self.animator(Sasuke['DamagedRight'], 1)
                if self.facingLeft:
                    self.animator(Sasuke['DamagedLeft'], 1)
                self.damaged = False
            elif self.isJumping:
                if self.facingRight:
                    if self.isFalling:
                        self.animator(Sasuke['FallingRight'], 1)
                    else:
                        self.animator(Sasuke['JumpingRight'], 1)
                if self.facingLeft:
                    if self.isFalling:
                        self.animator(Sasuke['FallingLeft'], 1)
                    else:
                        self.animator(Sasuke['JumpingLeft'], 1)
            elif self.transforming:
                if self.facingLeft:
                    self.animator(Sasuke['AwakeningLeft'], 0.2, 1)
                else:
                    self.animator(Sasuke['AwakeningRight'], 0.2, 1)
            elif self.playerNumber == 1:
                if self.right:
                    self.animator(Sasuke['StandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['StandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['StandRight'], 1)
                    self.facingRight = True
            elif self.playerNumber == 2:
                if self.right:
                    self.animator(Sasuke['StandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['StandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['StandLeft'], 1)
                    self.facingLeft = True
            elif self.standing:
                if self.standingLeft:
                    self.animator(Sasuke['StandLeft'], 1)
                if self.standingRight:
                    self.animator(Sasuke['StandRight'], 1)
            else:
                if self.right:
                    self.animator(Sasuke['StandRight'], 0.1)
                    self.standingRight = True
                elif self.left:
                    self.animator(Sasuke['StandLeft'], 1)
                    self.standingLeft = True
                else:
                    self.animator(Sasuke['StandRight'], 0.1)
                    self.standingRight = True
        if self.awaken:
            if not self.standing:
                if self.left:
                    if self.isJumping and self.isFalling:
                        self.animator(Sasuke['AwakeFallingLeft'], 1)
                    elif self.isJumping:
                        self.animator(Sasuke['AwakeJumpingLeft'], 0.3)
                    else:
                        self.animator(Sasuke['AwakeRunLeft'], 0.225)
                elif self.right:
                    if self.isJumping and self.isFalling:
                        self.animator(Sasuke['AwakeFallingRight'], 1)
                    elif self.isJumping:
                        self.animator(Sasuke['AwakeJumpingRight'], 0.3)
                    else:
                        self.animator(Sasuke['AwakeRunRight'], 0.225)
            elif self.isBlock:
                if self.left or self.facingLeft:
                    self.animator(Sasuke['AwakeBlockLeft'], 1)
                elif self.right or self.facingRight:
                    self.animator(Sasuke['AwakeBlockRight'], 1)
                else:
                    self.animator(Sasuke['AwakeBlockRight'], 1)
            elif self.combo1:
                if self.facingRight:
                    self.animator(Sasuke['AwakeCombo1Right'], 0.4, 1)
                elif self.facingLeft:
                    self.animator(Sasuke['AwakeCombo1Left'], 0.4, 1)
            elif self.throw:
                if self.facingRight:
                    self.animator(Sasuke['AwakeThrowRight'], 1)
                if self.facingLeft:
                    self.animator(Sasuke['AwakeThrowLeft'], 1)
                self.throw = False
            elif self.spell1:
                if self.facingRight:
                    self.doubleAnimation(Sasuke['AwakeSpell1ChargeRight'], Sasuke['AwakeSpell1AttackRight'], 0.075)
                if self.facingLeft:
                    self.doubleAnimation(Sasuke['AwakeSpell1ChargeLeft'], Sasuke['AwakeSpell1AttackLeft'], 0.075)
            elif self.spell2:
                if self.facingRight:
                    self.animator(Sasuke['AwakeSpell2Right'], 0.2, 1)
                if self.facingLeft:
                    self.animator(Sasuke['AwakeSpell2Left'], 0.2, 1)
            elif self.molding:
                if self.facingRight:
                    self.animator(Sasuke['AwakeMoldingRight'], 0.2)
                if self.facingLeft:
                    self.animator(Sasuke['AwakeMoldingLeft'], 0.2)
                self.molding = False
            elif self.isJumping:
                if self.facingRight:
                    if self.isFalling:
                        self.animator(Sasuke['AwakeFallingRight'], 1)
                    else:
                        self.animator(Sasuke['AwakeJumpingRight'], 1)
                if self.facingLeft:
                    if self.isFalling:
                        self.animator(Sasuke['AwakeFallingLeft'], 1)
                    else:
                        self.animator(Sasuke['AwakeJumpingLeft'], 1)
            elif self.playerNumber == 1:
                if self.right:
                    self.animator(Sasuke['AwakeStandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['AwakeStandRight'], 1)
                    self.facingRight = True
            elif self.playerNumber == 2:
                if self.right:
                    self.animator(Sasuke['AwakeStandRight'], 0.1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
                    self.facingLeft = True
            else:
                if self.right:
                    self.animator(Sasuke['AwakeStandRight'], 0.1)
                    self.standingRight = True
                elif self.left:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
                    self.standingLeft = True
                else:
                    self.animator(Sasuke['AwakeStandRight'], 0.1)
                    self.standingRight = True

        if not self.awaken and not self.transforming:
            self.hitbox = (self.x, self.y, 47, 66)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        if self.transforming:
            self.hitbox = (self.x, self.y, 65, 77)
            pygame.draw.rect(win, purple, self.hitbox, 2)
        if self.awaken:
            self.hitbox = (self.x, self.y, 65, 77)
            pygame.draw.rect(win, red, self.hitbox, 2)

    def draw_itachi(self, win):
        if not self.awaken:
            if not self.standing:
                if self.left:
                    if self.isJumping and self.isFalling:
                        self.animator(Itachi['FallingLeft'], 1)
                    elif self.isJumping:
                        self.animator(Itachi['JumpingLeft'], 0.3)
                    else:
                        self.y = 300
                        self.animator(Itachi['RunLeft'], 0.5)
                        #self.facingLeft = True
                elif self.right:
                    if self.isJumping and self.isFalling:
                        self.animator(Itachi['FallingRight'], 1)
                    elif self.isJumping:
                        self.animator(Itachi['JumpingRight'], 0.3)
                    else:
                        self.y = 300
                        self.animator(Itachi['RunRight'], 0.5)
                        #self.facingRight = True
            elif self.isBlock:
                if self.facingLeft:
                    self.animator(Itachi['BlockLeft'], 1)
                elif self.facingRight:
                    self.animator(Itachi['BlockRight'], 1)
            elif self.combo1:
                if self.isJumping or self.isFalling:
                    if self.facingLeft:
                        self.animator(Itachi['Combo1AirLeft'], 0.35, 1)
                    elif self.facingRight:
                        self.animator(Itachi['Combo1AirRight'], 0.35, 1)
                else:
                    if self.counter %2:
                        if self.facingLeft:
                            self.animator(Itachi['Combo1Left'], 0.4, 1)
                        elif self.facingRight:
                            self.animator(Itachi['Combo1Right'], 0.4, 1)
                    else:
                        if self.facingLeft:
                            self.animator(Itachi['Combo2Left'], 0.4, 1)
                        elif self.facingRight:
                            self.animator(Itachi['Combo2Right'], 0.4, 1)
            elif self.spell1:
                if self.facingLeft:
                    self.x -= 10
                    self.animator(Itachi['Spell1Left'], 0.5, 1)
                if self.facingRight:
                    self.x += 10
                    self.animator(Itachi['Spell1Right'], 0.45, 1)
            elif self.spell2:
                if self.facingLeft:
                    self.animator(Itachi['Spell2Left'], 0.5)
                if self.facingRight:
                    self.animator(Itachi['Spell2Right'], 0.5)
            elif self.molding:
                if self.facingLeft:
                    self.animator(Itachi['MoldingLeft'], 1)
                if self.facingRight:
                    self.animator(Itachi['MoldingRight'], 1)
                self.molding = False
            elif self.damaged:
                if self.facingLeft:
                    self.animator(Itachi['DamagedLeft'], 0.9, 1)
                if self.facingRight:
                    self.animator(Itachi['DamagedRight'],0.9, 1)
            elif self.isJumping:
                if self.facingRight:
                    if self.isFalling:
                        self.animator(Itachi['FallingRight'], 1)
                    else:
                        self.animator(Itachi['JumpingRight'], 1)
                if self.facingLeft:
                    if self.isFalling:
                        self.animator(Itachi['FallingLeft'], 1)
                    else:
                        self.animator(Itachi['JumpingLeft'], 1)
            elif self.playerNumber == 1:
                if self.left:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.facingLeft = True
                    self.left = False
                elif self.right:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 1)
                    self.facingRight = True
                    self.right = False
                elif self.facingLeft:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.facingLeft = True
                    self.left = False
                elif self.facingRight:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 1)
                    self.facingRight = True
                    self.right = False
                else:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 1)
                    self.facingRight = True
                    self.right = False
            elif self.playerNumber == 2:
                if self.right:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 0.1)
                    self.facingRight = True
                    self.right = False
                elif self.left:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.facingLeft = True
                    self.left = False
                if self.facingLeft:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.facingLeft = True
                    self.left = False
                if self.facingRight:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 1)
                    self.facingRight = True
                    self.right = False
                else:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.facingLeft = True
                    self.left = False
            else:
                if self.right:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 0.1)
                    self.standingRight = True
                    self.right = False
                elif self.left:
                    self.y = 280
                    self.animator(Itachi['StandLeft'], 1)
                    self.standingLeft = True
                    self.left = False
                else:
                    self.y = 280
                    self.animator(Itachi['StandRight'], 0.1)
                    self.standingRight = True
                    self.right = False

        if not self.awaken and not self.transforming and not self.left and not self.right and not self.combo1:
            self.hitbox = (self.x, self.y, 45, 85)
            pygame.draw.rect(win, purple, self.hitbox, 2)
        if self.left or self.right:
            self.hitbox = (self.x, self.y, 65, 65)
            pygame.draw.rect(win, purple, self.hitbox, 2)
        if self.combo1:
            self.hitbox = (self.x, self.y, 80, 85)
            pygame.draw.rect(win, red, self.hitbox, 2)

    def hit(self, damages):
        if self.health > 0:
            self.damaged = True
            self.health -= damages
            win.blit(bg, (-3, 0))
            print("Touché !", "Hp : ", self.health)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing
        self.current_sprite = 0
        self.dealable = True
        self.block = False
        self.hitbox = (self.x, self.y, 47, 60)
        self.fb_hitbox = (self.x + 25, self.y + 40, 110, 90)

    def draw(self, win):
        if facing == 1:
            win.blit(kunaiSpriteRight, (self.x, self.y))
            self.hitbox = (self.x, self.y, 20, 15)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        else:
            win.blit(kunaiSpriteLeft, (self.x, self.y))
            self.hitbox = (self.x, self.y, 20, 15)
            pygame.draw.rect(win, blue, self.hitbox, 2)

    def animator(self, list, increm):
        if self.current_sprite >= len(list) or 670 < fireball.x < -100:
            self.block = False
            return
        else:
            win.blit(list[int(self.current_sprite)], (self.x, self.y))
            if self.block:
                self.current_sprite = self.current_sprite
            else:
                self.current_sprite += increm

class fireball_projectile(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing = facing
        self.vel = 17 * facing
        self.current_sprite = 0
        self.dealable = True
        self.block = False
        self.hitbox = (self.x + 10, self.y + 35 , self.width - 5, self.height - 25)

    def animator(self, list, increm):
        if self.current_sprite >= len(list) or 670 < fireball.x < -100:
            self.block = False
            return
        else:
            win.blit(list[int(self.current_sprite)], (self.x, self.y))
            if self.block:
                self.current_sprite = self.current_sprite
            else:
                self.current_sprite += increm

    def animator2(self, list, increm):
        if self.current_sprite >= len(list) or 670 < fireball2.x < -100:
            self.block = False
            return
        else:
            win.blit(list[int(self.current_sprite)], (self.x, self.y))
            if self.block:
                self.current_sprite = self.current_sprite
            else:
                self.current_sprite += increm

    def draw_fireball(self, win):
        global fireballLoop
        if fireballLoop >= 1:
            self.current_sprite = 0

        if facing == 1:
            SasukeEffectRightRotated = []
            for i in Sasuke['EffectRight']:
                a = pygame.transform.rotate(i, 45)
                SasukeEffectRightRotated.append(a)
                fireball.animator(SasukeEffectRightRotated, 0.04)
                self.hitbox = (self.x + 10, self.y + 35 , self.width - 5, self.height - 25)
                #pygame.draw.rect(win, blue, self.hitbox, 2)

        if facing == -1:
            SasukeEffectLeftRotated = []
            for i in Sasuke['EffectLeft']:
                a = pygame.transform.rotate(i, 325)
                SasukeEffectLeftRotated.append(a)
                fireball.animator(SasukeEffectLeftRotated, 0.04)
                self.hitbox = (self.x + 10, self.y + 35 , self.width - 5, self.height - 25)
                #pygame.draw.rect(win, blue, self.hitbox, 2)

    def draw_fireball2(self, win):
        global fireballLoop2
        if fireballLoop2 >= 1:
            self.current_sprite = 0

        if facing == 1:
            SasukeEffectRightRotated = []
            for i in Sasuke['EffectRight']:
                a = pygame.transform.rotate(i, 45)
                SasukeEffectRightRotated.append(a)
                fireball2.animator2(SasukeEffectRightRotated, 0.04)
                if self.current_sprite == len(SasukeEffectRightRotated):
                    self.block = True
                self.hitbox = (self.x + 10, self.y + 35, self.width - 5, self.height - 25)
                # pygame.draw.rect(win, blue, self.hitbox, 2)

        if facing == -1:
            SasukeEffectLeftRotated = []
            for i in Sasuke['EffectLeft']:
                a = pygame.transform.rotate(i, 325)
                SasukeEffectLeftRotated.append(a)
                fireball2.animator2(SasukeEffectLeftRotated, 0.04)
                if self.current_sprite == len(SasukeEffectLeftRotated):
                    self.block = True
                self.hitbox = (self.x + 10, self.y + 35, self.width - 5, self.height - 25)
                # pygame.draw.rect(win, blue, self.hitbox, 2)


def redrawGameWindow():  # Toutes les modifications visuelles se feront ici et plus dans la boucle principale
    win.blit(bg2, (-3, 0))  # Black
    score1 = font.render("Score :" + str(player2Score), 1, (0, 0, 0))
    win.blit(score1, (20, 65))
    score2 = font.render("Score :" + str(player1Score), 1, (0, 0, 0))
    win.blit(score2, (565, 65))
    player1.character()
    player2.character()
    player1.draw_ath_player1(win)
    player2.draw_ath_player2(win)
    for kunai in kunais:
        kunai.draw(win)
    for kunai in kunais2:
        kunai.draw(win)
    for fireball in fireballs:
        fireball.draw_fireball(win)
    for fireball2 in fireballs2:
        fireball2.draw_fireball2(win)
    pygame.display.update()

# MAINLOOP
player1 = Player(100, 300, 64, 64, 1, player1Character)
fireballs = []
fireballLoop = 0
fireballs2 = []
fireballLoop2 = 0
player2 = Player(550, 300, 64, 64, 2, player2Character)
kunais = []  # Liste des Kunais --> Joueur 1
kunaiLoop = 0  # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 1
kunais2 = []  # Liste des Kunais --> Joueur 2
kunaiLoop2 = 0  # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 2
launched = True
playerSelect = True
launchGame = False
while launched:
    clock.tick(27)

    #print(player1.facingLeft ,player1.facingRight)
    #print(player1.counter)
    # Variable permettant de vérifier si une touché est pressée
    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:
        soundActivated = True
        soundsFunction()

    if keys[pygame.K_n]:
        if soundActivated:
            soundActivated = False
            pygame.mixer.music.stop()
            soundsFunction()

    # Permet de quitter le jeu avec la croix ou le bouton entrer
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False
        # ////////// PLAYER 1 //////////
        # W = Player 1 Awakening
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            # Sasuke = Cursed Mark Mode
            if not player1.awaken and player1.characterNumber == 2:
                player1.transforming = True
                player1.y = 295
        # G = Player 1 Combo 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            player1.combo1 = True
            player1.dealable = True
        # X = Player 1 Spell 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            # Sasuke = Chidori
            if not player1.transforming and player1.characterNumber == 2:
                if player1.mana >= 50:
                    player1.mana -= 50
                    player1.spell1 = True
                    player1.dealable = True
            # Itachi = Crows Attack
            if player1.characterNumber == 3:
                if player1.mana >= 50:
                    player1.mana -= 50
                    player1.spell1 = True
                    player1.dealable = True
        # C = Player 1 Spell 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            # Sasuke = Fireball Jutsu
            if not player1.transforming and not player1.spell1 and len(fireballs) < 1 and player1.characterNumber == 2:
                if player1.mana >= 50:
                    player1.mana -= 50
                    player1.spell2 = True
                    fireball_projectile.dealable = True
                    if player1.facingLeft:
                        facing = -1
                    elif player1.facingRight:
                        facing = 1
                    else:
                        facing = 1
                    if len(fireballs) < 3:
                        if facing == 1:
                            fireballs.append(fireball_projectile(player1.x, player1.y - 65, 140, 120, facing))
                        else:
                            fireballs.append(fireball_projectile(player1.x - 150, player1.y - 65, 140, 120, facing))
                    fireballLoop = 1
            # Itachi = Fireball Jutsu
        # ////////// PLAYER 2 //////////
        # W = Player 2 Awakening
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            # Sasuke = Cursed Mark Mode
            if not player2.awaken and player2.characterNumber == 2:
                player2.transforming = True
                player2.y = 295
        # O = Player 2 Combo 1 ---> Objectif : Interrompre la marche pour utiliser le combo
        if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
            if not player2.transforming:
                player2.combo1 = True
        # K = Player 2 Spell 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            # Sasuke = Chidori
            if not player2.transforming and player2.characterNumber == 2:
                if player2.mana >= 50:
                    player2.mana -= 50
                    player2.spell1 = True
                    player1.dealable = True
            # Itachi = Crows Attack
            if player2.characterNumber == 3:
                if player2.mana >= 50:
                    player2.mana -= 50
                    player2.spell1 = True
        # L = Player 2 Spell 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            # Sasuke = Fireball Jutsu
            if not player2.transforming and not player2.spell1 and len(fireballs2) < 1 and player2.characterNumber == 2:
                if player2.mana >= 50:
                    player2.mana -= 50
                    player2.spell2 = True
                    fireball_projectile.dealable = True
                    if player2.facingLeft:
                        facing = -1
                    elif player2.facingRight:
                        facing = 1
                    else:
                        facing = 1
                    if len(fireballs2) < 3:
                        if facing == 1:
                            fireballs2.append(fireball_projectile(player2.x, player2.y - 65, 140, 120, facing))
                        else:
                            fireballs2.append(fireball_projectile(player2.x - 150, player2.y - 65, 140, 120, facing))
                    fireballLoop2 = 1
            # Itachi = Fireball Jutsu

            # Undefined

    # Fireball Loop Player 1
    if fireballLoop > 0:
        fireballLoop += 1
    if fireballLoop > 1:
        fireballLoop = 0

    # Fireball Hitbox Config Player 1
    for fireball in fireballs:
        if 670 > fireball.x > -200:
            if player2.hitbox[1] < fireball.hitbox[1] + fireball.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > \
                    fireball.hitbox[1] and player2.hitbox[0] + player2.hitbox[2] > fireball.hitbox[0] and \
                    player2.hitbox[0] < \
                    fireball.hitbox[0] + fireball.hitbox[2]:
                if player2.isBlock:
                    print("Bloqué !!")
                    fireballs.pop(fireballs.index(fireball))
                else:
                    if fireball_projectile.dealable:
                        if soundActivated:
                            fireballImpactSound.play()
                        if player2.characterNumber == 3 and player2.spell1:
                            print("Dodged")
                        else:
                            player2.hit(2)
                            player1.dealable = False
                            player1Score += 1
                            if not player1.awaken:
                                if player1.awakening < 200:
                                    player1.awakening += 20
                            fireballs.pop(fireballs.index(fireball))
                            fireball_projectile.dealable = False

        # Fireball Velocity Config Player 1
        if 670 > fireball.x > -200:
            fireball.x += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))

    # Fireball Loop Player 2
    if fireballLoop2 > 0:
        fireballLoop2 += 1
    if fireballLoop2 > 1:
        fireballLoop2 = 0

    # Fireball Hitbox Config Player 2
    for fireball2 in fireballs2:
        if 670 > fireball2.x > -200:
            if player1.hitbox[1] < fireball2.hitbox[1] + fireball2.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] \
                    > fireball2.hitbox[1] and player1.hitbox[0] + player1.hitbox[2] > fireball2.hitbox[0] and \
                    player1.hitbox[0] < fireball2.hitbox[0] + fireball2.hitbox[2]:
                if player1.isBlock:
                    print("Bloqué !!")
                    fireballs2.pop(fireballs2.index(fireball2))
                else:
                    if fireball_projectile.dealable:
                        print(False)
                        if soundActivated:
                            fireballImpactSound.play()
                        if player1.characterNumber == 3 and player1.spell1:
                            print("Dodged")
                        else:
                            if player1.characterNumber == 3 and player1.spell1:
                                print("Dodged")
                            else:
                                if player1.characterNumber == 3 and player1.spell1:
                                    print("Dodged")
                                else:
                                    player1.hit(2)
                                    fireball_projectile.dealable = False
                                    player1Score += 1
                                    if not player1.awaken:
                                        if player1.awakening < 200:
                                            player1.awakening += 20
                                    fireballs2.pop(fireballs2.index(fireball2))

        # Fireball Velocity Config Player 2
        if 670 > fireball2.x > -200:
            fireball2.x += fireball2.vel
        else:
            fireballs2.pop(fireballs2.index(fireball2))

    # Fireballs Collision
    for fireball in fireballs:
        for fireball2 in fireballs2:
            if 670 > fireball.x > -200:
                if 670 > fireball2.x > -200:
                    if fireball2.hitbox[1] < fireball.hitbox[1] + fireball.hitbox[3] and fireball2.hitbox[1] + fireball2.hitbox[3] > \
            fireball.hitbox[1] and fireball2.hitbox[0] + fireball2.hitbox[2] > fireball.hitbox[0] and fireball2.hitbox[0] < \
            fireball.hitbox[0] + fireball.hitbox[2]:
                            fireballs.pop(fireballs.index(fireball))
                            fireballs2.pop(fireballs2.index(fireball2))

    # ////////////// Player 1 //////////////

    # Hitbox collision --> Pour Combo
    if player1.hitbox[1] < player2.hitbox[1] + player2.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > \
            player2.hitbox[1] and player1.hitbox[0] + player1.hitbox[2] > player2.hitbox[0] and player1.hitbox[0] < \
            player2.hitbox[0] + player2.hitbox[2]:
        player1.isContact = True
    else:
        player1.isContact = False

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop2 > 0:
        kunaiLoop2 += 1
    if kunaiLoop2 > 3:
        kunaiLoop2 = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais2:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player2.hitbox[1] + player2.hitbox[3] and kunai.y + kunai.radius > \
                    player2.hitbox[1]:
                if kunai.x + kunai.radius > player2.hitbox[0] and kunai.x - kunai.radius < player2.hitbox[0] + \
                        player2.hitbox[2]:
                    if player2.isBlock:
                        print("Bloqué !!")
                        kunais2.pop(kunais2.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        if player2.characterNumber == 3 and player2.spell1:
                            print("Dodged")
                        else:
                            player2.hit(2)
                            player1.dealable = False
                            player1Score += 1
                            if not player1.awaken:
                                if player1.awakening < 200:
                                    player1.awakening += 20
                            kunais2.pop(kunais2.index(kunai))

        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais2.pop(kunais2.index(kunai))

    # Kunai Throw --> Player 1 (F)
    if keys[pygame.K_f] and kunaiLoop2 == 0:
        player1.throw = True
        if soundActivated:
            kunaiSound.play()
        if player1.facingLeft:
            facing = -1
        elif player1.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais2) < 3:
            if facing == 1:
                kunais2.append(projectile(round(player1.x + player1.width // 2), round(player1.y + 10 + player1.height // 4),6, (0, 0, 0), facing))
            else:
                kunais2.append(projectile(round(player1.x), round(player1.y + player1.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop2 = 1

    # Left Movement --> Player 1 (Q)
    elif keys[pygame.K_q] and player1.x > player1.vel and not player1.transforming and not player1.spell1:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False
        player1.standing = False
        player1.standingLeft = False
        player1.standingRight = False
        player1.facingLeft = True
        player1.facingRight = False
        player1.isBlock = False
        player1.combo1 = False
        player1.throw = False
        player1.spell1 = False

    # Right Movement --> Player 1 (D)
    elif keys[pygame.K_d] and player1.x < 700 - player1.width - player1.vel and not player1.transforming and not player1.spell1:
        player1.x += player1.vel
        player1.right = True
        player1.left = False
        player1.standing = False
        player1.standingLeft = False
        player1.standingRight = False
        player1.facingLeft = False
        player1.facingRight = True
        player1.isBlock = False
        player1.combo1 = False
        player1.throw = False
        player1.spell1 = False

    # Down Movement --> Player 1 (S)
    elif keys[pygame.K_s] and not player1.transforming and not player1.spell1:
        player1.isBlock = True

    # Gain Mana --> Player 1 (H)
    elif keys[pygame.K_h] and not player1.transforming and not player1.spell1:
        if player1.mana < 200:
            player1.mana += 2.25
            player1.molding = True

    elif player1.spell1:
        if nextAnim:
            if player1.isContact:
                if player1.dealable:
                    if player2.characterNumber == 3 and player2.spell1:
                        print("Dodged")
                    else:
                        player2.hit(5)
                        player1.spell1 = False
                        player1.dealable = False
                        nextAnim = False
    else:
        player1.standing = True
        player1.isBlock = False
        player1.walkCount = 0

    # Combo 1 --> Damages
    if player1.isContact:
        if player1.combo1:
            if player1.dealable:
                if player1.characterNumber == 3 and player1.spell1:
                    print("Dodged")
                else:
                    player2.hit(5)
                    player1.dealable = False
                    player1Score += 1
                    if player1.awakening < 200:
                        player1.awakening += 20
        else:
            player1Score = player1Score

    # Jump Movement --> Player 1 (Z)
    if not player1.isJumping:
        if keys[pygame.K_z] and not player1.transforming and not player1.spell1:
            player1.isJumping = True
            player1.isBlock = False
            player1.walkCount = 0
    else:
        if player1.jumpCount >= -10:
            neg = 1
            if player1.jumpCount < 0:
                player1.isFalling = True
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1
        else:
            player1.isJumping = False
            player1.jumpCount = 10
            player1.isFalling = False

    # ////////////// Player 2 //////////////

    if player2.hitbox[1] < player1.hitbox[1] + player1.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > \
            player1.hitbox[1] and player2.hitbox[0] + player2.hitbox[2] > player1.hitbox[0] and player2.hitbox[0] < \
            player1.hitbox[0] + player1.hitbox[2]:
        player2.isContact = True
    else:
        player2.isContact = False

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop > 0:
        kunaiLoop += 1
    if kunaiLoop > 3:
        kunaiLoop = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player1.hitbox[1] + player1.hitbox[3] and kunai.y + kunai.radius > \
                    player1.hitbox[1]:
                if kunai.x + kunai.radius > player1.hitbox[0] and kunai.x - kunai.radius < player1.hitbox[0] + \
                        player1.hitbox[2]:
                    if player1.isBlock:
                        print("Bloqué !!")
                        kunais.pop(kunais.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        if player1.characterNumber == 3 and player1.spell1:
                            print("Dodged")
                        else:
                            player1.hit(5)
                            player2Score += 1
                            if not player2.awaken:
                                if player2.awakening < 200:
                                    player2.awakening += 20
                            kunais.pop(kunais.index(kunai))

    for kunai in kunais:
        for kunai2 in kunais2:
            if 670 > kunai.x > 0:
                if 670 > kunai.x > 0:
                    if kunai.y - kunai.radius < kunai2.hitbox[1] + kunai2.hitbox[3] and kunai.y + kunai.radius > \
                            kunai2.hitbox[1]:
                        if kunai.x + kunai.radius > kunai2.hitbox[0] and kunai.x - kunai.radius < kunai2.hitbox[0] + \
                                kunai2.hitbox[2]:
                            kunais.pop(kunais.index(kunai))
                            kunais2.pop(kunais2.index(kunai2))

        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais.pop(kunais.index(kunai))

    # Kunai Throw --> Player 2 (I)
    if keys[pygame.K_i] and kunaiLoop == 0:
        player2.throw = True
        if soundActivated:
            kunaiSound.play()
        if player2.facingLeft:
            facing = -1
        elif player2.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais) < 3:
            if facing == 1:
                kunais.append(projectile(round(player2.x + player2.width // 2), round(player2.y + player2.height // 4), 6, (0, 0, 0),  facing))
            else:
                kunais.append(projectile(round(player2.x), round(player2.y + player2.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop = 1

    # Left Movement --> Player 2 (Left)
    elif keys[pygame.K_LEFT] and player2.x > player2.vel:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False
        player2.standingLeft = False
        player2.standingRight = False
        player2.facingLeft = True
        player2.facingRight = False
        player2.isBlock = False
        player2.combo1 = False
        player2.throw = False

    # Right Movement --> Player 2 (Right)
    elif keys[pygame.K_RIGHT] and player2.x < 700 - player2.width - player2.vel:
        player2.x += player2.vel
        player2.right = True
        player2.left = False
        player2.standing = False
        player2.standingLeft = False
        player2.standingRight = False
        player2.facingLeft = False
        player2.facingRight = True
        player2.isBlock = False
        player2.combo1 = False
        player2.throw = False

    # Down Movement --> Player 2 (Down)
    elif keys[pygame.K_DOWN]:
        player2.isBlock = True

    # Gain Mana --> Player 2 (P)
    elif keys[pygame.K_p]:
        if player2.mana < 200:
            player2.mana += 2.25
            player2.molding = True

    elif player2.spell1:
        if nextAnim2:
            if player2.isContact:
                if player2.dealable:
                    player1.hit(5)
                    player2.spell1 = False
                    player2.dealable = False
                    nextAnim2 = False
    else:
        player2.standing = True
        player2.isBlock = False
        player2.walkCount = 0

    # Combo 1 --> Damages
    if player2.isContact:
        if player2.combo1:
            if player2.dealable:
                if player2.characterNumber == 3 and player2.spell1:
                    print("Dodged")
                else:
                    player1.hit(5)
                    player2.dealable = False
                    player2Score += 1
                    if player2.awakening < 200:
                        player2.awakening += 20
        else:
            player1Score = player1Score

    # Jump Movement --> Player 2 (Up)
    if not player2.isJumping:
        if keys[pygame.K_UP]:
            player2.isJumping = True
            player2.isBlock = False
            player2.walkCount = 0
    else:
        if player2.jumpCount >= -10:
            neg = 1
            if player2.jumpCount < 0:
                player2.isFalling = True
                neg = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
            player2.jumpCount -= 1
        else:
            player2.isJumping = False
            player2.jumpCount = 10
            player2.isFalling = False

    '''if keys[pygame.K_x]:
        playerSelect = False
        launchGame = True

    if keys[pygame.K_w]:
        launchGame = True

    if playerSelect:
        pygame.draw.rect(win, blue_mana, rect1)
        pygame.draw.rect(win, green, rect2)
        pygame.display.flip()

    if launchGame:'''

    redrawGameWindow()

pygame.quit()
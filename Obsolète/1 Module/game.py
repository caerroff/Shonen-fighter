from tkinter import *
import pygame, time
#from gui import *

#Création de la fênetre de lancement du jeu
main = Tk()
main.title("Shonen Fighter")
main.geometry("1023x682")
main.minsize(1023, 682)
main.maxsize(1023, 682)

musicActivated = False

def settings():
    frameSettings = Frame(main, bg="grey", width=450, height=450, bd=3, relief=SUNKEN)
    frameSettings.place(relx=0.25, rely=0.1, anchor=N)

    buttonClose = Button(frameSettings, text="Fermer",bg="lightgrey", font=("Helvetica", 10), width=15, command=frameSettings.destroy)
    buttonClose.place(relx=0.66, rely=0.9)

def playMusic():
    pygame.mixer.music.load('naruto_theme.mp3')
    pygame.mixer.music.play(-1)

def musicFunction():
    global musicActivated
    musicActivated = True

def selectCharacter():
    global winSelect
    main.destroy()

    winSelect = Tk()
    winSelect.title("Shonen Fighter - Select Character")
    winSelect.geometry("1023x682")
    winSelect.minsize(1023, 682)
    winSelect.maxsize(1023, 682)

    buttonPlay = Button(winSelect, text='Play', bg='lightgrey', font=("Helvetica", 10), width=15, command=launchGame)
    buttonPlay.place(relx=0.8, rely=0.7)

    buttonMusic = Button(winSelect, text='Music', bg='lightgrey', font=("Helvetica", 10), width=15, command=musicFunction)
    buttonMusic.place(relx=0.5, rely=0.7)

    winSelect.mainloop()

#global launched
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

#///////////// PYGAME

pygame.init()
pygame.font.init()

win_res = (700, 400)
win = pygame.display.set_mode(win_res)
pygame.display.set_caption("Shonen Fighter")
walkRight = [pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"), pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"), pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png"),
             pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"), pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"), pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png")]
walkLeft = [pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False), pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False), pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False),
            pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False), pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False), pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False)]
spritesJump = [pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png")]
spritesJumpLeft = [pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False),
                   pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False),
                   pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False), pygame.transform.flip(spritesJump[0], True, False)]
block = [pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png")]
blockLeft = [pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False),
             pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False),
             pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False), pygame.transform.flip(block[0], True, False)]
combo1 = [pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png")]
combo1Left = [pygame.transform.flip(combo1[0], True, False), pygame.transform.flip(combo1[1], True, False), pygame.transform.flip(combo1[2], True, False),
              pygame.transform.flip(combo1[2], True, False), pygame.transform.flip(combo1[2], True, False), pygame.transform.flip(combo1[2], True, False),
              pygame.transform.flip(combo1[2], True, False), pygame.transform.flip(combo1[2], True, False), pygame.transform.flip(combo1[2], True, False)]
bg = pygame.image.load("bg.jpg")
narutoSprite = pygame.image.load("naruto_2.png")
narutoSpriteLeft = pygame.transform.flip(narutoSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)

clock = pygame.time.Clock()

'''
soundActivated = False
musicActivated = False

def soundsFunction():
    global kunaiSound, kunaiImpactSound
    kunaiSound = pygame.mixer.Sound("kunai_flying.wav")
    kunaiImpactSound = pygame.mixer.Sound("kunai_impact.wav")

def musicFunction():
    global music
    music = pygame.mixer.music.load('naruto_theme.mp3')
    pygame.mixer.music.play(-1)
'''

font = pygame.font.Font("Helvetica.ttf", 30) #Font importé pour le score
narutoScore = 0
player2Score = 0

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

class Player(object):
    def __init__(self, x, y, width, height, playerNumber):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.isBlock = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.combo1 = False
        self.comboCount = 1
        self.standing = True
        self.standingRight = False
        self.standingLeft = False
        self.facingLeft = False
        self.facingRight = False
        self.hitbox = (self.x, self.y, 47, 60)
        self.health = 100
        self.playerNumber = playerNumber
        self.isContact = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                if self.isJump:
                    win.blit(spritesJumpLeft[self.jumpCount // 3], (self.x, self.y))
                else:
                    win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                if self.isJump:
                    win.blit(spritesJump[self.jumpCount // 3], (self.x, self.y))
                else:
                    win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.isBlock:
            if self.left:
                #self.isBlock = True
                win.blit(blockLeft[self.walkCount // 3], (self.x, self.y))
            elif self.right:
                win.blit(block[self.walkCount // 3], (self.x, self.y))
                #self.isBlock = True
            else:
                win.blit(block[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            #self.isBlock = False
        elif self.combo1:
            if self.facingRight:
                win.blit(combo1[self.walkCount // 3], (self.x, self.y))
            elif self.facingLeft:
                win.blit(combo1Left[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.combo1 = False
        elif self.isJump:
            if self.facingRight:
                win.blit(spritesJump[self.jumpCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.facingLeft:
                win.blit(spritesJumpLeft[self.jumpCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.playerNumber == 1:
            if self.right:
                win.blit(narutoSprite, (self.x, self.y))
                self.facingRight = True
            elif self.left:
                win.blit(narutoSpriteLeft, (self.x, self.y))
                self.facingLeft = True
            else:
                win.blit(narutoSprite, (self.x, self.y))
        elif self.playerNumber == 2:
            if self.right:
                win.blit(narutoSprite, (self.x, self.y))
            elif self.left:
                win.blit(narutoSpriteLeft, (self.x, self.y))
            else:
                win.blit(narutoSpriteLeft, (self.x, self.y))
        else:
            if self.right:
                win.blit(narutoSprite, (self.x, self.y))
                self.standingRight = True
            elif self.left:
                win.blit(narutoSpriteLeft, (self.x, self.y))
                self.standingLeft = True
            else:
                win.blit(narutoSprite, (self.x, self.y))
                self.standingRight = True

        if self.playerNumber == 1: # Jauge de vie du Joueur 1
            pygame.draw.rect(win, red, (20, 22, 200, 10))
            pygame.draw.rect(win, green, (20, 22, 200 - (2 * (100 - self.health)), 10))
        if self.playerNumber == 2: # Jauge de vie du Joueur 2
            pygame.draw.rect(win, red, (475, 22, 200, 10))
            pygame.draw.rect(win, green, (475, 22, 200 - (2 * (100 - self.health)), 10))

        self.hitbox = (self.x, self.y, 47, 60)
        pygame.draw.rect(win, blue, self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
            print("Touché !", "Hp : ", self.health)

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 15 * facing

    def draw(self, win):
        if facing == 1:
            win.blit(kunaiSprite, (self.x, self.y))
        else:
            win.blit(kunaiSpriteLeft, (self.x, self.y))

def redrawGameWindow(): #Toutes les modifications visuelles se feront ici et plus dans la boucle principale
    win.blit(bg, (-3, 0))  # Black
    text = font.render("Score :" + str(narutoScore), 1, (0, 0, 0))
    win.blit(text, (100, 55))
    text = font.render("Score :" + str(player2Score), 1, (0, 0, 0))
    win.blit(text, (400, 55))
    naruto.draw(win)
    player2.draw(win)
    for kunai in kunais:
        kunai.draw(win)
    for kunai in kunais2:
        kunai.draw(win)
    pygame.display.update()

#MAINLOOP
naruto = Player(100, 300, 64, 64, 1)
naruto.facingRight = True
player2 = Player(550, 300, 64, 64, 2)
player2.facingLeft = True
kunais = [] # Liste des Kunais --> Joueur 1
kunaiLoop = 0 # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 1
kunais2 = [] # Liste des Kunais --> Joueur 2
kunaiLoop2 = 0 # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 2
while launched:
    clock.tick(27)

    # Permet de quitter le jeu avec la croix ou le bouton entrer
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False

    if musicActivated:
        print("Iyi")
        playMusic()


    if naruto.hitbox[1] < player2.hitbox[1] + player2.hitbox[3] and naruto.hitbox[1] + naruto.hitbox[3] > player2.hitbox[1] and naruto.hitbox[0] + naruto.hitbox[2] > player2.hitbox[0] and naruto.hitbox[0] < player2.hitbox[0] + player2.hitbox[2]:
        naruto.isContact = True
    else:
        naruto.isContact = False

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop > 0:
        kunaiLoop += 1
    if kunaiLoop > 3:
        kunaiLoop = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player2.hitbox[1] + player2.hitbox[3] and kunai.y + kunai.radius > player2.hitbox[1]:
                if kunai.x + kunai.radius > player2.hitbox[0] and kunai.x - kunai.radius < player2.hitbox[0] + player2.hitbox[2]:
                    if player2.isBlock:
                        print("Bloqué !!")
                        kunais.pop(kunais.index(kunai))
                    else:
                        #if soundActivated:
                        #    kunaiImpactSound.play()
                        player2.hit()
                        narutoScore += 1
                        kunais.pop(kunais.index(kunai))
        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais.pop(kunais.index(kunai))

    # Variable permettant de vérifier si une touché est pressée
    keys = pygame.key.get_pressed()

    soundActivated = False

    if keys[pygame.K_b]:
        soundActivated = True
        soundsFunction()

    if keys[pygame.K_n]:
        if soundActivated:
            soundActivated = False
            pygame.mixer.music.stop()
            #soundsFunction()

    # Kunai Throw --> I (Player 1)
    if keys[pygame.K_i] and kunaiLoop == 0:
        if soundActivated:
            kunaiSound.play()
        if naruto.facingLeft:
            facing = -1
        elif naruto.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais) < 3:
            if facing == 1:
                kunais.append(projectile(round(naruto.x + naruto.width // 2), round(naruto.y + naruto.height //4), 6, (0, 0, 0), facing))
            else:
                kunais.append(projectile(round(naruto.x), round(naruto.y + naruto.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop = 1

    # Left Movement --> Player 1 (Left)
    elif keys[pygame.K_LEFT] and naruto.x > naruto.vel:
        naruto.x -= naruto.vel
        naruto.left = True
        naruto.right = False
        naruto.standing = False
        naruto.standingLeft = False
        naruto.standingRight = False
        naruto.facingLeft = True
        naruto.facingRight = False
        naruto.isBlock = False
        naruto.combo1 = False

    # Right Movement --> Player 1 (Right)
    elif keys[pygame.K_RIGHT] and naruto.x < 700 - naruto.width - naruto.vel:
        naruto.x += naruto.vel
        naruto.right = True
        naruto.left = False
        naruto.standing = False
        naruto.standingLeft = False
        naruto.standingRight = False
        naruto.facingLeft = False
        naruto.facingRight = True
        naruto.isBlock = False
        naruto.combo1 = False

    # Down Movement --> Player 1 (Down)
    elif keys[pygame.K_DOWN]:
        naruto.isBlock = True

    # Combo 1 Movement --> Player 1 (O) ---> Objectif : Interrompre la marche pour utiliser le combo
    elif keys[pygame.K_o]:
        naruto.combo1 = True
    else:
        naruto.standing = True
        naruto.isBlock = False
        naruto.walkCount = 0

    #Combo 1 --> Damages
    if naruto.isContact:
        if naruto.combo1:
            print("Dégâts Sur Combo")
            player2.hit()
            narutoScore += 1

    # Jump Movement --> Player 1 (Space)
    if not naruto.isJump:
        if keys[pygame.K_UP]:
            naruto.isJump = True
            naruto.isBlock = False
            naruto.walkCount = 0
    else:
        if naruto.jumpCount >= -10:
            neg = 1
            if naruto.jumpCount < 0:
                neg = -1
            naruto.y -= (naruto.jumpCount ** 2) * 0.5 * neg
            naruto.jumpCount -= 1

        else:
            naruto.isJump = False
            naruto.jumpCount = 10

    # ////////////// Player 2 //////////////

    # Hitbox collision --> Pour Combo
    if soundActivated:
        if player2.hitbox[1] < naruto.hitbox[1] + naruto.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > \
                naruto.hitbox[1]:
            if player2.hitbox[0] + player2.hitbox[2] > naruto.hitbox[0] and player2.hitbox[0] < naruto.hitbox[0] + \
                    naruto.hitbox[2]:
                pass
                #naruto.hit()
                #player2Score += 1

    # Permet de faire fonctionner la kunaiLoop2, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop2 > 0:
        kunaiLoop2 += 1
    if kunaiLoop2 > 3:
        kunaiLoop2 = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais2:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < naruto.hitbox[1] + naruto.hitbox[3] and kunai.y + kunai.radius > naruto.hitbox[1]:
                if kunai.x + kunai.radius > naruto.hitbox[0] and kunai.x - kunai.radius < naruto.hitbox[0] +naruto.hitbox[2]:
                    if naruto.isBlock:
                        print("Bloqué !!")
                        kunais2.pop(kunais2.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        naruto.hit()
                        player2Score += 1
                        kunais2.pop(kunais2.index(kunai))
        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais2.pop(kunais2.index(kunai))

    # Kunai Throw --> F (Player 2)
    if keys[pygame.K_f] and kunaiLoop2 == 0:
        # kunaiSound.play()
        if player2.facingLeft:
            facing = -1
        elif player2.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais2) < 3:
            if facing == 1:
                kunais2.append(
                    projectile(round(player2.x + player2.width // 2), round(player2.y + player2.height // 4), 6,
                               (0, 0, 0), facing))
            else:
                kunais2.append(
                    projectile(round(player2.x), round(player2.y + player2.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop2 = 1

    # Left Movement --> Player 2 (Q)
    if keys[pygame.K_q] and player2.x > player2.vel:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False
        player2.standingLeft = False
        player2.standingRight = False
        player2.facingLeft = True
        player2.facingRight = False

    # Right Movement --> Player 2 (D)
    elif keys[pygame.K_d] and player2.x < 700 - player2.width - player2.vel:
        player2.x += player2.vel
        player2.right = True
        player2.left = False
        player2.standing = False
        player2.standingLeft = False
        player2.standingRight = False
        player2.facingLeft = False
        player2.facingRight = True

    # Down Movement --> Player 2 (S)
    elif keys[pygame.K_s]:
        player2.isBlock = True

    # Combo 1 Movement --> Player 2 (G)
    elif keys[pygame.K_g]:
        player2.combo1 = True
    else:
        player2.standing = True
        player2.isBlock = False
        player2.walkCount = 0

    # Jump Movement --> Player 2 (Z)
    if not player2.isJump:
        if keys[pygame.K_z]:
            player2.isJump = True
            player2.isBlock = False
            player2.walkCount = 0
    else:
        if player2.jumpCount >= -10:
            neg = 1
            if player2.jumpCount < 0:
                neg = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
            player2.jumpCount -= 1

        else:
            player2.isJump = False
            player2.jumpCount = 10

    redrawGameWindow()

pygame.quit()
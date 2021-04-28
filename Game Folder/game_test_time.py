# -*- coding: utf-8 -*-
import pygame, time
from perso_os import *
# from gui import *

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
player1Score = 0
player2Score = 0

rect1 = pygame.Rect(250, 70, 65, 65)  # Constructeur d'objet --> Rectangle, Arg: x, y, w, h
rect2 = pygame.Rect(350, 70, 65, 65)  # Constructeur d'objet --> Rectangle, Arg: x, y, w, h

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (109, 111, 111)
blue_mana = (0, 186, 240)
yellow = (255, 232, 1)

kunaiSpriteRight = pygame.image.load('../Sprite/Kunai/sprite.png')
kunaiSpriteLeft = pygame.transform.flip(kunaiSpriteRight, True, False)
bg = pygame.image.load('../Sprite/bg.jpg')

class Player(object):
    def __init__(self, x, y, width, height, playerNumber):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.isFalling = False
        self.isBlock = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.combo1 = False
        self.throw = False
        self.spell1 = False
        self.isSpell1 = True
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
        self.mana = 0
        self.molding = False
        self.awakening = 200
        self.awaken = False
        self.transforming = False
        self.isContact = False
        self.playerNumber = playerNumber
        self.current_sprite = 0

    def animator(self, list, increm, iter = 0):
        if iter == 1:
            if self.current_sprite >= len(list):
                self.spell1 = False
            else:
                win.blit(list[int(self.current_sprite)], (self.x, self.y))
                self.current_sprite += increm
        else:
            if self.current_sprite >= len(list):
                self.current_sprite = 0
            win.blit(list[int(self.current_sprite)], (self.x, self.y))
            self.current_sprite += increm

    def doubleAnimation(self, listA, listB, increm = 1, increm2 = 0.35):
        nextAnim = False
        if self.current_sprite < len(listA):
            win.blit(listA[int(self.current_sprite)], (self.x, self.y))
            self.current_sprite += increm
        else:
            nextAnim = True
        if nextAnim:
            if self.current_sprite >= len(listA):
                if self.current_sprite >= len(listB):
                    self.spell1 = False
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
                        self.dealable = False

    def draw_ath(self, win):
        if self.playerNumber == 1:  # Jauge de vie du Joueur 1
            pygame.draw.rect(win, red, (20, 22, 200, 10))
            pygame.draw.rect(win, green, (20, 22, 200 - (2 * (100 - self.health)), 10))
            pygame.draw.rect(win, grey, (20, 35, 200, 10))
            pygame.draw.rect(win, blue_mana, (20, 35, 0 + self.mana, 10))
            pygame.draw.rect(win, grey, (20, 50, 200, 10))
            pygame.draw.rect(win, yellow, (20, 50, 0 + self.awakening, 10))

        if self.playerNumber == 2:  # Jauge de vie du Joueur 2
            pygame.draw.rect(win, red, (475, 22, 200, 10))
            pygame.draw.rect(win, green, (475, 22, 200 - (2 * (100 - self.health)), 10))
            pygame.draw.rect(win, grey, (475, 35, 200, 10))
            pygame.draw.rect(win, blue_mana, (475, 35, 0 + self.mana, 10))
            pygame.draw.rect(win, grey, (475, 50, 200, 10))
            pygame.draw.rect(win, yellow, (475, 50, 0 + self.awakening, 10))

    def draw_naruto(self, win):
        if not self.standing:
            if self.left:
                if self.isJump and self.isFalling:
                    self.animator(Naruto['FallingLeft'], 1)
                elif self.isJump:
                    self.animator(Naruto['JumpingLeft'], 0.3)
                else:
                    self.animator(Naruto['RunLeft'], 0.5)
            elif self.right:
                if self.isJump and self.isFalling:
                    self.animator(Naruto['FallingRight'], 1)
                elif self.isJump:
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
        elif self.isJump:
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
            if self.left:
                self.animator(Naruto['StandLeft'], 1)
                self.facingLeft = True
            else:
                self.animator(Naruto['StandRight'], 1)
        elif self.playerNumber == 2:
            if self.right:
                self.animator(Naruto['StandRight'], 1)
                self.facingRight = True
            elif self.left:
                self.animator(Naruto['StandLeft'], 1)
                self.facingLeft = True
            else:
                self.animator(Naruto['StandLeft'], 1)
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
            self.hitbox = (self.x, self.y, 47, 60)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        else:
            self.hitbox = (self.x, self.y, 65, 80)
            pygame.draw.rect(win, red, self.hitbox, 2)

    def draw_sasuke(self, win):
        if not self.awaken:
            if not self.standing:
                if self.left:
                    if self.isJump and self.isFalling:
                        self.animator(Sasuke['FallingLeft'], 1)
                    elif self.isJump:
                        self.animator(Sasuke['JumpingLeft'], 0.3)
                    else:
                        self.animator(Sasuke['RunLeft'], 0.5)
                elif self.right:
                    if self.isJump and self.isFalling:
                        self.animator(Sasuke['FallingRight'], 1)
                    elif self.isJump:
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
                    self.animator(Sasuke['Combo1Right'], 0.4)
                elif self.facingLeft:
                    self.animator(Sasuke['Combo1Left'], 0.4)
                self.combo1 = False
            elif self.throw:
                if self.facingRight:
                    self.animator(Sasuke['ThrowRight'], 1)
                if self.facingLeft:
                    self.animator(Sasuke['ThrowLeft'], 1)
                self.throw = False
            elif self.spell1:
                if self.facingRight:
                    self.doubleAnimation(Sasuke['Spell1ChargeRight'], Sasuke['Spell1AttackRight'], 1, 0.05)
                if self.facingLeft:
                    self.doubleAnimation(Sasuke['Spell1ChargeLeft'], Sasuke['Spell1AttackLeft'], 1, 0.05)
                self.spell1 = False
            elif self.spell2:
                if self.facingRight:
                    self.doubleAnimation(Sasuke['Spell2Right'], Sasuke['EffectRight'], 0.5, 0.5)
                if self.facingLeft:
                    self.doubleAnimation(Sasuke['Spell2Left'], Sasuke['EffectLeft'], 0.5, 0.5)
                self.spell2 = False
            elif self.molding:
                if self.facingRight:
                    self.animator(Sasuke['MoldingRight'], 1, 0.2)
                if self.facingLeft:
                    self.animator(Sasuke['MoldingLeft'], 1, 0.2)
                self.molding = False
            elif self.isJump:
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
            elif self.playerNumber == 1:
                if self.right:
                    self.animator(Naruto['StandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Naruto['StandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Naruto['StandRight'], 1)
            elif self.playerNumber == 2:
                if self.right:
                    self.animator(Sasuke['StandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['StandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['StandLeft'], 1)
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
        if self.transforming:
            if self.facingRight:
                self.animator(Sasuke['AwakeningRight'], 0.2)
            if self.facingLeft:
                self.animator(Sasuke['AwakeningLeft'], 0.2)
            self.transforming = False
            self.awaken = True
        if self.awaken:
            if not self.standing:
                if self.left:
                    if self.isJump and self.isFalling:
                        self.animator(Sasuke['AwakeFallingLeft'], 1)
                    elif self.isJump:
                        self.animator(Sasuke['AwakeJumpingLeft'], 0.3)
                    else:
                        self.animator(Sasuke['AwakeRunLeft'], 0.2)
                elif self.right:
                    if self.isJump and self.isFalling:
                        self.animator(Sasuke['AwakeFallingRight'], 1)
                    elif self.isJump:
                        self.animator(Sasuke['AwakeJumpingRight'], 0.3)
                    else:
                        self.animator(Sasuke['AwakeRunRight'], 0.2)
            elif self.isBlock:
                if self.left or self.facingLeft:
                    self.animator(Sasuke['AwakeBlockLeft'], 1)
                elif self.right or self.facingRight:
                    self.animator(Sasuke['AwakeBlockRight'], 1)
                else:
                    self.animator(Sasuke['AwakeBlockRight'], 1)
            elif self.combo1:
                if self.facingRight:
                    self.animator(Sasuke['AwakeCombo1Right'], 0.4)
                elif self.facingLeft:
                    self.animator(Sasuke['AwakeCombo1Left'], 0.4)
                self.combo1 = False
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
                self.spell1 = False
            elif self.molding:
                if self.facingRight:
                    self.animator(Sasuke['AwakeMoldingRight'], 0.2)
                if self.facingLeft:
                    self.animator(Sasuke['AwakeMoldingLeft'], 0.2)
                self.molding = False
            elif self.isJump:
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
                    self.animator(Naruto['AwakeStandRight'], 1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Naruto['AwakeStandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Naruto['AwakeStandRight'], 1)
            elif self.playerNumber == 2:
                if self.right:
                    self.animator(Sasuke['AwakeStandRight'], 0.1)
                    self.facingRight = True
                elif self.left:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
                    self.facingLeft = True
                else:
                    self.animator(Sasuke['AwakeStandLeft'], 1)
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
        if not self.awaken:
            self.hitbox = (self.x, self.y, 47, 60)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        else:
            self.hitbox = (self.x, self.y, 65, 80)
            pygame.draw.rect(win, red, self.hitbox, 2)


    def hit(self, damages):
        if self.health > 0:
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
        self.hitbox = (self.x, self.y, 20, 15)

    def draw(self, win):
        if facing == 1:
            win.blit(kunaiSpriteRight, (self.x, self.y))
            self.hitbox = (self.x, self.y, 20, 15)
            pygame.draw.rect(win, blue, self.hitbox, 2)
        else:
            win.blit(kunaiSpriteLeft, (self.x, self.y))
            self.hitbox = (self.x, self.y, 20, 15)
            pygame.draw.rect(win, blue, self.hitbox, 2)

def redrawGameWindow():  # Toutes les modifications visuelles se feront ici et plus dans la boucle principale
    win.blit(bg, (-3, 0))  # Black
    score1 = font.render("Score :" + str(player1Score), 1, (0, 0, 0))
    win.blit(score1, (20, 65))
    score2 = font.render("Score :" + str(player2Score), 1, (0, 0, 0))
    win.blit(score2, (565, 65))
    player1.draw_naruto(win)
    player1.draw_ath(win)
    player2.draw_sasuke(win)
    player2.draw_ath(win)
    for kunai in kunais:
        kunai.draw(win)
    for kunai in kunais2:
        kunai.draw(win)
    pygame.display.update()

# MAINLOOP
player1 = Player(100, 300, 64, 64, 1)
player1.facingRight = True
player2 = Player(550, 300, 64, 64, 2)
player2.facingLeft = True
kunais = []  # Liste des Kunais --> Joueur 1
kunaiLoop = 0  # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 1
kunais2 = []  # Liste des Kunais --> Joueur 2
kunaiLoop2 = 0  # Permet d'ajouter un "Cooldown" aux kunais, un seul peut être lancer à la fois --> Joueur 2
launched = True
playerSelect = True
launchGame = False

current_time = 0
button_press_time = False

while launched:
    clock.tick(27)
    current_time = pygame.time.get_ticks()

    if current_time - button_press_time > 2000:
        player2.isSpell1 = True
    else:
        player2.isSpell1 = False

    print(current_time)
    print(button_press_time)

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

    # ////////////// Player 1 //////////////

    if player1.hitbox[1] < player2.hitbox[1] + player2.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > \
            player2.hitbox[1] and player1.hitbox[0] + player1.hitbox[2] > player2.hitbox[0] and player1.hitbox[0] < \
            player2.hitbox[0] + player2.hitbox[2]:
        player1.isContact = True
    else:
        player1.isContact = False

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop > 0:
        kunaiLoop += 1
    if kunaiLoop > 3:
        kunaiLoop = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player2.hitbox[1] + player2.hitbox[3] and kunai.y + kunai.radius > \
                    player2.hitbox[1]:
                if kunai.x + kunai.radius > player2.hitbox[0] and kunai.x - kunai.radius < player2.hitbox[0] + \
                        player2.hitbox[2]:
                    if player2.isBlock:
                        print("Bloqué !!")
                        kunais.pop(kunais.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        player2.hit(5)
                        player1Score += 1
                        if not player1.awaken:
                            if player1.awakening < 200:
                                player1.awakening += 1
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

    # Kunai Throw --> I (Player 1)
    if keys[pygame.K_i] and kunaiLoop == 0:
        player1.throw = True
        if soundActivated:
            kunaiSound.play()
        if player1.facingLeft:
            facing = -1
        elif player1.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais) < 3:
            if facing == 1:
                kunais.append(projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 4), 6, (0, 0, 0),  facing))
            else:
                kunais.append(projectile(round(player1.x), round(player1.y + player1.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop = 1

    # Left Movement --> Player 1 (Left)
    elif keys[pygame.K_LEFT] and player1.x > player1.vel:
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

    # Right Movement --> Player 1 (Right)
    elif keys[pygame.K_RIGHT] and player1.x < 700 - player1.width - player1.vel:
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

    # Down Movement --> Player 1 (Down)
    elif keys[pygame.K_DOWN]:
        player1.isBlock = True

    # Gain Mana --> Player 1 (P)
    elif keys[pygame.K_p]:
        if player1.mana < 200:
            player1.mana += 2.25
            player1.molding = True

    # Combo 1 Movement --> Player 1 (O) ---> Objectif : Interrompre la marche pour utiliser le combo
    elif keys[pygame.K_o]:
        player1.combo1 = True
    else:
        player1.standing = True
        player1.isBlock = False
        player1.walkCount = 0

    # Combo 1 --> Damages
    if player1.isContact:
        if player1.combo1:
            player2.hit(10)
            player1Score += 1
            if player1.awakening < 200:
                player1.awakening += 1
        else:
            player1Score = player1Score

    # Jump Movement --> Player 1 (Space)
    if not player1.isJump:
        if keys[pygame.K_UP]:
            player1.isJump = True
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
            player1.isJump = False
            player1.jumpCount = 10
            player1.isFalling = False

    # ////////////// Player 2 //////////////

    # Hitbox collision --> Pour Combo
    if player2.hitbox[1] < player1.hitbox[1] + player1.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > \
            player1.hitbox[1] and player2.hitbox[0] + player2.hitbox[2] > player1.hitbox[0] and player2.hitbox[0] < \
            player1.hitbox[0] + player1.hitbox[2]:
        player2.isContact = True
    else:
        player2.isContact = False

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop2> 0:
        kunaiLoop2+= 1
    if kunaiLoop2> 3:
        kunaiLoop2= 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais2:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player1.hitbox[1] + player1.hitbox[3] and kunai.y + kunai.radius > \
                    player1.hitbox[1]:
                if kunai.x + kunai.radius > player1.hitbox[0] and kunai.x - kunai.radius < player1.hitbox[0] + \
                        player1.hitbox[2]:
                    if player1.isBlock:
                        print("Bloqué !!")
                        kunais2.pop(kunais2.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        player1.hit(5)
                        player2Score += 1
                        if not player2.awaken:
                            if player2.awakening < 200:
                                player2.awakening += 100
                        kunais2.pop(kunais2.index(kunai))

        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais2.pop(kunais2.index(kunai))

    # Kunai Throw --> F (Player 2)
    if keys[pygame.K_f] and kunaiLoop2== 0:
        player2.throw = True
        if soundActivated:
            kunaiSound.play()
        if player2.facingLeft:
            facing = -1
        elif player2.facingRight:
            facing = 1
        else:
            facing = 1
        if len(kunais2) < 3:
            if facing == 1:
                kunais2.append(projectile(round(player2.x + player2.width // 2), round(player2.y + player2.height // 4), 6, (0, 0, 0), facing))
            else:
                kunais2.append(projectile(round(player2.x), round(player2.y + player2.height // 4), 6, (0, 0, 0), facing))
        kunaiLoop2= 1

    # Left Movement --> Player 2 (Q)
    elif keys[pygame.K_q] and player2.x > player2.vel:
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
        player2.spell1 = False

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
        player2.isBlock = False
        player2.combo1 = False
        player2.throw = False
        player2.spell1 = False

    # Down Movement --> Player 2 (S)
    elif keys[pygame.K_s]:
        player2.isBlock = True

    # Gain Mana --> Player 1 (H)
    elif keys[pygame.K_h]:
        if player2.mana < 200:
            player2.mana += 2.25
            player2.molding = True

    elif keys[pygame.K_c]:
        button_press_time = pygame.time.get_ticks()
        if player2.isSpell1:
            player2.spell1 = True
            if player2.isContact:
                if player2.dealable:
                    player1.hit(1)

    #elif current_time - button_press_time > 2000:
    #    player2.isSpell1 = False
    #elif current_time - button_press_time <= 2000:
    #   player2.isSpell1 = False

    # Transforming
    elif keys[pygame.K_w]:
        if player2.awakening >= 200:
            player2.transforming = True
            player2.y -= 15
            player2.awakening = 0

    # Test Katon
    elif keys[pygame.K_x]:
        player2.spell2 = True

    # Combo 1 Movement --> Player 2 (G) ---> Objectif : Interrompre la marche pour utiliser le combo
    elif keys[pygame.K_g]:
        player2.combo1 = True
    else:
        player2.standing = True
        player2.isBlock = False
        player2.walkCount = 0

    # Combo 1 --> Damages
    if player2.isContact:
        if player2.combo1:
            player1.hit(10)
            player2Score += 1
            if player2.awakening < 200:
                player2.awakening += 1
        else:
            player2Score = player2Score

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
                player2.isFalling = True
                neg = -1
            player2.y -= (player2.jumpCount ** 2) * 0.5 * neg
            player2.jumpCount -= 1
        else:
            player2.isJump = False
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
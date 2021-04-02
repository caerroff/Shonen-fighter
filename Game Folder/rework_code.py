# -*- coding: utf-8 -*-
import pygame, time
from perso import *
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
        self.sasukeWalkCount = 0
        self.combo1 = False
        self.comboCount = 1
        self.throw = False
        self.throwCount = 0
        self.spell1 = False
        self.standing = True
        self.standingRight = False
        self.standingLeft = False
        self.facingLeft = False
        self.facingRight = False
        self.hitbox = (self.x, self.y, 47, 60)
        self.health = 100
        self.mana = 0
        self.awakening = 0
        self.isContact = False
        self.playerNumber = playerNumber
        self.current_sprite = 0

    def animator(self, liste, increm):
        win.blit(liste[int(self.current_sprite)], (self.x, self.y))
        self.current_sprite += increm
        if self.current_sprite >= len(liste):
            self.current_sprite = 0

    def draw_naruto(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.throwCount + 1 >= 27:
            self.throwCount = 0
        if not self.standing:
            if self.left:
                if self.isJump:
                    self.animator(NarutoJumpLeft, 1)
                else:
                    win.blit(NarutoWalkLeft[int(self.current_sprite)], (self.x, self.y))
                    self.current_sprite += 0.2
                    if self.current_sprite >= len(NarutoWalkLeft):
                        self.current_sprite = 0
                self.walkCount += 1
            elif self.right:
                if self.isJump:
                    win.blit(NarutoJumpRight[self.jumpCount // 3], (self.x, self.y))
                else:
                    win.blit(NarutoWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.isBlock:
            if self.left:
                # self.isBlock = True
                win.blit(NarutoBlockLeft[self.walkCount // 3], (self.x, self.y))
            elif self.right:
                win.blit(NarutoBlockRight[self.walkCount // 3], (self.x, self.y))
                # self.isNarutoBlockRight = True
            else:
                win.blit(NarutoBlockRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            # self.isNarutoBlockRight = False
        elif self.combo1:
            if self.facingRight:
                self.animator(NarutoCombo1Right, 0.4)
            elif self.facingLeft:
                win.blit(NarutoCombo1Left[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.combo1 = False
        elif self.throw:
            if self.facingRight:
                win.blit(NarutoKunaiThrowRight[self.walkCount // 3], (self.x, self.y))
            if self.facingLeft:
                win.blit(NarutoKunaiThrowLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.throw = False
        elif self.spell1:
            if self.facingRight:
                win.blit(NarutoSpell1Right[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.facingLeft:
                win.blit(NarutoSpell1Left[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.isJump:
            if self.facingRight:
                win.blit(NarutoJumpRight[self.jumpCount // 3], (self.x, self.y))
                self.walkCount += 1
            if self.facingLeft:
                win.blit(NarutoJumpLeft[self.jumpCount // 3], (self.x, self.y))
                self.walkCount += 1
        elif self.playerNumber == 1:
            if self.right:
                win.blit(NarutoSprite, (self.x, self.y))
                self.facingRight = True
            elif self.left:
                win.blit(NarutoSpriteLeft, (self.x, self.y))
                self.facingLeft = True
            else:
                win.blit(NarutoSprite, (self.x, self.y))
        elif self.playerNumber == 2:
            if self.right:
                win.blit(NarutoSprite, (self.x, self.y))
                self.facingRight = True
            elif self.left:
                win.blit(NarutoSpriteLeft, (self.x, self.y))
                self.facingLeft = True
            else:
                win.blit(NarutoSpriteLeft, (self.x, self.y))
        else:
            if self.right:
                win.blit(NarutoSprite, (self.x, self.y))
                self.standingRight = True
            elif self.left:
                win.blit(NarutoSpriteLeft, (self.x, self.y))
                self.standingLeft = True
            else:
                win.blit(NarutoSprite, (self.x, self.y))
                self.standingRight = True

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

        self.hitbox = (self.x, self.y, 47, 60)
        pygame.draw.rect(win, blue, self.hitbox, 2)

    def draw_sasuke(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.facingRight:
            win.blit(sasukeSprite, (self.x, self.y))
        if self.facingLeft:
            win.blit(sasukeSpriteLeft, (self.x, self.y))
        if not self.standing:
            if self.right:
                win.blit(SasukeWalkRight[self.walkCount // 3], (self.x, self.y))
            else:
                win.blit(sasukeSprite, (self.x, self.y))
            self.walkCount += 1

            '''elif self.right:
                win.blit(SasukeWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1'''

    def hit(self):
        if self.health > 0:
            self.health -= 1
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
            win.blit(kunaiSprite, (self.x, self.y))
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
    player2.draw_naruto(win)
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
while launched:
    clock.tick(27)

    # Permet de quitter le jeu avec la croix ou le bouton entrer
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False

    if player1.hitbox[1] < player2.hitbox[1] + player2.hitbox[3] and player1.hitbox[1] + player1.hitbox[3] > \
            player2.hitbox[1] and player1.hitbox[0] + player1.hitbox[2] > player2.hitbox[0] and player1.hitbox[0] < \
            player2.hitbox[0] + player2.hitbox[2]:
        player1.isContact = True
    else:
        player1.isContact = False

    ''''# Hitbox collision --> Pour Combo
    if player1.isContact:
        if player1.combo1:
            print("Dégâts Sur Combo")
            player2.hit()
            player1Score += 1
            player1.awakening += 1
        else:
            player1Score = player1Score'''

    # Permet de faire fonctionner la kunaiLoop, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop > 0:
        kunaiLoop += 1
    if kunaiLoop > 3:
        kunaiLoop = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais:
        # for kunai2 in kunais2:
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
                        player2.hit()
                        player1Score += 1
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
                            # while kunai.y > 300:
                            # print(kunai.y)
                            # print(kunai.distGround)
                            # kunai.y += 1
                            # kunai2.y += 1

        if 670 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais.pop(kunais.index(kunai))

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
                kunais.append(
                    projectile(round(player1.x + player1.width // 2), round(player1.y + player1.height // 4), 6, (0, 0, 0),
                               facing))
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

    # Test
    elif keys[pygame.K_p]:
        if player1.mana < 200:
            player1.mana += 2.25
        # player1.spell1 = True

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
            player2.hit()
            player1Score += 1
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
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1

        else:
            player1.isJump = False
            player1.jumpCount = 10

    # ////////////// Player 2 //////////////

    # Hitbox collision --> Pour Combo
    if soundActivated:
        if player1.hitbox[1] < player1.hitbox[1] + player1.hitbox[3] and player2.hitbox[1] + player2.hitbox[3] > \
                player1.hitbox[1]:
            if player2.hitbox[0] + player2.hitbox[2] > player1.hitbox[0] and player2.hitbox[0] < player1.hitbox[0] + \
                    player1.hitbox[2]:
                pass
                # player1.hit()
                # player2Score += 1

    # Permet de faire fonctionner la kunaiLoop2, fonctionne sur plusieurs itérations de la mainloop
    if kunaiLoop2 > 0:
        kunaiLoop2 += 1
    if kunaiLoop2 > 3:
        kunaiLoop2 = 0

    # Kunai collision --> Pour attaque avec kunai
    for kunai in kunais2:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < player1.hitbox[1] + player1.hitbox[3] and kunai.y + kunai.radius > player1.hitbox[
                1]:
                if kunai.x + kunai.radius > player1.hitbox[0] and kunai.x - kunai.radius < player1.hitbox[0] + \
                        player1.hitbox[2]:
                    if player1.isBlock:
                        print("Bloqué !!")
                        kunais2.pop(kunais2.index(kunai))
                    else:
                        if soundActivated:
                            kunaiImpactSound.play()
                        player1.hit()
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
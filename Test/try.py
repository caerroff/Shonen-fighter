import pygame, time
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
combo1 = [pygame.image.load("naruto_combo1.png"), pygame.image.load("naruto_combo2.png"), pygame.image.load("naruto_combo3.png"),
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

#kunaiSound = pygame.mixer.Sound("kunai_flying.wav")
#kunaiImpactSound = pygame.mixer.Sound("kunai_impact.wav")

#music = pygame.mixer.music.load('naruto_theme.mp3')
#pygame.mixer.music.play(-1)

font = pygame.font.Font("Helvetica.ttf", 30) #Font importé pour le score
score = 0

class Player(object):
    def __init__(self, x, y, width, height):
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
        self.hitbox = (self.x, self.y, 47, 60)
        self.health = 100

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
        elif self.isJump:
            win.blit(spritesJump[self.jumpCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isJump and self.right:
            win.blit(spritesJump[self.jumpCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif self.isBlock:
            if self.right:
                win.blit(blockLeft[self.walkCount // 3], (self.x, self.y))
            elif self.right:
                win.blit(block[self.walkCount // 3], (self.x, self.y))
            else:
                win.blit(block[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.isBlock = False
        elif self.combo1:
            if self.right:
                win.blit(combo1[self.walkCount // 3], (self.x, self.y))
            elif self.left:
                win.blit(combo1Left[self.walkCount // 3], (self.x, self.y))
            else:
                win.blit(combo1[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
            self.combo1 = False
        else:
            if self.right:
                win.blit(narutoSprite, (self.x, self.y))
            elif self.left:
                win.blit(narutoSpriteLeft, (self.x, self.y))
            else:
                win.blit(narutoSprite, (self.x, self.y))
        self.hitbox = (self.x, self.y, 47, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        if self.health > 0:
            self.health -= 10
            print("Hp : ", self.health)
            print("Touché")

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
    text = font.render("Score :" + str(score), 1, (0, 0, 0))
    win.blit(text, (570, 25))
    naruto.draw(win)
    player2.draw(win)
    for kunai in kunais:
        kunai.draw(win)
    pygame.display.update()

#MAINLOOP
naruto = Player(300, 300, 64, 64)
player2 = Player(500, 300, 64, 64)
shootLoop = 0 # "Timer" Kunai (Voir plus bas) --> Permet de ne pas tirer plusieurs kunai pile en même temps
kunais = [] #Kunaï --> Kunai --> Kunais

launched = True
while launched:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False

    if shootLoop > 0: # Permet de faire fonctionner la shootLoop
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for kunai in kunais:
        if 670 > kunai.x > 0:
                    #kunaiImpactSound.play()
                    score += 1
                    kunais.pop(kunais.index(kunai))
        if 665 > kunai.x > 0:
            kunai.x += kunai.vel
        else:
            kunais.pop(kunais.index(kunai))

    keys = pygame.key.get_pressed() #Variable permettant de vérifier si une touché est pressée

    if keys[pygame.K_i] and shootLoop == 0:
        #kunaiSound.play()
        if naruto.left:
            facing = -1
        elif naruto.right:
            facing = 1
        else:
            facing = 1
        if len(kunais) < 3:
            if facing == 1:
                kunais.append(projectile(round(naruto.x + naruto.width // 2), round(naruto.y + naruto.height //4), 6, (0, 0, 0), facing))
            else:
                kunais.append(projectile(round(naruto.x), round(naruto.y + naruto.height // 4), 6, (0, 0, 0), facing))
        shootLoop = 1

    # Left
    if keys[pygame.K_LEFT] and naruto.x > naruto.vel:
        naruto.x -= naruto.vel
        naruto.left = True
        naruto.right = False
        naruto.standing = False

    # Right
    elif keys[pygame.K_RIGHT] and naruto.x < 700 - naruto.width - naruto.vel:
        naruto.x += naruto.vel
        naruto.right = True
        naruto.left = False
        naruto.standing = False

    #Down
    elif keys[pygame.K_DOWN]:
        naruto.isBlock = True
        naruto.left = False
        naruto.right = False

    #Combo
    elif keys[pygame.K_o]:
        naruto.combo1 = True
    else:
        naruto.standing = True
        naruto.isBlock = False
        naruto.walkCount = 0

    #Jump
    if not naruto.isJump:
        if keys[pygame.K_UP]:
            naruto.isJump = True
            naruto.left = False
            naruto.right = False
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

    for kunai in kunais:
        if 670 > kunai.x > 0:
            if kunai.y - kunai.radius < naruto.hitbox[1] + naruto.hitbox[3] and kunai.y + kunai.radius > naruto.hitbox[1]:
                if kunai.x + kunai.radius > naruto.hitbox[0] and kunai.x - kunai.radius < naruto.hitbox[0] + naruto.hitbox[2]:
                    #naruto.hit()
                    score -= 5
                    kunais.pop(kunais.index(kunai))

    if shootLoop > 0:  # Permet de faire fonctionner la shootLoop
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    keys = pygame.key.get_pressed()  # Variable permettant de vérifier si une touché est pressée

    # F (Kunaï)
    if keys[pygame.K_f] and shootLoop == 0:
        # kunaiSound.play()
        if player2.left:
            facing = -1
        elif player2.right:
            facing = 1
        else:
            facing = 1
        if len(kunais) < 3:
            if facing == 1:
                kunais.append(
                    projectile(round(player2.x + player2.width // 2), round(player2.y + player2.height // 4), 6,
                               (0, 0, 0), facing))
            else:
                kunais.append(
                    projectile(round(player2.x), round(player2.y + player2.height // 4), 6, (0, 0, 0), facing))
        shootLoop = 1

    # Left (Q)
    if keys[pygame.K_q] and player2.x > player2.vel:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False
        player2.standing = False

    # Right (D)
    elif keys[pygame.K_d] and player2.x < 700 - player2.width - player2.vel:
        player2.x += player2.vel
        player2.right = True
        player2.left = False
        player2.standing = False

    # Down (S)
    elif keys[pygame.K_s]:
        player2.isBlock = True
        player2.left = False
        player2.right = False

    # Combo (G)
    elif keys[pygame.K_g]:
        player2.combo1 = True
    else:
        player2.standing = True
        player2.isBlock = False
        player2.walkCount = 0

    # Jump (Z)
    if not player2.isJump:
        if keys[pygame.K_z]:
            player2.isJump = True
            player2.left = False
            player2.right = False
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
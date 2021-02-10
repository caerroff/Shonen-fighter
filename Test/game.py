import pygame, time

win_res = (700, 400)
win = pygame.display.set_mode(win_res)
pygame.display.set_caption("Shonen Fighter")

walkRight = [pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"), pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"), pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png"),
             pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"), pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"), pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png")]
walkLeft = [pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False), pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False), pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False),
            pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False), pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False), pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False)]
spritesJump = [pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump2.png"), pygame.image.load("naruto_jump3.png"), pygame.image.load("naruto_jump4.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump2.png"), pygame.image.load("naruto_jump3.png"), pygame.image.load("naruto_jump4.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump2.png"), pygame.image.load("naruto_jump3.png"), pygame.image.load("naruto_jump4.png")]
bg = pygame.image.load("bg.jpg")
narutoSprite = pygame.image.load("naruto_2.png")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (naruto.x, naruto.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (naruto.x, naruto.y))
            self.walkCount += 1
        else:
            win.blit(narutoSprite, (naruto.x, naruto.y))

def redrawGameWindow(): #Toutes les modifications visuelles se feront ici et plus dans la boucle principale
    win.blit(bg, (0, 0))  # Black
    naruto.draw(win)
    pygame.display.update()

naruto = Player(300, 300, 64, 64)
launched = True
while launched:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False

    keys = pygame.key.get_pressed() #Variable permettant de vérifier si une touché est pressée

    if keys[pygame.K_LEFT] and naruto.x > naruto.vel: #///// LEFT
        naruto.x -= naruto.vel
        naruto.left = True
        naruto.right = False
    elif keys[pygame.K_RIGHT] and naruto.x < 700 - naruto.width - naruto.vel: #///// RIGHT
        naruto.x += naruto.vel
        naruto.right = True
        naruto.left = False
    else:
        naruto.right = False
        naruto.left = False
        naruto.walkCount = 0

    if not naruto.isJump:
        if keys[pygame.K_SPACE]:
            naruto.isJump = True
            naruto.left = False
            naruto.right = False
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

    redrawGameWindow()

pygame.quit()
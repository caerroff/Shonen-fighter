import pygame, time

win_res = (700, 400)
win = pygame.display.set_mode(win_res)
pygame.display.set_caption("Shonen Fighter")

walkLeft = [pygame.image.load("N_L_W1.png"), pygame.image.load("N_L_W2.png"), pygame.image.load("N_L_W3.png"), pygame.image.load("N_L_W4.png"), pygame.image.load("N_L_W5.png"), pygame.image.load("N_L_W6.png"), pygame.image.load("N_L_W1.png"), pygame.image.load("N_L_W2.png"), pygame.image.load("N_L_W3.png"), ]
walkRight = [pygame.image.load("N_R_W2.png"), pygame.image.load("N_R_W2.png"), pygame.image.load("N_R_W3.png"), pygame.image.load("N_R_W4.png"), pygame.image.load("N_R_W5.png"), pygame.image.load("N_R_W6.png"), pygame.image.load("N_R_W1.png"), pygame.image.load("N_R_W2.png"), pygame.image.load("N_R_W3.png"), pygame.image.load("N_R_W4.png"), pygame.image.load("N_R_W5.png"), pygame.image.load("N_R_W6.png")]
bg = pygame.image.load("bg.jpg")
naruto = pygame.image.load("N_R3.png")


clock = pygame.time.Clock()

x = 50
y = 300
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
black_color = (0, 0, 0)
green_color = (0, 255, 0)

def redrawGameWindow(): #Toutes les modifications visuelles se feront ici et plus dans la boucle principale
    global walkCount
    win.blit(bg, (0, 0)) #Black

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(naruto, (x, y))

    pygame.display.update()

launched = True
while launched:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN or event.type == pygame.QUIT:
            launched = False

    keys = pygame.key.get_pressed() #Variable permettant de vérifier si une touché est pressée

    if keys[pygame.K_LEFT] and x > vel: #///// LEFT
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 700 - width - vel: #///// RIGHT
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()




pygame.quit()
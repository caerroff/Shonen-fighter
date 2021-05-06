import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Tuto Pichou")

x = 40
y = 40
w = 40
h = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - w - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - h -vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,10), (x,y, w, h))
    pygame.display.update()

pygame.quit()


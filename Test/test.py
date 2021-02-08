import pygame, time

pygame.init()

winRes = (800, 600)
surface = pygame.display.set_mode(winRes)
black_color = (0, 0, 0)

spriteX = 200
spriteY = 200
spriteCoords = (spriteX, spriteY)
#/// Sprite Base
sprite1 = pygame.image.load("Sprite.png")
sprite1.convert()
sprite2 = pygame.image.load("Sprite 2.png")
sprite2.convert()
sprite3 = pygame.image.load("Sprite 3.png")
sprite3.convert()
#/// Sprite Walk
sprite_walk = pygame.image.load("Sprite_walk.png")
sprite_walk.convert()
sprite_walk_2 = pygame.image.load("Sprite_walk_2.png")
sprite_walk_2.convert()
sprite_walk_3 = pygame.image.load("Sprite_walk_3.png")
sprite_walk_3.convert()
sprite_walk_4 = pygame.image.load("Sprite_walk_4.png")
sprite_walk_4.convert()
sprite_walk_5 = pygame.image.load("Sprite_walk_5.png")
sprite_walk_5.convert()
sprite_walk_6 = pygame.image.load("Sprite_walk_6.png")
sprite_walk_6.convert()
#/// Jump
sprite_jump = pygame.image.load("Sprite_jump.png")
sprite_jump.convert()
sprite_jump_2 = pygame.image.load("Sprite_jump_2.png")
sprite_jump_2.convert()
sprite_jump_3 = pygame.image.load("Sprite_jump_3.png")
sprite_jump_3.convert()
sprite_jump_4 = pygame.image.load("Sprite_jump_4.png")
sprite_jump_4.convert()
#/// Block
sprite_block = pygame.image.load("Sprite_block.png")
sprite_block.convert()



surface.blit(sprite1, spriteCoords)
pygame.display.flip()

launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            launched = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            surface.fill(black_color)
            surface.blit(sprite2, spriteCoords)
            pygame.display.flip()
            time.sleep(.001)
            surface.fill(black_color)
            surface.blit(sprite3, spriteCoords)
            pygame.display.flip()
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            surface.fill(black_color)
            surface.blit(sprite2, spriteCoords)
            pygame.display.flip()
            time.sleep(.001)
            surface.fill(black_color)
            surface.blit(sprite1, spriteCoords)
            pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: #Déplacement vers la droite
            surface.fill(black_color)
            surface.blit(sprite_walk, spriteCoords) #Sprite 1
            pygame.display.flip()
            time.sleep(.05)
            spriteX += 2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_2, spriteCoords) #Sprite 2
            pygame.display.flip()
            time.sleep(.05)
            spriteX += 2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_3, spriteCoords) #Sprite 3
            pygame.display.flip()
            time.sleep(.05)
            spriteX += 2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_4, spriteCoords) #Sprite 4
            pygame.display.flip()
            spriteX += 2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_5, spriteCoords) #Sprite 5
            pygame.display.flip()
            spriteX += 2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_6, spriteCoords) #Sprite 6
            pygame.display.flip()
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            surface.fill(black_color)
            surface.blit(sprite2, spriteCoords)
            pygame.display.flip()
            time.sleep(.001)
            surface.fill(black_color)
            surface.blit(sprite1, spriteCoords)
            pygame.display.flip()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            surface.fill(black_color)
            surface.blit(sprite_jump, spriteCoords)
            pygame.display.flip()
            time.sleep(.05)
            spriteY -+ 20
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_jump_2, spriteCoords)
            pygame.display.flip()
            time.sleep(.05)
            spriteY -= 20
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_jump_3, spriteCoords)
            pygame.display.flip()
            time.sleep(.05)
            spriteY -= 20
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_jump_4, spriteCoords)
            pygame.display.flip()
            time.sleep(.05)
            for i in range(40):
                spriteY += 1
                spriteCoords = (spriteX, spriteY)
                surface.fill(black_color)
                surface.blit(sprite_jump_4, spriteCoords)
                pygame.display.flip()
            surface.fill(black_color)
            surface.blit(sprite2, spriteCoords)
            pygame.display.flip()
            time.sleep(.001)
            surface.fill(black_color)
            surface.blit(sprite1, spriteCoords)
            pygame.display.flip()
        if keys[pygame.K_LEFT]:  # Déplaczement vers la gauche
            # if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            # keys = False
            # print("Ouais mec")
            print("Non")
            surface.fill(black_color)
            surface.blit(sprite_walk, spriteCoords) # Sprite 1, Gauche
            pygame.display.flip()
            time.sleep(.05)
            spriteX += -2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_2, spriteCoords) # Sprite 2, Gauche
            pygame.display.flip()
            time.sleep(.05)
            spriteX += -2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_3, spriteCoords) # Sprite 3, Gauche
            pygame.display.flip()
            time.sleep(.05)
            spriteX += -2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_4, spriteCoords) # Sprite 4, Gauche
            pygame.display.flip()
            spriteX += -2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_5, spriteCoords) # Sprite 5, Gauche
            pygame.display.flip()
            spriteX += -2
            spriteCoords = (spriteX, spriteY)
            surface.fill(black_color)
            surface.blit(sprite_walk_6, spriteCoords) # Sprite 6, Gauche
            pygame.display.flip()
            surface.fill(black_color)
            surface.blit(sprite2, spriteCoords)
            pygame.display.flip()
            time.sleep(.001)
            surface.fill(black_color)
            surface.blit(sprite1, spriteCoords) #Retour en Position normal
            pygame.display.flip()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: #Block Down
            surface.fill(black_color)
            surface.blit(sprite_block, spriteCoords)
            pygame.display.flip()
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN: #Block Up
            surface.fill(black_color)
            surface.blit(sprite1, spriteCoords)
            pygame.display.flip()









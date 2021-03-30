import pygame

# from gui import *

pygame.init()
pygame.font.init()

win_res = (700, 400)
win = pygame.display.set_mode(win_res)
pygame.display.set_caption("Shonen Fighter")
walkRight = [pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"),
             pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"),
             pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png"),
             pygame.image.load("naruto_walk1.png"), pygame.image.load("naruto_walk2.png"),
             pygame.image.load("naruto_walk3.png"), pygame.image.load("naruto_walk4.png"),
             pygame.image.load("naruto_walk5.png"), pygame.image.load("naruto_walk6.png")]
walkLeft = [pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False),
            pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False),
            pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False),
            pygame.transform.flip(walkRight[0], True, False), pygame.transform.flip(walkRight[1], True, False),
            pygame.transform.flip(walkRight[2], True, False), pygame.transform.flip(walkRight[3], True, False),
            pygame.transform.flip(walkRight[4], True, False), pygame.transform.flip(walkRight[5], True, False)]
spritesJumpRight = [pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png"), pygame.image.load("naruto_jump1.png"),
               pygame.image.load("naruto_jump1.png")]
spritesJumpLeft = [pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False),
                   pygame.transform.flip(spritesJumpRight[0], True, False)]
blockRight = [pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png"), pygame.image.load("naruto_block.png"),
         pygame.image.load("naruto_block.png")]
blockLeft = [pygame.transform.flip(blockRight[0], True, False), pygame.transform.flip(blockRight[0], True, False),
             pygame.transform.flip(blockRight[0], True, False),
             pygame.transform.flip(blockRight[0], True, False), pygame.transform.flip(blockRight[0], True, False),
             pygame.transform.flip(blockRight[0], True, False),
             pygame.transform.flip(blockRight[0], True, False), pygame.transform.flip(blockRight[0], True, False),
             pygame.transform.flip(blockRight[0], True, False)]
combo1Right = [pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png"), pygame.image.load("naruto_combo3.png"),
          pygame.image.load("naruto_combo3.png")]
combo1Left = [pygame.transform.flip(combo1Right[0], True, False), pygame.transform.flip(combo1Right[1], True, False),
              pygame.transform.flip(combo1Right[2], True, False),
              pygame.transform.flip(combo1Right[2], True, False), pygame.transform.flip(combo1Right[2], True, False),
              pygame.transform.flip(combo1Right[2], True, False),
              pygame.transform.flip(combo1Right[2], True, False), pygame.transform.flip(combo1Right[2], True, False),
              pygame.transform.flip(combo1Right[2], True, False)]
kunaiThrowRight = [pygame.image.load("kunai_throw1.png"), pygame.image.load("kunai_throw2.png"),
              pygame.image.load("kunai_throw3.png"),
              pygame.image.load("kunai_throw2.png"), pygame.image.load("kunai_throw2.png"),
              pygame.image.load("kunai_throw2.png"),
              pygame.image.load("kunai_throw3.png"), pygame.image.load("kunai_throw3.png"),
              pygame.image.load("kunai_throw3.png")]
kunaiThrowLeft = [pygame.transform.flip(kunaiThrowRight[0], True, False), pygame.transform.flip(kunaiThrowRight[1], True, False),
                  pygame.transform.flip(kunaiThrowRight[2], True, False)]
spell1Right = [pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png'),
          pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png'),
          pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png'), pygame.image.load('rasengan1.png')]
spell1Left = [pygame.transform.flip(spell1Right[0], True, False), pygame.transform.flip(spell1Right[0], True, False),
              pygame.transform.flip(spell1Right[0], True, False),
              pygame.transform.flip(spell1Right[0], True, False), pygame.transform.flip(spell1Right[0], True, False),
              pygame.transform.flip(spell1Right[0], True, False),
              pygame.transform.flip(spell1Right[0], True, False), pygame.transform.flip(spell1Right[0], True, False),
              pygame.transform.flip(spell1Right[0], True, False)]
bg = pygame.image.load("bg.jpg")
narutoSprite = pygame.image.load("naruto_2.png")
narutoSpriteLeft = pygame.transform.flip(narutoSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)

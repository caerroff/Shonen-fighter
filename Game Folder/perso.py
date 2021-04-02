import pygame

# from gui import *

NarutoWalkRight = [pygame.image.load("../Sprite/Naruto/Walk/Sprite 1.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 2.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 3.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 4.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 5.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 6.png")]
NarutoWalkLeft = [pygame.transform.flip(NarutoWalkRight[0], True, False),
            pygame.transform.flip(NarutoWalkRight[1], True, False),
            pygame.transform.flip(NarutoWalkRight[2], True, False),
            pygame.transform.flip(NarutoWalkRight[3], True, False),
            pygame.transform.flip(NarutoWalkRight[4], True, False),
            pygame.transform.flip(NarutoWalkRight[5], True, False)]
NarutoJumpRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 2.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 3.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 4.png")]
#NarutoJumpingRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
#                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 2.png")]
#NarutoFallingRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 3.png"),
#                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 4.png")]
NarutoJumpLeft = [pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[1], True, False),
                   pygame.transform.flip(NarutoJumpRight[2], True, False),
                   pygame.transform.flip(NarutoJumpRight[3], True, False)]
NarutoBlockRight = [pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png"),
              pygame.image.load("../Sprite/Naruto/Block/Sprite 1.png")]
NarutoBlockLeft = [pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False),
             pygame.transform.flip(NarutoBlockRight[0], True, False)]
NarutoCombo1Right = [pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 1.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 2.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 4.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 5.png")]
NarutoCombo1Left = [pygame.transform.flip(NarutoCombo1Right[0], True, False),
              pygame.transform.flip(NarutoCombo1Right[1], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False),
              pygame.transform.flip(NarutoCombo1Right[2], True, False)]
NarutoKunaiThrowRight = [pygame.image.load("../Sprite/Naruto/Throw/Sprite 1.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 2.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 3.png")]
NarutoKunaiThrowLeft = [pygame.transform.flip(NarutoKunaiThrowRight[0], True, False),
                  pygame.transform.flip(NarutoKunaiThrowRight[1], True, False),
                  pygame.transform.flip(NarutoKunaiThrowRight[2], True, False)]
NarutoSpell1Right = [pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png'),
               pygame.image.load('../Sprite/Naruto/Rasengan/Sprite 1.png')]
NarutoSpell1Left = [pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False),
              pygame.transform.flip(NarutoSpell1Right[0], True, False)]
SasukeRunRight = [pygame.image.load("../Sprite/Sasuke/Run/Sprite 1.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Sprite 2.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Sprite 3.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Sprite 4.png")]
SasukeRunLeft = [pygame.transform.flip(SasukeRunRight[0], True, False),
                 pygame.transform.flip(SasukeRunRight[1], True, False),
                 pygame.transform.flip(SasukeRunRight[2], True, False),
                 pygame.transform.flip(SasukeRunRight[3], True, False)]
SasukeJumpRight = [pygame.image.load("../Sprite/Sasuke/Jump/Sprite 1.png")]
                   #ygame.image.load("../Sprite/Sasuke/Jump/Sprite 1.png")]
SasukeJumpLeft = [pygame.transform.flip(SasukeJumpRight[0], True, False)]
                  #pygame.transform.flip(SasukeJumpRight[0], True, False)]
SasukeBlockRight = [pygame.image.load("../Sprite/Sasuke/Block/Sprite 1.png")]
SasukeBlockLeft = [pygame.transform.flip(SasukeBlockRight[0], True, False)]

bg = pygame.image.load("bg.jpg")
NarutoSprite = pygame.image.load("naruto_2.png")
NarutoSpriteLeft = pygame.transform.flip(NarutoSprite, True, False)
SasukeSpriteRight = pygame.image.load("../Sprite/Sasuke/Stand/Sprite 1.png")
SasukeSpriteLeft = pygame.transform.flip(SasukeSpriteRight, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)


SasukeSpriteTransformationRight = pygame.image.load("../Sprite/Sasuke/Transformation/Sprite 1.png")
SasukeSpriteTransformationLeft = pygame.transform.flip(SasukeSpriteTransformationRight, True, False)

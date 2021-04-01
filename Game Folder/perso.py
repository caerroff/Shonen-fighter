import pygame

# from gui import *

NarutoWalkRight = [pygame.image.load("../Sprite/Naruto/Walk/Sprite 1.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 2.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 3.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 4.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 5.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 6.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 1.png"),
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
            pygame.transform.flip(NarutoWalkRight[5], True, False),
            pygame.transform.flip(NarutoWalkRight[0], True, False),
            pygame.transform.flip(NarutoWalkRight[1], True, False),
            pygame.transform.flip(NarutoWalkRight[2], True, False),
            pygame.transform.flip(NarutoWalkRight[3], True, False),
            pygame.transform.flip(NarutoWalkRight[4], True, False),
            pygame.transform.flip(NarutoWalkRight[5], True, False)]
NarutoJumpRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png")]
NarutoJumpLeft = [pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False),
                   pygame.transform.flip(NarutoJumpRight[0], True, False)]
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
NarutoCombo1Right = [pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png"),
               pygame.image.load("../Sprite/Naruto/Combo 1/Sprite 3.png")]
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
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 3.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 2.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 2.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 2.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 3.png"),
                   pygame.image.load("../Sprite/Naruto/Throw/Sprite 3.png"),
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
SasukeWalkRight = [pygame.image.load("../Sprite/Sasuke/Run/Run 1.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Run 2.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Run 3.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Run 4.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Run 5.png"),
                   pygame.image.load("../Sprite/Sasuke/Run/Run 6.png")]
bg = pygame.image.load("bg.jpg")
NarutoSprite = pygame.image.load("naruto_2.png")
NarutoSpriteLeft = pygame.transform.flip(NarutoSprite, True, False)
SasukeSprite = pygame.image.load("../Sprite/Sasuke/Stand/Sprite 1.png")
SasukeSpriteLeft = pygame.transform.flip(SasukeSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)

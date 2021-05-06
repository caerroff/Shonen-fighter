import pygame

# from gui import *

NarutoRunRight = [pygame.image.load("../Sprite/Naruto/Walk/Sprite 1.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 2.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 3.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 4.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 5.png"),
             pygame.image.load("../Sprite/Naruto/Walk/Sprite 6.png")]
NarutoRunLeft = [pygame.transform.flip(NarutoRunRight[0], True, False),
            pygame.transform.flip(NarutoRunRight[1], True, False),
            pygame.transform.flip(NarutoRunRight[2], True, False),
            pygame.transform.flip(NarutoRunRight[3], True, False),
            pygame.transform.flip(NarutoRunRight[4], True, False),
            pygame.transform.flip(NarutoRunRight[5], True, False)]
NarutoJumpingRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 1.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 2.png")]
NarutoJumpingLeft = [pygame.transform.flip(NarutoJumpingRight[0], True, False),
                     pygame.transform.flip(NarutoJumpingRight[1], True, False)]
NarutoFallingRight = [pygame.image.load("../Sprite/Naruto/Jump/Sprite 3.png"),
                    pygame.image.load("../Sprite/Naruto/Jump/Sprite 4.png")]
NarutoFallingLeft = [pygame.transform.flip(NarutoFallingRight[0], True, False),
                     pygame.transform.flip(NarutoFallingRight[1], True, False)]
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
SasukeJumpingRight = [pygame.image.load("../Sprite/Sasuke/Jump/Sprite 1.png")]
SasukeJumpingLeft = [pygame.transform.flip(SasukeJumpingRight[0], True, False)]
SasukeFallingRight = [pygame.image.load("../Sprite/Sasuke/Jump/Sprite 2.png")]
SasukeFallingLeft = [pygame.transform.flip(SasukeFallingRight[0], True, False)]
SasukeBlockRight = [pygame.image.load("../Sprite/Sasuke/Block/Sprite 1.png")]
SasukeBlockLeft = [pygame.transform.flip(SasukeBlockRight[0], True, False)]
SasukeCombo1Right = [pygame.image.load("../Sprite/Sasuke/Combo 1/Sprite 1.png"),
                     pygame.image.load("../Sprite/Sasuke/Combo 1/Sprite 2.png"),
                     pygame.image.load("../Sprite/Sasuke/Combo 1/Sprite 3.png"),
                     pygame.image.load("../Sprite/Sasuke/Combo 1/Sprite 4.png"),
                     pygame.image.load("../Sprite/Sasuke/Combo 1/Sprite 5.png")]
SasukeCombo1Left = [pygame.transform.flip(SasukeCombo1Right[0], True, False),
                    pygame.transform.flip(SasukeCombo1Right[1], True, False),
                    pygame.transform.flip(SasukeCombo1Right[2], True, False),
                    pygame.transform.flip(SasukeCombo1Right[3], True, False),
                    pygame.transform.flip(SasukeCombo1Right[4], True, False)]
SasukeAwakeningRight = [pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 1.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 2.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 3.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 4.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 5.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 6.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 7.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 8.png"),
                        pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 9.png")]
SasukeAwakeningLeft = [pygame.transform.flip(SasukeAwakeningRight[0], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[1], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[2], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[3], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[4], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[5], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[6], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[7], True, False),
                       pygame.transform.flip(SasukeAwakeningRight[8], True, False)]
SasukeSpell1Right = [pygame.image.load("../Sprite/Sasuke/Spell 1/Sprite 1.png"),
                     pygame.image.load("../Sprite/Sasuke/Spell 1/Sprite 2.png"),
                     pygame.image.load("../Sprite/Sasuke/Spell 1/Sprite 3.png")]
SasukeSpell1Left = [pygame.transform.flip(SasukeSpell1Right[0], True, False),
                    pygame.transform.flip(SasukeSpell1Right[1], True, False),
                    pygame.transform.flip(SasukeSpell1Right[2], True, False)]
SasukeFireballRight = [pygame.image.load("../Sprite/Sasuke/Effect/Sprite 1.png")]
SasukeFireballLeft = [pygame.transform.flip(SasukeFireballRight[0], True, False)]

bg = pygame.image.load("bg.jpg")
NarutoSprite = pygame.image.load("naruto_2.png")
NarutoSpriteLeft = pygame.transform.flip(NarutoSprite, True, False)
SasukeSpriteRight = pygame.image.load("../Sprite/Sasuke/Stand/Sprite 1.png")
SasukeSpriteLeft = pygame.transform.flip(SasukeSpriteRight, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)
kunaiSprite = pygame.image.load("kunai.png")
kunaiSpriteLeft = pygame.transform.flip(kunaiSprite, True, False)


SasukeSpriteAwakeningRight = pygame.image.load("../Sprite/Sasuke/Awakening/Sprite 1.png")
SasukeSpriteAwakeningLeft = pygame.transform.flip(SasukeSpriteAwakeningRight, True, False)

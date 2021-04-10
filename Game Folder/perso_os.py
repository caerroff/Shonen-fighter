#!/usr/bin/env python
# -*- coding: utf-8 -*-

### Renommage cohérent des répertoires : Combo 1 --> Combo1 ; Rasengan --> Spell1

import os, pygame

def perso(path = "../Sprite/", name ="Naruto", default_orientation=">") :
    """Dictionnaire de sprites pour un perso"""
    perso = {}
    def flip(sprite, orientation = ">") :   # Fonction pour flipper les sprites :
        if orientation == default_orientation : return sprite
        else : return pygame.transform.flip(sprite, True, False)    
    poses = next(os.walk(path+name))[1]     # Poses (clés d'un dict des dossiers) + Left/Right :
    for pose in poses :    
        perso[pose+"Left"] = []
        perso[pose+"Right"] = []
        ls_sprites = next(os.walk(path+name+"/"+pose))[2]
        ls_sprites.sort()
        for png in ls_sprites :             # Collecte des fichiers png :
            perso[pose+"Left" ].append(flip(pygame.image.load(path+name+"/"+pose+"/"+png), "<"))
            perso[pose+"Right"].append(flip(pygame.image.load(path+name+"/"+pose+"/"+png), ">"))
    return perso

Naruto = perso()
Sasuke = perso('../Sprite/', 'Sasuke')
Deku = perso('../Sprite/', 'Deku')

### Recréation d'une multitude de variables à partir du dico :
### ET ÇA BLOQUE : et de toutes façons, exec, c'est sale !
## persos = [ ("../Sprite/", "Naruto", ">"), ("../Sprite/", "Sasuke", ">") ]
# persos = [ ("", "naruto", ">") ]
# for pers in persos :
#     p = perso(*pers)
#     for pose in p.keys() :
#         exec(pers[1]+pose + "=" + str(p[pose]))
# pprint(locals())



def main(args) :   # Pour lancement direct et vérif sprites :
    return 0
if __name__ == '__main__':
    import sys
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    font = pygame.font.SysFont(None, 35)
    perso1 = perso("../Sprite/", "Naruto", ">")
    x, y = 0, 0
    for pose in perso1.keys() :
        y = 0
        for sprite in perso1[pose] :
            if y > 600 :
                y = 0
                x += int(1.2*sprite.get_size()[0])
            screen.blit(sprite, (x,y))
            y += int(1.2*sprite.get_size()[1])
        screen.blit(pygame.transform.rotate(font.render(pose, True, (255,255,255)),-90), (x,y))
        x += int(1.2*sprite.get_size()[0])
    continuer = True
    while continuer :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                continuer = False
        pygame.display.flip()
    pygame.quit()
    sys.exit(main(sys.argv))

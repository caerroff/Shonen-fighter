# -*- coding: utf-8 -*-

class Player :
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, width, height)

    def __str__(self) :
        return "x {0:4d} | y {1:4d} | hx {2:2d} | hy {3:2d}".format(self.hitbox[0], self.hitbox[1], self.hitbox[2], self.hitbox[3])

    def collision(self, other) :
        return (-other.hitbox[0] <= other.x - self.x <= self.hitbox[0]) and (-other.hitbox[1] <= other.y - self.y <= self.hitbox[1])


from random import randrange
k=1
while k <= 1000 :
    p1 = Player( randrange(100), randrange(100), randrange(5,12), randrange(5,12) )
    p2 = Player( randrange(100), randrange(100), randrange(5,12), randrange(5,12) )
    if p1.collision(p2) :
        print(p1, "et", p2, "collision")
    else :
        print(p1, "et", p2, "pas collision")
    k+=1
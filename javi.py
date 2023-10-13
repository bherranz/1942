
import random
import pyxel
import data
import time
from bullets import Bullets_e


class Javi:
    """This class contain information about the enemy named javi"""
    def __init__(self):
        self.y = 0
        self.w = data.Javi_WIDTH
        self.h = data.Javi_HEIGHT
        self.alive = True
        self.counter = 0
        self.x = random.randint(0, 190)
        self.possibility = random.randint(1, 3)
        self.b = pyxel.rndi(0, 59)
        self.dir = 1
        self.maybe = random.randint(1, 5)
        self.reach = False
        self.shoot = False
        self.bullets_j_l = []
        self.collision = False
        self.a = time.time()

    def update(self):
        """The position y goes down until half screen and then it could
        move up, with a random and static position x"""
        if self.maybe == 2 and self.y >= data.PROG_HEIGHT / 2:
            self.reach = True
        elif self.reach is False:
            self.y += data.Javi_SPEED
            if (pyxel.frame_count + self.b) % 60 < 20:
                self.x += data.Javi_SPEED
                self.dir = 1
            else:
                self.x -= data.Javi_SPEED
                self.dir = -1
            if self.y > data.PROG_HEIGHT - 1:
                self.alive = False
            if self.possibility == 1 or self.possibility == 2:
                num = random.randint(1, data.PROG_HEIGHT / 2)
                if self.y == num:
                    self.shoot = True
                    self.bullet = Bullets_e(self.x, self.y)
                    self.bullets_j_l.append(self.bullet)
        if self.reach:
            self.y -= data.Javi_SPEED
            if self.y < 0:
                self.alive = False

    def draw(self):
        """This function will contain the sprite of the plane javi, imported
        from pyxel edit and the initial position of the plane javi"""
        if self.alive is True:
            # If the enemy reaches the middle of the screen, it will have
            # some probability of going backwards. So this will charge that
            # sprite
            self.a = time.time()
            if self.reach is False:
                pyxel.blt(self.x, self.y, 0, 6, 202, self.w, self.h, 8)
                if self.shoot:
                    self.bullet.update()
                    self.bullet.draw()
            else:
                pyxel.blt(self.x, self.y, 0, 4, 160, self.w, self.h, 8)
        else:
            # When the enemy is not alive, this will create an animation of
            # each enemy's collision, relating it with the time in screen

            if time.time() - self.a < 0.1:
                pyxel.blt(self.x, self.y, 0, 164, 80, 12, 12, 0)
            elif 0.1 <= time.time() - self.a < 0.15:
                pyxel.blt(self.x, self.y, 0, 180, 80, 14, 12, 0)
            elif 0.15 <= time.time() - self.a < 0.3:
                pyxel.blt(self.x, self.y, 0, 196, 78, 16, 16, 0)
                self.collision = True

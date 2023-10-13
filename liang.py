
import pyxel
import time
import data
import math
import random
from bullets import Bullets_e

class Liang:
    """This class contain information about the enemy named liang"""

    def __init__(self):
        self.x = 0
        self.y = 40
        self.w = data.Liang_WIDTH
        self.h = data.Liang_HEIGHT
        self.alive = True
        self.collision = False
        self.turn_time = time.time()
        self.a = time.time()
        self.shoot = False
        self.shoot_time = time.time()
        self.bullets_l_l = []
        self.rarely = random.randint(1, 3)

    def update(self):
        """This enemy come also in groups following a formation.
        They usually perform two or three circles until they disappear.
        They rarely shoot at you. If you destroy them all you get some bonus
        like double shooting capacity."""
        if time.time() - self.turn_time < 1:
            self.x += data.Liang_SPEED
            self.y = 40
        elif time.time() - self.turn_time < 1.3:
            self.x += 2*math.cos(math.radians(45))
            self.y += 2*math.sin(math.radians(45))
        elif time.time() - self.turn_time < 1.6:
            self.y += data.Liang_SPEED
        elif time.time() - self.turn_time < 1.9:
            self.x -= 2*math.sin(math.radians(45))
            self.y += 2*math.cos(math.radians(45))
        elif time.time() - self.turn_time < 2.2:
            self.x -= data.Liang_SPEED
        elif time.time() - self.turn_time < 2.5:
            self.x -= 2 * math.cos(math.radians(45))
            self.y -= 2 * math.sin(math.radians(45))
        elif time.time() - self.turn_time < 2.8:
            self.y -= data.Liang_SPEED
        elif time.time() - self.turn_time < 3.1:
            self.x += 2 * math.sin(math.radians(45))
            self.y -= 2 * math.cos(math.radians(45))
            self.turn_time = time.time()
        if self.rarely == 1:
            if time.time() - self.shoot_time > 2:
                self.shoot = True
                bullet = Bullets_e(self.x + data.Diego_WIDTH/2, self.y + 9)
                self.bullets_l_l.append(bullet)
                self.shoot_time = time.time()

    def draw(self):
        """This function will contain the sprite of the plane liang, imported
        from pyxel edit and the initial position of the plane liang. There
        will be fewer number of liang planes"""
        if self.alive is True:
            # As liang moves with a circular motion, this "if" will create 9
            # sprites in order to create a more realistic motion.
            self.a = time.time()
            if time.time() - self.turn_time < 1:
                pyxel.blt(self.x, self.y, 1, 38, 132, 14, 14, 4)
            elif time.time() - self.turn_time < 1.3:
                pyxel.blt(self.x, self.y, 1, 58, 138, 14, 12, 4)
            elif time.time() - self.turn_time < 1.6:
                pyxel.blt(self.x, self.y, 1, 60, 152, 16, 14, 4)
            elif time.time() - self.turn_time < 1.9:
                pyxel.blt(self.x, self.y, 1, 54, 170, 12, 12, 4)
            elif time.time() - self.turn_time < 2.2:
                pyxel.blt(self.x, self.y, 1, 30, 172, 14, 12, 4)
            elif time.time() - self.turn_time < 2.5:
                pyxel.blt(self.x, self.y, 1, 6, 168, 14, 14, 4)
            elif time.time() - self.turn_time < 2.8:
                pyxel.blt(self.x, self.y, 1, 4, 152, 16, 14, 4)
            elif time.time() - self.turn_time < 3.1:
                pyxel.blt(self.x, self.y, 1, 10, 136, 14, 14, 4)
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
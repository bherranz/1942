import pyxel
import data
import random
import time
from bullets import Bullets_e


class Barbara:
    """This class will contain the info referring to what happens when the
    user press Z"""
    def __init__(self):
        self.x = random.randint(30, 150)
        self.y = 0
        self.w = data.Barbara_WIDTH
        self.h = data.Barbara_HEIGHT
        self.alive = True
        self.shoot = False
        self.collision = False
        self.b = pyxel.rndi(0, 59)
        self.dir = 1
        self.lives = 15
        self.a = time.time()
        self.t = time.time()
        self.bullets_b_l = []
        self.Oscar = time.time()

    def update(self):
        """This plane is stronger than others, it shoots more bullets and
        moves along the x axis, slower than liang plane"""
        if self.y < data.PROG_WIDTH - 140:
            self.y += data.Barbara_SPEED + 1
        else:
            self.y += data.Barbara_SPEED - 0.6
            if (pyxel.frame_count + self.b) % 60 < 20:
                self.x += data.Barbara_SPEED
                self.dir = 1
            else:
                self.x -= data.Barbara_SPEED
                self.dir = -1

            if time.time() - self.t > 0.5:
                self.shoot = True
                bullet = Bullets_e(self.x + data.Barbara_WIDTH / 2 - 5,
                                   self.y + 40)
                self.bullets_b_l.append(bullet)
                self.Oscar = time.time()
                self.t = time.time()
            if self.y > data.PROG_HEIGHT - 1:
                self.alive = False

    def draw(self):
        if self.alive:
            pyxel.blt(self.x, self.y, 1, 0, 0, self.w, self.h, 0)
            self.a = time.time()
            for bullet in self.bullets_b_l:
                bullet.update()
                bullet.draw()
        else:
            # When the enemy is not alive, this will create an animation of
            # each enemy's collision, relating it with the time in screen
            if time.time() - self.a < 0.1:
                pyxel.blt(self.x, self.y, 0, 0, 104, 30, 22, 0)
            elif 0.1 <= time.time() - self.a < 0.2:
                pyxel.blt(self.x, self.y, 0, 34, 102, 32, 28, 0)
            elif 0.2 <= time.time() - self.a < 0.3:
                pyxel.blt(self.x, self.y, 0, 70, 100, 32, 30, 0)
            elif 0.3 <= time.time() - self.a < 0.4:
                pyxel.blt(self.x, self.y, 0, 104, 100, 32, 32, 1)
            elif 0.4 <= time.time() - self.a < 0.5:
                pyxel.blt(self.x, self.y, 0, 140, 102, 30, 28, 1)
            else:
                pyxel.blt(self.x, self.y, 0, 176, 104, 28, 22, 0)
                self.collision = True




import pyxel
import random
import data
import time
from bullets import Bullets_e

class Diego:
    """This class contain information about the enemy named diego"""
    def __init__(self):
        self.x = 0
        self.xi = random.randint(50, data.PROG_WIDTH-data.Diego_WIDTH)
        self.y = random.randint(1, 50)
        self.w = data.Diego_WIDTH
        self.h = data.Diego_HEIGHT
        self.a = time.time()
        self.alive = True
        self.shoot = False
        self.collision = False
        self.lives = 5
        self.bullets_d_l = []
        self.t = time.time()

    def update(self):
        """This plane is stronger than others, it shoots more bullets and
        moves along the x axis, slower than liang plane"""
        if self.x < self.xi:
            self.x += (data.Diego_SPEED - 1)
        else:
            self.y += data.Diego_SPEED + 0.5
        if time.time() - self.t > 2:
            self.shoot = True
            bullet = Bullets_e(self.x + data.Diego_WIDTH/2, self.y + 9)
            self.bullets_d_l.append(bullet)
            self.t = time.time()

    def draw(self):
        """This function will contain the sprite of the plane diego, imported
        from pyxel edit and the initial position of the plane diego"""
        # 32, 48, 32, 18
        if self.alive:
            pyxel.blt(self.x, self.y, 0, 32, 48, self.w, self.h, 8)
            self.a = time.time()
            for bullet in self.bullets_d_l:
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


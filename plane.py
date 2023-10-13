import pyxel
from bullets import Bullets_p
from enemies import Enemies
import data
import time
import random


class Plane:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.w = data.Plane_WIDTH
        self.h = data.Plane_HEIGHT
        self.b = False
        self.lives = 3
        self.bullets_p_l = []
        self.alive = True
        self.enemies = Enemies()
        self.collision = False
        self.bonus_pos = random.randint(10, data.PROG_WIDTH - 30)
        self.bonus = False
        self.double_shoot = False
        self.double_time = time.time()
        self.loop = False
        self.loop_time = time.time()

    def move(self, direction: str):
        """This function contains the program that execute the movement of
        the player's plane inside the boundaries"""
        # If the arrows are pressed it updates x or y accordingly
        if self.lives == 0:
            self.alive = False

        if pyxel.btn(pyxel.KEY_SPACE) and direction == 'none':
            # As we invoke the bullets function here, we need to add a
            # direction string (none), and append it to the bullets list
            bullet_p = Bullets_p(self.x, self.y)
            self.bullets_p_l.append(bullet_p)
            # To invoke the bonus, we will use the following condition
            if self.double_shoot:
                for element in self.bullets_p_l:
                    element.double_shoot = True
        if pyxel.btn(pyxel.KEY_RIGHT) and direction == 'right':
            self.x += data.Plane_SPEED
            self.right = True
        if pyxel.btn(pyxel.KEY_LEFT) and direction == 'left':
            self.x -= data.Plane_SPEED
            self.left = True
        if pyxel.btn(pyxel.KEY_UP) and direction == 'up':
            self.y -= data.Plane_SPEED
        if pyxel.btn(pyxel.KEY_DOWN) and direction == 'down':
            self.y += data.Plane_SPEED

        if self.bonus:
            if (self.x + self.w > self.bonus_pos
                    and self.bonus_pos + 14 > self.x
                    and self.y + self.h > self.bonus_pos
                    and self.bonus_pos + 10 > self.y):
                self.double_shoot = True
                self.double_time = time.time()
                self.bonus = False
        # In order to stop this bonus, we will use the command time.time()
        # and a bool
        if time.time() - self.double_time > 10:
            self.double_shoot = False

    def draw(self):
        if self.alive is True:
            if not self.loop:
                # To create a simulation of the helix movement, we have
                # related it with frame.count
                if pyxel.frame_count % 2 == 0:
                    pyxel.blt(self.x, self.y, 0, 134, 7, self.w,
                              self.h, 8)
                else:
                    pyxel.blt(self.x, self.y, 1, 134, 7, self.w,
                              self.h, 8)
                self.loop_time = time.time()
            else:
                # To animate the loop, we will use the following sequence of
                # sprites
                if time.time() - self.loop_time < 0.15:
                    pyxel.blt(self.x, self.y-8, 0, 228, 29, 24, 7, 8)
                elif time.time() - self.loop_time < 0.3:
                    pyxel.blt(self.x, self.y-8, 0, 164, 31, 24, 6, 8)
                elif time.time() - self.loop_time < 0.45:
                    pyxel.blt(self.x, self.y-8, 0, 68, 27, 26, 12, 8)
                elif time.time() - self.loop_time < 0.6:
                    pyxel.blt(self.x, self.y+6, 0, 35, 52, 29, 16, 8)
                elif time.time() - self.loop_time < 0.75:
                    pyxel.blt(self.x, self.y+6, 0, 66, 48, 31, 21, 8)
                elif time.time() - self.loop_time < 0.9:
                    pyxel.blt(self.x, self.y+6, 0, 100, 29, 26, 7, 8)
                elif time.time() - self.loop_time < 1.05:
                    pyxel.blt(self.x, self.y+6, 0, 228, 29, 24, 7, 8)
                else:
                    self.loop = False

            self.a = time.time()
            for element in self.bullets_p_l:
                element.update()
                element.draw()
            # To draw the bonus bullets, we will use the following:
            if self.bonus:
                pyxel.blt(self.bonus_pos, self.bonus_pos, 0, 90, 140, 14,
                          10, 8)

        else:
            # For the collision animation
            if time.time() - self.a < 0.2:
                pyxel.blt(self.x, self.y, 0, 0, 104, 30, 22, 0)
            elif 0.2 <= time.time() - self.a < 0.4:
                pyxel.blt(self.x, self.y, 0, 34, 102, 32, 28, 0)
            elif 0.4 <= time.time() - self.a < 0.6:
                pyxel.blt(self.x, self.y, 0, 70, 100, 32, 30, 0)
            elif 0.6 <= time.time() - self.a < 0.8:
                pyxel.blt(self.x, self.y, 0, 104, 100, 32, 32, 1)
            elif 0.8 <= time.time() - self.a < 1:
                pyxel.blt(self.x, self.y, 0, 140, 102, 30, 28, 1)
            elif 1 <= time.time() - self.a < 1.2:
                pyxel.blt(self.x, self.y, 0, 176, 104, 28, 22, 0)
            else:
                # If collision happens, the plane will return to its initial
                # position
                self.x = data.PROG_WIDTH / 2 - 15
                self.y = 200
                self.collision = True

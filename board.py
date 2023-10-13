import pyxel
from enemies import Enemies
from plane import Plane
import time
import data


class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, width: int, height: int):
        """ The parameters are the width and height of the board"""
        self.width = width
        self.height = height
        self.start = False
        self.features = False
        self.game_over = False
        self.plane = Plane(self.width / 2 - 15, 200)
        self.enemies = Enemies()
        self.score = 0
        self.count_loop = 0
        self.t = time.time()
        # To initialize pyxel
        pyxel.init(self.width, self.height, title="1942")
        pyxel.load("assets\my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ This is executed each frame, here invocations to the update
        methods of all objects must be included"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        # If you press "S" the game will start
        if pyxel.btn(pyxel.KEY_S):
            self.score = 0
            self.features = False
            self.game_over = False
            self.start = True
            self.plane.alive = True
        # To see the features you have to press F
        if pyxel.btnp(pyxel.KEY_F):
            self.features = True

        # The plane will move with a horizontal, vertical and diagonal
        # direction
        if self.start is True and self.features is False:
            if pyxel.btn(pyxel.KEY_RIGHT):
                if self.plane.x < self.width - 25:
                    self.plane.move('right')
            if pyxel.btn(pyxel.KEY_LEFT):
                if self.plane.x > 5:
                    self.plane.move('left')
            if pyxel.btn(pyxel.KEY_UP):
                if self.plane.y > 0:
                    self.plane.move('up')
            if pyxel.btn(pyxel.KEY_DOWN):
                if self.plane.y < self.height - 20:
                    self.plane.move('down')
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.plane.move('none')
            if pyxel.btnp(pyxel.KEY_Z) and self.count_loop < 2:
                self.plane.loop = True
                self.count_loop += 1

            self.enemies.update()

            # This three fors are related with the first type of enemies (Javi)
            for enemy in self.enemies.list_j:
                # If a bullet from the plane touch a plane javi,
                # it is destroyed
                for bullet in self.plane.bullets_p_l:
                    if (enemy.x + enemy.w > bullet.x
                            and bullet.x + bullet.w > enemy.x
                            and enemy.y + enemy.h > bullet.y
                            and bullet.y + bullet.h > enemy.y):
                        enemy.alive = False
                        bullet.alive = False
                        self.score += 10
                        self.plane.bullets_p_l.remove(bullet)

            # When an enemy touches our plane, the enemy will die and the
            # plane loses a life
            for enemy in self.enemies.list_j:
                if (enemy.x + enemy.w > self.plane.x
                        and self.plane.x + data.Plane_WIDTH > enemy.x
                        and enemy.y + enemy.h > self.plane.y
                        and self.plane.y + data.Plane_HEIGHT > enemy.y
                        and enemy.alive is True and self.plane.lives != 0
                        and self.plane.loop is False):
                    self.plane.lives -= 1
                    enemy.alive = False
                if enemy.collision:
                    self.enemies.list_j.remove(enemy)
                if enemy.y <= 0:
                    self.enemies.list_j.remove(enemy)
            # When javi's bullets get in contact with the user's plane,
            # the plane will lose a life
            for element in self.enemies.list_j:
                for bullet in element.bullets_j_l:
                    if (self.plane.x + self.plane.w > bullet.x
                            and bullet.x + bullet.w > self.plane.x
                            and self.plane.y + self.plane.h > bullet.y
                            and bullet.y + bullet.h > self.plane.y
                            and self.plane.lives != 0
                            and self.plane.loop is False):
                        self.plane.lives -= 1
                        bullet.alive = False
                        if not bullet.alive:
                            element.bullets_j_l.remove(bullet)

            # This two fors are related with the second type of enemies (liang)
            for enemy in self.enemies.list_l:
                # If a bullet from the plane touch a plane liang,
                # it is destroyed
                for bullet in self.plane.bullets_p_l:
                    if (enemy.x + enemy.w > bullet.x
                            and bullet.x + bullet.w > enemy.x
                            and enemy.y + enemy.h > bullet.y
                            and bullet.y + bullet.h > enemy.y
                            and enemy.alive is True):
                        bullet.alive = False
                        self.enemies.damaged += 1
                        enemy.alive = False
                        self.score += 10
                        self.plane.bullets_p_l.remove(bullet)
                        if self.enemies.damaged == 5:
                            self.plane.bonus = True
                # When an enemy touches our plane, the enemy will die and the
                # plane loses a life
                if (enemy.x + enemy.w > self.plane.x
                        and self.plane.x + data.Plane_WIDTH > enemy.x
                        and enemy.y + enemy.h > self.plane.y
                        and self.plane.y + data.Plane_HEIGHT > enemy.y
                        and enemy.alive is True and self.plane.lives != 0
                        and self.plane.loop is False):
                    self.plane.lives -= 1
                    enemy.alive = False
                if enemy.collision:
                    self.enemies.dead += 1
                    self.enemies.list_l.remove(enemy)

                if enemy.x > data.PROG_WIDTH + 10:
                    self.enemies.dead += 1
                    self.enemies.list_l.remove(enemy)
                # When liang's bullets get in contact with the user's plane,
                # the plane will lose a life
                for bullet in enemy.bullets_l_l:
                    if (self.plane.x + self.plane.w > bullet.x
                            and bullet.x + bullet.w > self.plane.x
                            and self.plane.y + self.plane.h > bullet.y
                            and bullet.y + bullet.h > self.plane.y
                            and self.plane.lives != 0
                            and self.plane.loop is False):
                        self.plane.lives -= 1
                        bullet.alive = False
                        if not bullet.alive:
                            enemy.bullets_l_l.remove(bullet)

            # This two fors are related with diego type of enemies
            for enemy in self.enemies.list_d:
                # If a bullet from the plane touch a plane diego,
                # it is destroyed
                for bullet in self.plane.bullets_p_l:
                    if (enemy.x + enemy.w > bullet.x
                            and bullet.x + bullet.w > enemy.x
                            and enemy.y + enemy.h > bullet.y
                            and bullet.y + bullet.h > enemy.y
                            and enemy.lives != 0 and self.plane.loop is False):
                        enemy.lives -= 1
                        self.score += 20
                        bullet.alive = False
                        self.plane.bullets_p_l.remove(bullet)
                if enemy.lives == 0:
                    enemy.alive = False
                if enemy.collision is True:
                    self.enemies.list_d.remove(enemy)

                # If diego is in contact with the player, the player will
                # lose a live and diego will die.
                if (enemy.x + enemy.w > self.plane.x
                        and self.plane.x + data.Plane_WIDTH > enemy.x
                        and enemy.y + enemy.h > self.plane.y
                        and self.plane.y + data.Plane_HEIGHT > enemy.y
                        and enemy.alive is True and self.plane.lives != 0
                        and self.plane.loop is False):
                    self.plane.lives -= 1
                    enemy.alive = False

                for bullet in enemy.bullets_d_l:
                    if (self.plane.x + self.plane.w > bullet.x
                            and bullet.x + bullet.w > self.plane.x
                            and self.plane.y + self.plane.h > bullet.y
                            and bullet.y + bullet.h > self.plane.y
                            and self.plane.lives != 0
                            and self.plane.loop is False):
                        self.plane.lives -= 1
                        bullet.alive = False
                        if not bullet.alive:
                            enemy.bullets_d_l.remove(bullet)
            # The following three fors are related to the Plane Barbara
            # If barbara is in contact with the bullets of the player,
            # barbara will lose one of its 15 lives.
            for barbara in self.enemies.list_b:
                for bullet in self.plane.bullets_p_l:
                    if (barbara.x + barbara.w > bullet.x
                            and bullet.x + bullet.w > barbara.x
                            and barbara.y + barbara.h > bullet.y
                            and bullet.y + bullet.h > barbara.y
                            and barbara.lives != 0):
                        barbara.lives -= 1
                        self.score += 20
                        bullet.alive = False
                        self.plane.bullets_p_l.remove(bullet)
                if (barbara.x + barbara.w > self.plane.x
                        and self.plane.x + data.Plane_WIDTH > barbara.x
                        and barbara.y + barbara.h > self.plane.y
                        and self.plane.y + data.Plane_HEIGHT > barbara.y
                        and barbara.alive is True and self.plane.lives != 0
                        and self.plane.loop is False):
                    self.plane.lives -= 1
                    barbara.alive = False
                # when a barbara's bullet touch the player, he will lose a live
                for bullet in barbara.bullets_b_l:
                    if (self.plane.x + self.plane.w > bullet.x
                            and bullet.x + bullet.w > self.plane.x
                            and self.plane.y + self.plane.h > bullet.y
                            and bullet.y + bullet.h > self.plane.y
                            and self.plane.lives != 0
                            and self.plane.loop is False):
                        self.plane.lives -= 1
                        bullet.alive = False
                        if not bullet.alive:
                            barbara.bullets_b_l.remove(bullet)

                if barbara.lives == 0:
                    self.score += 40
                    barbara.alive = False
                if barbara.collision is True:
                    self.enemies.list_b.remove(barbara)

            # If the plane has already collided the game will end
            if self.plane.collision is True:
                self.game_over = True

        # When the game is over all the variables return to its initial state
        if self.game_over:
            self.plane.lives = 3
            self.enemies.list_j.clear()
            self.enemies.list_d.clear()
            self.enemies.list_l.clear()
            self.enemies.list_b.clear()
            for enemy in self.enemies.list_j:
                enemy.bullets_j_l.clear()
            for enemy in self.enemies.list_l:
                enemy.bullets_l_l.clear()
            for enemy in self.enemies.list_d:
                enemy.bullets_d_l.clear()
            self.plane.bullets_p_l.clear()
            self.plane.b = False
            self.plane.collision = False
            self.plane.bonus = False
            self.enemies.damaged = 0
            self.enemies.dead = 0
            self.plane.double_shoot = False

    def draw(self):
        """ This is executed also each frame, here you should just draw
        things """
        # Initial screen
        pyxel.cls(0)
        if time.time() - self.t < 2:
            pyxel.text(self.width / 2 - 20, self.height / 2 - 20, "WELCOME",
                       pyxel.frame_count % 16)
        if 2 <= time.time() - self.t <= 3:
            pyxel.text(self.width / 2 - 10, self.height / 2 - 10, "TO",
                       pyxel.frame_count % 16)
        if 3 <= time.time() - self.t <= 4:
            pyxel.text(self.width / 2 - 10, self.height / 2, "1942",
                       pyxel.frame_count %
                       16)
        if time.time() - self.t > 4:
            pyxel.text(55, self.height / 2 + 10, "Press S to start the game",
                       pyxel.frame_count % 16)
            pyxel.text(90, self.height - 10, "Press Q to quit the game", 12)
            pyxel.text(90, self.height - 20, "Press F to see the features", 12)

        # Features screen
        if self.features:
            pyxel.cls(0)
            pyxel.text(self.width / 2 - 20, 10, "GAME FEATURES",
                       pyxel.frame_count % 16)
            pyxel.text(5, 30, "RIGHT ARROW : Move right\nLEFT ARROW : "
                              "Move left\nUP ARROW : Move up\nDOWN ARROW : "
                              "Move down\nKEY SPACE : Shoot\nKEY Z : "
                              "Make a loop and get invincible\n", 12)
            pyxel.text(5, 80, "ENEMIES INFORMATION", 9)
            pyxel.text(5, 100, "REGULAR ENEMIES: Points "
                               "= 10, Lives = 1\nRED ENEMIES: "
                               "Points = 10, Lives = 1\nBOMBARDIER: "
                               "Points = 10(20 kill), Lives = 5\nSUPER "
                               "BOMBARDIER: Points = 10(20 kill),Lives=15 ",
                       12)
            pyxel.text(90, self.height - 20, "Press S to start the game",
                       pyxel.frame_count % 16)
            pyxel.text(90, self.height - 10, "Press Q to quit the game", 12)

        if self.start:
            # To draw the infinite loop animation
            y = pyxel.frame_count
            pyxel.cls(1)
            pyxel.blt(0, y - 250 * (pyxel.frame_count // 250), 2, 0, 0, 200,
                      250)
            pyxel.blt(0, y - 250 * (pyxel.frame_count // 250 + 1), 2, 0, 0,
                      200, 250)
            # Game animations
            pyxel.text(10, 10, "Score: " + str(self.score), 0)
            pyxel.text(150, 10, "Lives: " + str(self.plane.lives), 0)
            self.plane.draw()
            self.enemies.draw()

        if self.game_over:
            # game over screen animations
            pyxel.cls(0)
            pyxel.text(84, self.height / 2, "GAME OVER", 10)
            pyxel.text(84, self.height / 2 + 10, "Score:" + str(self.score),
                       12)
            pyxel.text(85, self.height - 10, "Press Q to quit the game", 12)
            pyxel.text(85, self.height - 20, "Press S to continue the game",
                       12)

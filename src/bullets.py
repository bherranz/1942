
import pyxel
import data


class Bullets_p:
    """This class contains information about the bullets"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = data.BULLET_p_WIDTH
        self.h = data.BULLET_p_HEIGHT
        self.alive = True
        self.double_shoot = False

    def update(self):
        """The bullets move along the y axis with vertical direction from
        the position of the plane until it collides with the enemy"""
        self.y -= data.BULLET_p_SPEED
        return self.y

    def draw(self):
        """This function stores the graphical information about the bullets
        x and y should be the positions of the plane"""
        if self.alive is True:
            if not self.double_shoot:
                pyxel.blt(self.x + 5, self.y - 7, 0, 103, 84, self.w,
                          self.h, 8)
            else:
                self.w = 18
                self.h = 12
                pyxel.blt(self.x, self.y - 7, 0, 139, 82, self.w,
                          self.h, 8)

class Bullets_e:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.w = data.BULLET_e_WIDTH
        self.h = data.BULLET_e_HEIGHT
        self.alive = True


    def update(self):
        """The bullets move along the y axis with vertical direction from
        the position of the plane until it collides with the plane"""
        self.y += data.BULLET_e_SPEED
        return self.y

    def draw(self):
        """This function stores the graphical information about the bullets
        x and y should be the positions of the enemies"""
        if self.alive is True:
            pyxel.blt(self.x, self.y, 0, 122, 90, self.w,
                      self.h, 8)

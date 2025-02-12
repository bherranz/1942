
import time
from javi import Javi
from diego import Diego
from liang import Liang
from barbara import Barbara
import random

class Enemies:
    """This class contains the information of every type of enemies"""
    def __init__(self):
        self.list_j = []
        self.list_d = []
        self.list_l = []
        self.list_b = []
        self.dead = 0
        self.a = time.time()
        self.b = time.time()
        self.c = time.time()
        self.l1 = time.time()
        self.l2 = time.time()
        self.count = 0
        self.damaged = 0

    def update(self):
        # Every 4 seconds, 4 javi airplanes will appear
        if time.time() - self.a > 4:
            self.a = time.time()
            for i in range(4):
                self.list_j.append(Javi())
        # Every 10 seconds, one diego airplane will appear
        if time.time() - self.b > 10:
            self.b = time.time()
            self.list_d.append(Diego())
        # 5 Liang airplanes will appear following a circle, when all of them
        # has already appeared a counter l1 will start, the next group of
        # liang airplanes will appear in 12, 15 seconds since l1 is started
        if time.time() - self.l1 > random.randint(12, 15):
            if self.dead == 5:
                self.damaged = 0
                self.dead = 0
            if time.time() - self.l2 > 0.4:
                self.l2 = time.time()
                self.list_l.append(Liang())
                self.count += 1
            if self.count == 5:
                self.count = 0
                self.l1 = time.time()
                if self.dead == 5:
                    self.damaged = 0
                    self.dead = 0
            # Every 25 seconds one barbara airplane will appear
            if time.time() - self.c > 25:
                self.c = time.time()
                self.list_b.append(Barbara())

        for element in self.list_j:
            element.update()

        for element in self.list_d:
            element.update()

        for element in self.list_l:
            element.update()

        for element in self.list_b:
            element.update()

    def draw(self):
        for element in self.list_j:
            element.update()
            element.draw()
        for element in self.list_d:
            element.update()
            element.draw()
        for element in self.list_l:
            element.update()
            element.draw()
        for element in self.list_b:
            element.update()
            element.draw()

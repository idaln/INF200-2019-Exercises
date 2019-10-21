# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


import random as rd


class Walker:
    def __init__(self, x0, h):
        self.x = x0
        self.h = h
        self.steps = 0

    def move(self):
        if rd.randint(0, 1) == 0:
            self.x -= 1
        else:
            self.x += 1

        self.steps += 1

    def is_at_home(self):
        return Walker.get_position(self) == self.h

    def get_position(self):
        return self.x

    def get_steps(self):
        return self.steps

    def walking_process(self):
        while Walker.is_at_home(self) is False:
            Walker.move(self)
        return Walker.get_steps(self)


if __name__ == '__main__':

    distance = [1, 2, 5, 10, 20, 50, 100]
    init_pos = 0
    num_sim = 5

    for dist in distance:
        path_lengths = []
        for num in range(num_sim):
            walker = Walker(init_pos, dist)
            path_lengths.append(walker.walking_process())
        print(f'Distance:{dist:3} -> Path lengths: {path_lengths}')

# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"

from walker_sim import Walker, Simulation
import random


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(self.start, self.home)

    def move(self):
        """
        Makes walker move one step left or right. Whether he walks left or
        right is determined by whether the random number generated is 0 or 1,
        accordingly. Walker is restricted by left and right limit

        """
        if random.randint(0, 1) == 0:
            if self.position > self.left_limit:
                self.position -= 1


        else:
            if self.position < self.right_limit:
                self.position += 1
        self.steps += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home, seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        bounded_walker = BoundedWalker(self.start, self.home, self.left_limit,
                                       self.right_limit)

        return bounded_walker.walking_process()

if __name__ == '__main__':

    num_sim = 20

    start = 0
    home = 20
    seed = 1
    left_limit = [0, -10, -100, -1000, -10000]
    right_limit = 20

    for limit in left_limit:
        walk_simulation = BoundedSimulation(start, home, seed,
                                            limit, right_limit)
        sim = Simulation(start, home, seed)
        print(f' Starting position: {start}, home position: {home},'
              f' seed: {seed} gives length of walks\n'
              f'{walk_simulation.run_simulation(num_sim)}')

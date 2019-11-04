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
        accordingly. Walker is restricted by left and right limit.
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
        while not bounded_walker.is_at_home():
            bounded_walker.move()
        return bounded_walker.get_steps()


if __name__ == '__main__':

    num_sim = 20

    start_pos = 0
    home_pos = 20
    seed_val = 1
    left_lim = [0, -10, -100, -1000, -10000]
    right_lim = 20

    print(f' Starting position: {start_pos}, home position: {home_pos}, '
          f'seed: {seed_val}, right limit: {right_lim}')

    for limit in left_lim:
        walk_simulation = BoundedSimulation(start_pos, home_pos, seed_val,
                                            limit, right_lim)
        print(f'Left limit: {limit} \n'
              f'{walk_simulation.run_simulation(num_sim)}')

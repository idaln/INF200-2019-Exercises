# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"

import random


class Walker:
    """
    Simulates the journey of a walker on his way home in a
    one dimensional world.

    Attributes
    ----------
    position : int
        The walkers current position
    steps: int
        Number of steps needed for walker to achieve current position

    """
    def __init__(self, start, home):
        """
        Parameters
        ----------
        start: int
            Starting position
        home: int
            Home position

        """
        self.position = start
        self.home = home
        self.steps = 0

    def move(self):
        """
        Makes walker move one step left or right. Whether he walks left or
        right is determined by whether the random number generated is 0 or 1,
        accordingly.

        """

        if random.randint(0, 1) == 0:
            self.position -= 1
        else:
            self.position += 1

        self.steps += 1

    def is_at_home(self):
        """
        Checks if the walker is home.

        Returns:
        -------
        bool
            True if the walker is home, False otherwise.

        """
        return self.get_position() == self.home

    def get_position(self):
        """

        Returns:
        -------
        position : int
            Current position

        """
        return self.position

    def get_steps(self):
        """

        Returns
        -------
        steps : int
            Current number of steps

        """
        return self.steps


class Simulation:
    def __init__(self, start, home, seed):
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
        """
        self.start = start
        self.home = home
        random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        walker = Walker(self.start, self.home)
        while not walker.is_at_home():
            walker.move()
        return walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

        return [self.single_walk() for _ in range(num_walks)]


if __name__ == '__main__':

    num_sim = 20

    start = [0, 0, 0, 10, 10, 10]
    home = [10, 10, 10, 0, 0, 0]
    seed = [12345, 12345, 54321, 12345, 12345, 54321]

    for i in range(len(start)):
        walk_simulation = Simulation(start[i], home[i], seed[i])
        print(f' Starting position: {start[i]}, home position: {home[i]},'
              f' seed: {seed[i]} gives length of walks\n'
              f'{walk_simulation.run_simulation(num_sim)}'
        )

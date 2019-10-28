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
    def __init__(self, start, home, seed):
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
        self.seed = seed
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
        return Walker.get_position(self) == self.home

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

    def walking_process(self):
        """

        Returns
        -------
        steps : int
            Number of steps needed for walker to get home.

        """
        while Walker.is_at_home(self) is False:
            Walker.move(self)
        return Walker.get_steps(self)


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
        self.seed = seed
        self.walker = Walker(self.start, self.home)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        return self.walker.walking_process()

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
        list_of_steps = []

        for walk in range(num_walks):
            list_of_steps.append(Simulation.single_walk(self))

        return list_of_steps

# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


class LCGRand:
    def __init__(self, seed):
        """
        Initializes class with constants a and m.

        Parameters
        ----------
        seed: Random seed given by user

        """
        self.a = 7**5
        self.m = 2**31-1
        self.seed = seed

    def rand(self):
        """
        Creates random number using the linear congruential
        generator function.

        Returns
        -------
        random_number: int

        """
        random_number = self.a * self.seed % self.m
        self.seed = random_number
        return random_number


class ListRand:
    def __init__(self, list_of_numbers):
        """
        Initializes function with a counter.

        Parameters
        ----------
        list_of_numbers: List of numbers given by user
        """
        self.list_of_numbers = list_of_numbers
        self.counter = 0

    def rand(self):
        """
        Return numbers in list taken as input, starting with the first
        number. Moves on to the next number as the rand function is called
        again.

        Returns
        -------
        random_number: int

        """
        if self.counter == len(self.list_of_numbers):
            raise RuntimeError
        else:
            random_number = self.list_of_numbers[self.counter]
            self.counter += 1
            return random_number


if __name__ == '__main__':
    lcg_generator = LCGRand(22)
    print(lcg_generator.rand())
    print(lcg_generator.rand())

    listrand_generator = ListRand([4, 5, 612, 555, 87, 12, 45])
    print(listrand_generator.rand())
    print(listrand_generator.rand())

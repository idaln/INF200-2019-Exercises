# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


class LCGrand:
    def __init__(self, seed):
        self.a = 7**5
        self.m = 2**31-1
        self.seed = seed

    def rand(self):
        random_number = self.a * self.seed % self.m
        self.seed = random_number
        return random_number


class ListRand:
    def __init__(self):
        pass

    def rand(self):
        pass

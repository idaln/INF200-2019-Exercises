# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


def test_lcg():

    lcg = LCGRand(346)
    assert lcg.rand() == 5815222
    assert lcg.rand() == 1099672039

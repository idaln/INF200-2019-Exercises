# -*- coding: utf-8 -*-

__author__ = "Ida Lunde Naalsund"
__email__ = "idna@nmbu.no"


class LCGRand:
    """Implementation of a linear congruential generator
    that returns random numbers.
    """

    def __init__(self, seed):
        """Initialises the class with given constants a and m.

        Parameters
        ----------
        seed : int
            The seed that the generating is based on.
        """
        self._hidden_state = seed
        self.slope = 7 ** 5
        self.congruence_class = 2 ** 31 - 1

    def rand(self):
        """Generates a single random number based on a seed given by the user.

        Returns
        -------
        random_number : int
            The generated number.
        """
        self._hidden_state *= self.slope
        self._hidden_state %= self.congruence_class

        return self._hidden_state

    def random_sequence(self, length):

        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        self.rand() : int
            A random number.

        """
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """

        self.generator = random_number_generator.rand
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError('iter can only be called once on same '
                               'RandIter object')

        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError('__next__ method is called before __iter__')

        if self.num_generated_numbers == self.length:
            raise StopIteration('All random numbers have been'
                                'generated')

        self.num_generated_numbers += 1

        return self.generator()


if __name__ == '__main__':
    rand_generator = LCGRand(1)
    for rand in rand_generator.random_sequence(10):
        print(rand)

    for i, rand in enumerate(rand_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break

import numpy as np


class Object:
    position: (int, int)

    def __init__(self, world):
        """
        Set the object position
        """
        self.position = tuple(np.random.randint(world.shape))


class Animal(Object):
    pass


class Food(Object):
    pass


class World:
    def __init__(self, shape=(8, 8)):
        """
        Initialize an empty world of a given shape
        """
        self.data = np.zeros(shape, dtype=np.int8)
        self.shape = self.data.shape


class Engine:
    def __init__(self, world=World()):
        """
        Populate the new world
        """
        self._world = world
        self._animal = Animal(world)
        self._food = [Food(world) for food in range(3)]
        self._update_world_data()
        self._print_world_data()

    def _update_world_data(self):
        """
        Update the world data
        """
        data = self._world.data
        data[self._animal.position] = 1
        for food in self._food:
            data[food.position] = 2

    def _print_world_data(self):
        """
        Hello world
        """
        print(self._world.data)


class Game:
    pass


def main():
    engine = Engine()


if __name__ == "__main__":
    main()

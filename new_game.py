import numpy as np


class Object:
    position: (int, int)

    def __init__(self, world):
        self.position = tuple(np.random.randint(world.shape))


class Animal(Object):
    pass


class Food(Object):
    pass


class World:
    def __init__(self, shape=(8, 8)):
        self.data = np.zeros(shape, dtype=np.int8)
        self.shape = self.data.shape


class Engine:
    def __init__(self, world):
        self._world = world
        self._animal = Animal(world)
        self._food = [Food(world) for _ in range(3)]


class Game:
    pass


def main():
    world = World()
    engine = Engine(world)
    game = Game(engine)


if __name__ == "__main__":
    main()

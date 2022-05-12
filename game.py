import numpy as np


class World:
    """
    Two-dimensional grid-world
    """
    def __init__(self, shape, random=False, dtype=np.int8):
        if random:
            self.data = np.random.randint(0, 3, size=shape, dtype=dtype)
        else:
            self.data = np.zeros(shape, dtype=dtype)
        self.shape = self.data.shape
        self.dtype = dtype
        self._engine = Engine(self)

    def __str__(self):
        return self.data.__str__()


class Engine:
    """
    World Engine
    """
    def __init__(self, world, dtype=np.int8):
        self._world = world
        self.shape = world.shape
        self.dtype = dtype
        self._animal = Animal(world=self._world)
        self._set_animal()

    def _set_animal(self):
        world = self._world.data
        position = self._animal.position
        world[position] = 1

    def _update_world(self, command):
        world = self._world.data
        animal = self._animal

        if command == "11":
           world[animal.position] = 0 
           animal.update_position()
           world[animal.position] = 1
        elif command == "01":
            R = np.array([[0, -1], [1, 0]], dtype=self.dtype)
            animal.update_direction(R)
        elif command == "10":
            L = np.array([[0, 1], [-1, 0]], dtype=self.dtype)
            animal.update_direction(L)
        elif command == "00":
            pass

        animal.step += 1


    def next_state(self):
        command = input()
        self._update_world(command)


class Animal:
    """
    World Animal
    """
    def __init__(self, world, default=True):
        self._world = world
        if default:
            self.position = (2, 3)
            self.direction = np.array((0, 1))
        world._animal = self
        self.step = 0

    
    def update_position(self):
        self.position = tuple((self.position + self.direction) % self._world.shape)


    def update_direction(self, direction):
        self.direction = np.matmul(self.direction, direction)

    def __str__(self):
        return f"{self.step=}\n{self.position=}\n{self.direction=}"

def main():
    world = World((4, 8))
    while True:
        print(world)
        print(world._animal)
        world._engine.next_state()


if __name__ == "__main__":
    main()

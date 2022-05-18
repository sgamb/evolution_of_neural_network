import numpy as np


class World:
    """
    Two-dimensional grid-world
    """
    def __init__(self, shape, dtype=np.int8):
        self.data = np.zeros(shape, dtype=dtype)
        self.shape = self.data.shape
        self.dtype = dtype
        self.state = 0
        self._engine = Engine(self)

    def __str__(self):
        return self.data.__str__()

    @property
    def engine(self):
        return self._engine


def angle(vec1, vec2):
    """
    Measure the angle between the vectors
    """
    scalar = vec1 @ vec2
    print(f"{scalar=}")
    vec1_ = np.linalg.norm(vec1)
    vec2_ = np.linalg.norm(vec2)
    if vec1_ * vec2_ == 0:
        return 0
    cos_a = scalar / (vec1_ * vec2_)
    return np.arccos(cos_a) / np.pi


class Engine:
    """
    Game engine
    """
    def __init__(self, world, dtype=np.int8):
        self._world = world
        self.shape = world.shape
        self.dtype = dtype
        # Initialize an animal and a food
        self._animal = Animal(world)
        self._food = Food()
        # Update the world's data
        world.data[self._animal.position] = 1
        world.data[self._food.position] = 2
        # Update animal sense
        self._update_animal_sense()

    def _update_world(self, command):
        # set local variables
        data = self._world.data
        animal = self._animal
        # FORWARD and UPDATE world data
        if command == "11":
            data[animal.position] = 0 
            animal.go_forward()
            data[animal.position] = 1
        # Right
        elif command == "01":
            animal.turn_right()
        # Left
        elif command == "10":
            animal.turn_left()
        # Stay still
        elif command == "00":
            pass
        animal.last_command = command

    def _update_animal_sense(self):
        food_position = np.array(self._food.position)
        animal_position = np.array(self._animal.position)
        delta_vector = food_position - animal_position
        animal = self._animal
        animal.distance_to_the_nearest_food = np.linalg.norm(delta_vector) / self._world.shape[0]
        animal.angle_to_the_nearest_food = angle(delta_vector, self._animal.direction)

    def next_state(self):
        command = input()
        self._world.state += 1
        self._update_world(command)
        self._update_animal_sense()

    @property
    def animal(self):
        return self._animal


class Animal:
    """
    World Animal
    """
    def __init__(self, world, default=True):
        self.angle_to_the_nearest_food = None
        self.distance_to_the_nearest_food = None
        self._world = world
        if default:
            self.position = (2, 3)
            self.direction = np.array((0, 1))
            self.last_command = "00"
        self.step = 0

    def go_forward(self):
        self.position = tuple(
            (self.position + self.direction) % self._world.shape
        )
        self.step += 1

    def turn_right(self):
        R = np.array([[0, -1], [1, 0]], dtype=self._world.dtype)
        self.update_direction(R)

    def turn_left(self):
        L = np.array([[0, 1], [-1, 0]], dtype=self._world.dtype)
        self.update_direction(L)

    def update_direction(self, direction):
        self.direction = np.matmul(self.direction, direction)

    def __str__(self):
        return f"{self.step=}\n{self.position=}\n{self.direction=}"
    
    def sense(self):
        return (
            self.distance_to_the_nearest_food,
            self.angle_to_the_nearest_food,
        )


class Food:
    """
    Sample world's object
    """
    def __init__(self, default=True):
        if default:
            self.position = (6, 5)


def main():
    world = World((8, 8))
    animal = world.engine.animal
    while True:
        print(world)
        # print animal sense
        print(animal.sense())
        # and animal previous move
        print(animal.last_command)
        world.engine.next_state()


if __name__ == "__main__":
    main()

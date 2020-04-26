import numpy as np
from opensimplex import OpenSimplex

class NoiseMap:
    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.map = self._make_map()

    def _make_map(self):
        gen = OpenSimplex(self.seed)
        the_map = np.zeros((self.height, self.width))

        for y in range(self.height):
            for x in range(self.width):
                nx = x/self.width# - 0.5
                ny = y/self.height# - 0.5

                the_map[y][x] = gen.noise2d(nx, ny)# + (.5 * gen.noise2d(2 * nx, 2 * ny)) + (.25 * gen.noise2d(4 * nx, 4 * ny)) + (.125 * gen.noise2d(
                   # 8 * nx, 8 * ny)) + (.0625 * gen.noise2d(16 * nx, 16 * ny)) + (.03125 * gen.noise2d(32 * nx, 32 * ny))

        return the_map

    def _normalize_map(self, min_val, max_val):
        divisor = max_val-min_val
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] = (self.map[y][x] - min_val)/divisor

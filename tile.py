import numpy as np
from scipy.spatial import ConvexHull


class Tile:
    def __init__(self, vertices):
        self.vertices = vertices
        self.elev = 0
        self.hull = ConvexHull(vertices)
        self.centroid = np.average(vertices, 0)
        self.lowest_neighbor = []

    def _set_elev(self, noise_map):
        self.elev = noise_map[int(self.centroid[1]), int(self.centroid[0])]

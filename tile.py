import numpy as np
from scipy.spatial import ConvexHull


class Tile:
    def __init__(self, vertices, elev=0):
        self.vertices = vertices
        self.elev = elev
        self.hull = ConvexHull(vertices)
        self.centroid = np.average(vertices, 0)

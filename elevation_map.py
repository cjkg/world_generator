import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull, Voronoi, voronoi_plot_2d

class PinkNoiseFactory:
    def __init__(self):
        self.blah = 1

class FractalMap:
    def __init__(self, width, height, seed, scale=150.0, octaves=6, persistence=0.5, lacunarity=2.0):
        self.width = width
        self.height = height
        self.seed = seed
        self.scale = scale
        self.octaves = octaves
        self.persistence = persistence
        self.lacunarity = lacunarity

        #self.array = self._initialize_ndarray()

    def _initialize_ndarray(self):
        # https://medium.com/@yvanscher/playing-with-perlin-noise-generating-realistic-archipelagos-b59f004d8401
        ndarray = np.zeros((self.height, self.width))
        for y in range(self.height):
            for x in range(self.width):
                ndarray[y][x] = 

        toimage(ndarray).show()
        # return ndarr

fmap = FractalMap(1024, 1024, 0)
fmap._initialize_ndarray()

class VorMap:
    def __init__(self, generator_count, generator_min, generator_max, lloyd_relax):
        self.generator_count = generator_count
        self.generator_min = generator_min
        self.generator_max = generator_max
        self.lloyd_relax = lloyd_relax
        self.voronoi_map = self._set_voronoi()
        self.neighbor_dict = self._initialize_neighbor_dict()
        self.tiles = self._get_tiles()

    def _initialize_neighbor_dict(self):
        """initialize neighbor dict with empty set"""
        neighbor_dict = dict()
        for vert in self.voronoi_map.vertices:
            neighbor_dict[(vert[0], vert[1])] = set()
        return neighbor_dict

    def _get_tiles(self):
        """get tiles and populate their places in the neighbor_dict"""
        tiles = []

        for reg in self.voronoi_map.regions:
            if -1 not in reg and reg != []:
                vertices = self._get_region_vertices(
                    reg, self.voronoi_map.vertices)
                tile = Tile(list(vertices))
                tiles.append(tile)

                for vert in vertices:
                    self.neighbor_dict[(vert)].add(tile)
vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()

vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()
rn tiles
vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()

vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()
_region_vertices(self, region, vertices):
vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()
et the points of a vertex, using the index provided by scipy.spatial"""
vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()
rn list((vertices[r][0], vertices[r][1]) for r in region)
vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()

    def _set_voronoi(self):
        """Create a voronoi map with lloyd_relax many Lloyd Relaxations"""
        vor = Voronoi(np.random.randint(
            self.generator_min, self.generator_max, (self.generator_count, 2)), qhull_options="Qc")

        for r in range(self.lloyd_relax):
            centroids = [
                np.average(
                    self._get_region_vertices(reg, vor.vertices), 0)
                for reg in vor.regions]
            vor = Voronoi(centroids, qhull_options="Qc")

        return vor


class Tile:
    def __init__(self, vertices, elev=0):
        self.vertices = vertices
        self.elev = elev
        self.hull = ConvexHull(vertices)
        self.centroid = np.average(vertices, 0)


vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()

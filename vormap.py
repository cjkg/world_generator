import numpy as np
from scipy.spatial import Voronoi
from tile import Tile

class VorMap:
    def __init__(self, generator_count, generator_min, generator_max, lloyd_relax, game_seed):
        self.generator_count = generator_count
        self.generator_min = generator_min
        self.generator_max = generator_max
        self.lloyd_relax = lloyd_relax
        self.voronoi_map = self._set_voronoi()
        self.neighbor_dict = self._initialize_neighbor_dict()
        self.tiles = self._get_tiles()
        self.seed = game_seed

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
                if self.generator_max >= tile.centroid[0] >= self.generator_min and self.generator_max >= tile.centroid[1] >= self.generator_min: 
                    tiles.append(tile)

                    for vert in vertices:
                        self.neighbor_dict[(vert)].add(tile)

        return tiles

    def _get_region_vertices(self, region, vertices):
        """get the points of a vertex, using the index provided by scipy.spatial"""
        return list((vertices[r][0], vertices[r][1]) for r in region)

    def _set_voronoi(self):
        """Create a voronoi map with lloyd_relax many Lloyd Relaxations"""
        #np.random.seed(seed=self.seed)
        vor = Voronoi(np.random.randint(
            self.generator_min, self.generator_max, (self.generator_count, 2)), qhull_options="Qc")

        for r in range(self.lloyd_relax):
            centroids = [
                np.average(
                    self._get_region_vertices(reg, vor.vertices), 0)
                for reg in vor.regions]
            vor = Voronoi(centroids, qhull_options="Qc")

        return vor
    
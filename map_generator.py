#import matplotlib.pyplot as plt
#from scipy.spatial import voronoi_plot_2d
from vormap import VorMap
from noisemap import NoiseMap

"""DEBUG FILE"""
map_axis = 256
seed = 426
lloyd_relax = 3
vor = VorMap(map_axis*4, 0, map_axis-1, lloyd_relax, seed)
tiles = vor.tiles
vor_map = vor.voronoi_map
neighbor_dict = vor.neighbor_dict
noise_map = NoiseMap(map_axis, map_axis, seed)
noise_map._normalize_map(-1, 1)

for tile in tiles:
    tile._set_elev(noise_map.map)

for tile in tiles:
    min_vert = tile
    for vert in tile.vertices:
        for neighbor in neighbor_dict[(vert[0], vert[1])]:
            if neighbor.elev < min_vert.elev:
                min_vert = neighbor
                
        tile.lowest_neighbor = min_vert
        

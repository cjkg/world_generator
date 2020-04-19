import matplotlib.pyplot as plt
from scipy.spatial import voronoi_plot_2d
from vormap import VorMap

vor = VorMap(4096, 0, 1024, 5)
voronoi_plot_2d(vor.voronoi_map, show_points=False, show_vertices=False)
plt.show()

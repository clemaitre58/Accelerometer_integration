from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def plot_3d_dist(vect_x, vect_y, vect_z):
    """fonction affichage point 3D après dbl integration

    :vect_x: x 
    :vect_y: y
    :vect_z: z
    :returns: empty

    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(vect_x, vect_y, vect_z)
    plt.show()


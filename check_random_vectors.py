import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def random_vector_of_magnitude_p(p, num_vectors=1):
    """
    Generate random vectors of magnitude p in random directions in 3D.

    Parameters:
    - p: Magnitude of the vectors
    - num_vectors: Number of vectors to generate (default is 1)

    Returns:
    - vectors: An array of shape (num_vectors, 3) containing the random vectors
    """
    # Generate random points on the unit sphere using spherical coordinates
    theta = np.random.uniform(0, 2 * np.pi, num_vectors)
    phi = np.arccos(1 - 2 * np.random.uniform(0, 1, num_vectors))

    # Convert spherical coordinates to Cartesian coordinates
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    # Stack the coordinates into a single array
    unit_vectors = np.stack((x, y, z), axis=-1)

    # Scale by the desired magnitude
    vectors = p * unit_vectors

    return vectors


def plot_vectors(vectors):
    """
    Plot 3D vectors starting from the origin.

    Parameters:
    - vectors: An array of shape (num_vectors, 3) containing the vectors to plot
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot each vector
    for vec in vectors:
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2])

    # Set labels and limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # ax.set_xlim([-p, p])
    # ax.set_ylim([-p, p])
    # ax.set_zlim([-p, p])

    plt.show()


# Example usage
magnitude = 5
num_vectors = 10
vectors = random_vector_of_magnitude_p(magnitude, num_vectors)
plot_vectors(vectors)


print(vectors.shape)

print(np.sqrt(vectors[:, 0]**2 + vectors[:, 1]**2 + vectors[:, 2]**2))

print(vectors)
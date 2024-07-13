import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_random_3d_boxes(num_boxes, box_size_range, space_range):
    boxes = []
    for _ in range(num_boxes):
        center = np.random.uniform(low=space_range[0], high=space_range[1], size=3)
        size = np.random.uniform(low=box_size_range[0], high=box_size_range[1], size=3)
        boxes.append((center, size))
    return boxes

def create_box(center, size):
    cx, cy, cz = center
    sx, sy, sz = size
    vertices = [
        [cx - sx / 2, cy - sy / 2, cz - sz / 2],
        [cx + sx / 2, cy - sy / 2, cz - sz / 2],
        [cx + sx / 2, cy + sy / 2, cz - sz / 2],
        [cx - sx / 2, cy + sy / 2, cz - sz / 2],
        [cx - sx / 2, cy - sy / 2, cz + sz / 2],
        [cx + sx / 2, cy - sy / 2, cz + sz / 2],
        [cx + sx / 2, cy + sy / 2, cz + sz / 2],
        [cx - sx / 2, cy + sy / 2, cz + sz / 2],
    ]
    return vertices

def plot_3d_boxes(boxes):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for center, size in boxes:
        vertices = create_box(center, size)
        faces = [
            [vertices[j] for j in [0, 1, 2, 3]],
            [vertices[j] for j in [4, 5, 6, 7]],
            [vertices[j] for j in [0, 1, 5, 4]],
            [vertices[j] for j in [2, 3, 7, 6]],
            [vertices[j] for j in [1, 2, 6, 5]],
            [vertices[j] for j in [4, 7, 3, 0]],
        ]
        ax.add_collection3d(Poly3DCollection(faces, alpha=0.25, linewidths=1, edgecolors='r'))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')


    # Setting the view limits to zoom out
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([-20, 20])

    plt.show()

# Parameters
num_boxes = 10
box_size_range = (1, 3)  # Minimum and maximum box size
space_range = (-10, 10)  # Space in which to place the boxes

# Generate and plot boxes
random_boxes = generate_random_3d_boxes(num_boxes, box_size_range, space_range)
plot_3d_boxes(random_boxes)

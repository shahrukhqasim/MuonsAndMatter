import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def build_box(z1, z2):
    # Define the z-coordinates
    # z1, z2 = 0, 10

    # Define the size along x and y axes
    size = np.random.uniform(1, 5)

    # Define the coordinates of the first box
    x1, y1 = -size / 2, -size / 2
    x2, y2 = size / 2, size / 2

    # Define the coordinates of the second box, adjacent to the first box along the x-axis
    x3, y3 = x2, y1
    x4, y4 = x3 + size, y2

    x1 = x1 - size / 2
    x2 = x2 - size / 2
    x3 = x3 - size / 2
    x4 = x4 - size / 2

    # Define the vertices of the first box
    vertices1 = [
        [(x1, y1, z1), (x2, y1, z1), (x2, y2, z1), (x1, y2, z1)],  # Bottom face
        [(x1, y1, z2), (x2, y1, z2), (x2, y2, z2), (x1, y2, z2)],  # Top face
        [(x1, y1, z1), (x1, y1, z2), (x1, y2, z2), (x1, y2, z1)],  # Side face
        [(x2, y1, z1), (x2, y1, z2), (x2, y2, z2), (x2, y2, z1)],  # Side face
        [(x1, y1, z1), (x2, y1, z1), (x2, y1, z2), (x1, y1, z2)],  # Side face
        [(x1, y2, z1), (x2, y2, z1), (x2, y2, z2), (x1, y2, z2)],  # Side face
    ]

    # Define the vertices of the second box
    vertices2 = [
        [(x3, y3, z1), (x4, y3, z1), (x4, y4, z1), (x3, y4, z1)],  # Bottom face
        [(x3, y3, z2), (x4, y3, z2), (x4, y4, z2), (x3, y4, z2)],  # Top face
        [(x3, y3, z1), (x3, y3, z2), (x3, y4, z2), (x3, y4, z1)],  # Side face
        [(x4, y3, z1), (x4, y3, z2), (x4, y4, z2), (x4, y4, z1)],  # Side face
        [(x3, y3, z1), (x4, y3, z1), (x4, y3, z2), (x3, y3, z2)],  # Side face
        [(x3, y4, z1), (x4, y4, z1), (x4, y4, z2), (x3, y4, z2)],  # Side face
    ]


    box_1_sz = z2 - z1
    box_1_sx = size
    box_1_sy = size
    box_1_px = size/2
    box_1_py = 0
    box_1_pz = (z2 + z1) / 2

    box_2_sz = z2 - z1
    box_2_sx = size
    box_2_sy = size
    box_2_px = -size/2
    box_2_py = 0
    box_2_pz = (z2 + z1) / 2

    d1 = {
        'sz' : box_1_sz,
        'sx' : box_1_sx,
        'sy' : box_1_sy,
        'px' : box_1_px,
        'py' : box_1_py,
        'pz' : box_1_pz,
    }

    d2 = {
        'sz' : box_2_sz,
        'sx' : box_2_sx,
        'sy' : box_2_sy,
        'px' : box_2_px,
        'py' : box_2_py,
        'pz' : box_2_pz,
    }



    return (vertices1, d1, vertices2, d2)
#
# box1 = build_box(0, 10)
# box2 = build_box(10.5, 20)
# box3 = build_box(20.5, 30)

# boxes = [box1, box2, box3]

a = np.linspace(0, 40, 12)


boxes = []
for i in range(len(a) -1):
    z1 = a[i]
    z2 = a[i+1]
    boxes += [build_box(z1, z2)]

# Function to plot a box
def plot_box(ax, vertices, dat, color):
    ax.add_collection3d(Poly3DCollection(vertices, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))
    # TODO: Add a small dot at dat['px'], dat['py'], dat['pz']

    print([dat['px']], [dat['py']], [dat['pz']])
    ax.scatter([dat['px']], [dat['py']], [dat['pz']], color='red', s=4)



# Plotting the boxes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for vertices1,d1, vertices2,d2 in boxes:
    # Plot the first box
    plot_box(ax, vertices1, d1, 'cyan')
    # Plot the second box
    plot_box(ax, vertices2, d2, 'magenta')

# Set the limits
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-5, 35])

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

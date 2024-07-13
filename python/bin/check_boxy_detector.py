import json
import time

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from muon_slabs import add, simulate_muon, initialize, collect, set_field_value, set_kill_momenta, kill_secondary_tracks, visualize
import random

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

# Function to plot a box
def plot_box(ax, vertices, dat, color):
    vertices_2 = [[(element[2], element[0], element[1]) for element in sublist] for sublist in vertices]
    ax.add_collection3d(Poly3DCollection(vertices_2, facecolors=color, linewidths=0.1, edgecolors='r', alpha=.1))
    # TODO: Add a small dot at dat['px'], dat['py'], dat['pz']

    print([dat['px']], [dat['py']], [dat['pz']])
    # ax.scatter([dat['pz']], [dat['px']], [dat['py']], color='red', s=4)


def build_boxy_detector():
    start_z = -20
    end_z = 20


    a = np.linspace(start_z, end_z, 12)

    detector = {
        'worldPositionX' : 0,
        'worldPositionY' : 0,
        'worldPositionZ' : 0,
        'worldSizeX' : 11,
        'worldSizeY' : 11,
        'worldSizeZ' : end_z - start_z + 10,
        'components': []
    }

    boxes = []
    for i in range(len(a) - 1):
        z1 = a[i]
        z2 = a[i + 1]
        new_box = build_box(z1, z2)
        boxes += [new_box]
        detector['components'].append(
            {
                'sizeX' : new_box[1]['sx'],
                'sizeY' : new_box[1]['sy'],
                'sizeZ' : new_box[1]['sz'],
                'posX' : new_box[1]['px'],
                'posY' : new_box[1]['py'],
                'posZ' : new_box[1]['pz'],
                'fieldX' : 0,
                'fieldY' : 3,
                'fieldZ' : 0,
                'material': 'G4_Fe'
            }
        )
        detector['components'].append(
            {
                'sizeX' : new_box[3]['sx'],
                'sizeY' : new_box[3]['sy'],
                'sizeZ' : new_box[3]['sz'],
                'posX' : new_box[3]['px'],
                'posY' : new_box[3]['py'],
                'posZ' : new_box[3]['pz'],
                'fieldX' : 0,
                'fieldY' : -3,
                'fieldZ' : 0,
                'material': 'G4_Fe'
            }
        )


    return boxes, detector



def main():
    boxes, detector = build_boxy_detector()

    # Plotting the boxes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vertices1, d1, vertices2, d2 in boxes:
        # Plot the first box
        plot_box(ax, vertices1, d1, 'cyan')
        # Plot the second box
        plot_box(ax, vertices2, d2, 'magenta')

    # Set the limits
    ax.set_xlim([-20, 20])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    # Set labels
    ax.set_xlabel('Z (m)')
    ax.set_ylabel('X (m)')
    ax.set_zlabel('Y (m)')

    # plt.show()
    # Initialize muon simulation

    print(json.dumps(detector))

    initialize(0, 4, 4, 5, json.dumps(detector))

    with open('../../data/boxy.json', 'w') as f:
        json.dump(detector, f)

    print("Here")
    set_field_value(1, 0, 0)
    print("Here 2")
    set_kill_momenta(65)
    kill_secondary_tracks(True)
    print("Done")
    # visualize() this does not really work :/

    muon_data = []
    for i in range(10):
        charge = np.random.randint(2) - 1
        # momenta = np.maximum(10., np.random.normal(40.,10.))
        # momenta = -momenta
        simulate_muon(0, 0, -100, charge, np.random.normal(0,1), np.random.normal(0,1), 20)
        data = collect()
        muon_data += [data]

    do_timing_study = False

    if do_timing_study:
        for j in range(10):
            t1 = time.time()
            for i in range(100):
                simulate_muon(0, 0, -70, -1, 1, 1, 20)
            print("Took", time.time() - t1, "seconds.")

    colors = plt.cm.get_cmap('tab10', 10)  # Get a colormap with 10 colors

    for i, data in enumerate(muon_data):
        x = data['x']
        y = data['y']
        z = data['z']
        # Check if the number of items is more than 20
        if len(x) > 20:
            # Calculate the step size for downsampling
            step = len(x) // 20
            # Select elements at regular intervals
            x = x[::step][:20]
            y = y[::step][:20]
            z = z[::step][:20]

        # print(data)

        ax.plot(z, x, y, color=colors(i), label=f'Muon {i + 1}')
        # ax.scatter(z, x, y, s=10, color=colors(i), label=f'Muon {i + 1}')

    # Set labels and title
    # ax.set_xlabel('X Coordinate (m)')
    # ax.set_ylabel('Y Coordinate (m)')
    # ax.set_zlabel('Z Coordinate (m)')
    ax.set_title('3D Scatter Plot of Muon Simulation Data')

    # Add legend
    # ax.legend()

    # Show plot
    plt.show()


if __name__ == '__main__':
    main()
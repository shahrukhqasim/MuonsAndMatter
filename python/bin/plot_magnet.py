import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_magnet(detector, output_file='plots/detector_visualization.png',
                muon_data = [], z_bias =50,sensitive_film_position = 57,
                fixed_zlim:bool = False):
    magnets = detector['magnets']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for mag in magnets:
        z1 = -mag['dz']
        z2 = +mag['dz']

        for i, component in enumerate(mag['components']):
            the_dat = component['corners']
            field = component['field']
            col = 'purple'
            if field[0] < 0:
                col = 'red'
            elif field[0] > 0:
                col = 'green'
            elif field[1] < 0:
                col = 'red'
            elif field[1] > 0:
                col = 'green'
            elif field[2] < 0:
                col = 'blue'
            elif field[2] > 0:
                col = 'blue'
            corners = np.array(
                [
                    [the_dat[0], the_dat[1], z1], [the_dat[2], the_dat[3], z1], [the_dat[4], the_dat[5], z1], [the_dat[6], the_dat[7], z1],
                    [the_dat[0 + 8], the_dat[1 + 8], z2], [the_dat[2 + 8], the_dat[3 + 8], z2], [the_dat[4 + 8], the_dat[5 + 8], z2], [the_dat[6 + 8], the_dat[7 + 8], z2],
                    ]
            )
            
            corners[:, 2] += mag['z_center']
            corners = np.array([[c[2], c[0], c[1]] for c in corners])
            # Define the 12 edges connecting the corners
            edges = [[corners[j] for j in [0, 1, 2, 3]],
                        [corners[j] for j in [4, 5, 6, 7]],
                        [corners[j] for j in [0, 1, 5, 4]],
                        [corners[j] for j in [2, 3, 7, 6]],
                        [corners[j] for j in [0, 3, 7, 4]],
                        [corners[j] for j in [1, 2, 6, 5]]]

            # # Plot the edges
            ax.add_collection3d(Poly3DCollection(edges, facecolors=col, linewidths=0.07, edgecolors='r', alpha=.25))
            #
            # # Scatter plot of the corners
            # ax.scatter3D(corners[:, 0], corners[:, 1], corners[:, 2], color='b', s=0.04)

    if "sensitive_film" in detector:
        cz, cx, cy = detector["sensitive_film"]["z_center"], 0, 0

        # Calculate the half-sizes
        hw = detector["sensitive_film"]["dx"] / 2
        hl = detector["sensitive_film"]["dy"] / 2
        hh = detector["sensitive_film"]["dz"] / 2

        # Define the vertices of the box
        vertices = np.array([
            [cz - hh, cx - hw, cy - hl, ],
            [cz - hh, cx + hw, cy - hl, ],
            [cz - hh, cx + hw, cy + hl, ],
            [cz - hh, cx - hw, cy + hl, ],
            [cz + hh, cx - hw, cy - hl, ],
            [cz + hh, cx + hw, cy - hl, ],
            [cz + hh, cx + hw, cy + hl, ],
            [cz + hh, cx - hw, cy + hl, ],
        ])

        # Define the edges of the box
        edges = [
            [vertices[j] for j in [0, 1, 2, 3]],  # bottom face
            [vertices[j] for j in [4, 5, 6, 7]],  # top face
            [vertices[j] for j in [0, 1, 5, 4]],  # front face
            [vertices[j] for j in [2, 3, 7, 6]],  # back face
            [vertices[j] for j in [1, 2, 6, 5]],  # right face
            [vertices[j] for j in [0, 3, 7, 4]],  # left face
        ]
        box = Poly3DCollection(edges, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25)
        ax.add_collection3d(box)

    colors = plt.cm.get_cmap('tab10', 10)  # Get a colormap with 10 colors
    total_sensitive_hits = 0
    for i, data in enumerate(muon_data):
        x = data['x']
        y = data['y']
        z = data['z']

        if 'pdg_id' in data: 
            particle = data['pdg_id']  
        else: particle = 13
        total_sensitive_hits += len(data['x'])
        # print(len(x))
        # # Check if the number of items is more than 20
        # if len(x) > 20:
        #     # Calculate the step size for downsampling
        #     step = len(x) // 20
        #     # Select elements at regular intervals
        #     x = x[::step][:20]
        #     y = y[::step][:20]
        #     z = z[::step][:20]

        # print(data)
        ax.scatter(z[particle>0], x[particle>0], y[particle>0], color='red', label=f'Muon {i + 1}', s=3)
        ax.scatter(z[particle<0], x[particle<0], y[particle<0], color='green', label=f'AntiMuon {i + 1}', s=3)

    if fixed_zlim: ax.set_xlim(-30+z_bias+sensitive_film_position, detector['magnets'][0]['z_center'] - detector['magnets'][0]['dz']-5)
    else: ax.set_xlim(30, -15)
    ax.set_ylim(-20, 20)
    ax.set_zlim(-20, 20)

    # Adjust the view angle and zoom level
    # ax.view_init(elev=20., azim=30)  # Adjust elevation and azimuth
    # ax.dist = 6 # Smaller values zoom in, larger values zoom out

    ax.set_xlabel('Z (m)')
    ax.set_ylabel('X (m)')
    ax.set_zlabel('Y (m)')
    #ax.view_init(elev=17., azim=126)
    ax.view_init(elev=17., azim=90)
    fig.tight_layout()
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)

    if output_file is not None and output_file != '':
        fig.savefig(output_file, dpi=600, bbox_inches='tight', pad_inches=0)

    print("Total sensitive hits plotted", total_sensitive_hits)
    plt.close()
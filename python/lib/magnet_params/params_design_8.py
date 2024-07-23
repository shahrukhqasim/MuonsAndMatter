import numpy as np
from lib.ship_muon_shield import get_design as generic_design

# Design 8
def get_design(z_bias=50., force_remove_magnetic_field=False):
    mag_unit =  10.000000
    # nMagnets 9

    params = [70, 170, 0, 353.078, 125.083, 184.834, 150.193, 186.812, 40, 40, 150, 150, 2, 2, 80, 80, 150, 150, 2, 2,
              72, 51, 29, 46, 10, 7, 45.6888, 45.6888, 22.1839, 22.1839, 27.0063, 16.2448, 10, 31, 35, 31, 51, 11,
              24.7961, 48.7639, 8, 104.732, 15.7991, 16.7793, 3, 100, 192, 192, 2, 4.8004, 3, 100, 8, 172.729, 46.8285,
              2]

    shield = generic_design(params)
    print(shield)

    magnets_2 = []
    for mag in shield['magnets']:
        mag['dz'] = mag['dz'] / 100.
        mag['z_center'] = mag['z_center'] / 100. + z_bias
        components_2 = mag['components']
        print(components_2)

        if force_remove_magnetic_field:
            multiplier = 0
        else:
            multiplier = 1/mag_unit

        components_2 = [{'corners': (np.array(x['corners']) / 100.).tolist(),
                         'field': (x['field'][0] * multiplier, x['field'][1] *multiplier, x['field'][2] *multiplier)} for x
                        in components_2]
        mag['components'] = components_2
        mag['material'] = 'G4_Fe'
        mag['fieldX'] = 0.
        mag['fieldY'] = 0.
        mag['fieldZ'] = 0.
        magnets_2.append(mag)
    shield['magnets'] = magnets_2

    print(shield)
    shield.update({
        "worldPositionX": 0, "worldPositionY": 0, "worldPositionZ": 0, "worldSizeX": 11, "worldSizeY": 11,
        "worldSizeZ": 100,
        "type" : 1,
        "limits" : {
            "max_step_length": -1,
            "minimum_kinetic_energy": -1
        }
    })


    return shield
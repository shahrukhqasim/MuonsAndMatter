import numpy as np
from lib.ship_muon_shield import design_muon_shield
import json
import time
from lib.reference_designs.params_design_8_ref import get_design as get_design_8_ref

DEF_PARAMS = np.array([70.0, 170.0, 208.0, 207.0, 281.0, 248.0, 305.0,
242.0, 40.0, 40.0, 150.0, 150.0, 2.0, 2.0, 80.0, 80.0, 150.0, 150.0, 2.0, 2.0,
72.0, 51.0, 29.0, 46.0, 10.0, 7.0, 54.0, 38.0, 46.0, 192.0, 14.0, 9.0, 10.0,
31.0, 35.0, 31.0, 51.0, 11.0, 3.0, 32.0, 54.0, 24.0, 8.0, 8.0, 22.0, 32.0,
209.0, 35.0, 8.0, 13.0, 33.0, 77.0, 85.0, 241.0, 9.0, 26.0])
# Design 8
def get_design(params=DEF_PARAMS,z_bias=50.,force_remove_magnetic_field=False):
    mag_unit =  10.000000
    # nMagnets 9
    if len(params)==42:
        params = np.insert(params,0,[70.0, 170.0])
        params = np.insert(params,8,[40.0, 40.0, 150.0, 150.0, 2.0, 2.0, 80.0, 80.0, 150.0, 150.0, 2.0, 2.0])
        
    shield = design_muon_shield(params)
    # print(shield)

    magnets_2 = []
    max_z = None

    for mag in shield['magnets']:
        mag['dz'] = mag['dz'] / 100.
        mag['z_center'] = mag['z_center'] / 100. + z_bias
        components_2 = mag['components']
        # print(components_2)

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
        new_mz = mag['dz'] / 2 + mag['z_center'] + 0.05
        if max_z is None or new_mz > max_z:
            max_z = new_mz

    shield['magnets'] = magnets_2

    # print(shield)
    shield.update({
        "worldPositionX": 0, "worldPositionY": 0, "worldPositionZ": 0, "worldSizeX": 11, "worldSizeY": 11,
        "worldSizeZ": 100,
        "type" : 1,
        "limits" : {
            "max_step_length": -1,
            "minimum_kinetic_energy": -1
        },
        "sensitive_film": {
            "z_center": new_mz,
            "dz": 0.01,
            "dx": 3,
            "dy": 3,
        }
    })


    return shield



def convert_numpy_to_list(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_numpy_to_list(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_to_list(i) for i in obj]
    else:
        return obj



# Just a test case to verify the code against what we get from FairShip
if __name__ == "__main__":
    # params = np.array([70.0, 170.0, 208.0, 207.0, 281.0, 248.0, 305.0,
    #           242.0, 40.0, 40.0, 150.0, 150.0, 2.0, 2.0, 80.0, 80.0, 150.0, 150.0, 2.0, 2.0,
    #           72.0, 51.0, 29.0, 46.0, 10.0, 7.0, 54.0, 38.0, 46.0, 192.0, 14.0, 9.0, 10.0,
    #           31.0, 35.0, 31.0, 51.0, 11.0, 3.0, 32.0, 54.0, 24.0, 8.0, 8.0, 22.0, 32.0,
    #           209.0, 35.0, 8.0, 13.0, 33.0, 77.0, 85.0, 241.0, 9.0, 26.0])
    #params = [70, 170, 0, 353.078, 125.083, 184.834, 150.193, 186.812, 40, 40, 150, 150, 2, 2, 80, 80, 150, 150, 2, 2,
    #          72, 51, 29, 46, 10, 7, 45.6888, 45.6888, 22.1839, 22.1839, 27.0063, 16.2448, 10, 31, 35, 31, 51, 11,
    #          24.7961, 48.7639, 8, 104.732, 15.7991, 16.7793, 3, 100, 192, 192, 2, 4.8004, 3, 100, 8, 172.729, 46.8285,
    #          2]
    

    t1 = time.time()
    shield = get_design(z_bias=50)
    shield_ref = get_design_8_ref(z_bias=50)

    magnets = shield['magnets']
    magnets_ref = shield_ref['magnets']

    for mag, mag_ref in zip(magnets, magnets_ref):
        # print(mag)
        components, components_ref = mag['components'], mag_ref['components']
        for c, c_ref in zip(components, components_ref):
            corners = np.array(c['corners'])
            corners_ref = np.array(c_ref['corners'])
            err = np.mean(np.abs((corners-corners_ref)/(corners_ref+0.000001)))
            assert err < 1e-5

            field = np.array(c['field'])
            field_ref = np.array(c_ref['field'])
            err = np.mean(np.abs((field-field_ref)/(field_ref+0.000001)))
            assert err < 1e-5
    print("Test passed")
    print(shield)
    print(shield_ref)

    print("Took", time.time() - t1, "seconds.")
    print(shield)
    print(json.dumps(convert_numpy_to_list(shield)))



    with open('data/shield.json', 'w') as f:
        json.dump(convert_numpy_to_list(shield), f)
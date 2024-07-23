# Design 8
# nMagnets 9
import numpy as np

def get_design(z_bias=50., force_remove_magnetic_field=False):
    mag_unit = 10.
    magnets = []

    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'MagnAbsorb2_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -179.9, 0, 179.9, 50, 129.9, 50, -129.9, 0, -179.9, 0, 179.9, 50, 129.9, 50, -129.9],
        'field' : (0.000000, 16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (0.000000, 16.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 179.9, -0, -179.9, -50, -129.9, -50, 129.9, -0, 179.9, -0, -179.9, -50, -129.9, -50, 129.9],
        'field' : (0.000000, 16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (0.000000, 16.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagRetL'
    dat_element['components'].append( {
        'corners': [52, -129.9, 52, 129.9, 102, 179.9, 102, -179.9, 52, -129.9, 52, 129.9, 102, 179.9, 102, -179.9],
        'field' : (0.000000, -16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (0.000000, -16.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagRetR'
    dat_element['components'].append( {
        'corners': [-52, 129.9, -52, -129.9, -102, -179.9, -102, 179.9, -52, 129.9, -52, -129.9, -102, -179.9, -102, 179.9],
        'field' : (0.000000, -16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (0.000000, -16.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagTopLeft'
    dat_element['components'].append( {
        'corners': [50, 130, 0, 180, 102, 180, 52, 130, 50, 130, 0, 180, 102, 180, 52, 130],
        'field' : (16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (16.000000, 0.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagTopRight'
    dat_element['components'].append( {
        'corners': [-52, 130, -102, 180, -0, 180, -50, 130, -52, 130, -102, 180, -0, 180, -50, 130],
        'field' : (-16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (-16.000000, 0.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagBotLeft'
    dat_element['components'].append( {
        'corners': [52, -130, 102, -180, 0, -180, 50, -130, 52, -130, 102, -180, 0, -180, 50, -130],
        'field' : (-16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (-16.000000, 0.000000, 0.000000)
    dat_element['name'] =  'MagnAbsorb2_MagBotRight'
    dat_element['components'].append( {
        'corners': [-50, -130, -0, -180, -102, -180, -52, -130, -50, -130, -0, -180, -102, -180, -52, -130],
        'field' : (16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -5426.000000
    dat_element['field'] = (16.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)



    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'Magn2_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -159.15, 0, 159.15, 45.6888, 22.0839, 45.6888, -22.0839, 0, -159.15, 0, 159.15, 45.6888, 22.0839, 45.6888, -22.0839],
        'field' : (0.000000, 51.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (0.000000, 51.000000, 0.000000)
    dat_element['name'] =  'Magn2_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 159.15, -0, -159.15, -45.6888, -22.0839, -45.6888, 22.0839, -0, 159.15, -0, -159.15, -45.6888, -22.0839, -45.6888, 22.0839],
        'field' : (0.000000, 51.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (0.000000, 51.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagRetL'
    dat_element['components'].append( {
        'corners': [73.6888, -22.0839, 73.6888, 22.0839, 210.755, 159.15, 210.755, -159.15, 62.6888, -22.0839, 62.6888, 22.0839, 199.755, 159.15, 199.755, -159.15],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagRetR'
    dat_element['components'].append( {
        'corners': [-73.6888, 22.0839, -73.6888, -22.0839, -210.755, -159.15, -210.755, 159.15, -62.6888, 22.0839, -62.6888, -22.0839, -199.755, -159.15, -199.755, 159.15],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagTopLeft'
    dat_element['components'].append( {
        'corners': [45.6888, 22.1839, 0, 159.25, 210.755, 159.25, 73.6888, 22.1839, 45.6888, 22.1839, 0, 159.25, 199.755, 159.25, 62.6888, 22.1839],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagTopRight'
    dat_element['components'].append( {
        'corners': [-73.6888, 22.1839, -210.755, 159.25, -0, 159.25, -45.6888, 22.1839, -62.6888, 22.1839, -199.755, 159.25, -0, 159.25, -45.6888, 22.1839],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagBotLeft'
    dat_element['components'].append( {
        'corners': [73.6888, -22.1839, 210.755, -159.25, 0, -159.25, 45.6888, -22.1839, 62.6888, -22.1839, 199.755, -159.25, 0, -159.25, 45.6888, -22.1839],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn2_MagBotRight'
    dat_element['components'].append( {
        'corners': [-45.6888, -22.1839, -0, -159.25, -210.755, -159.25, -73.6888, -22.1839, -45.6888, -22.1839, -0, -159.25, -199.755, -159.25, -62.6888, -22.1839],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 348.078000
    dat_element['z_center'] = -4831.922000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)



    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'Magn4_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -32.6961, 0, 32.6961, 24.7961, 7.9, 24.7961, -7.9, 0, -153.396, 0, 153.396, 48.7639, 104.632, 48.7639, -104.632],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn4_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 32.6961, -0, -32.6961, -24.7961, -7.9, -24.7961, 7.9, -0, 153.396, -0, -153.396, -48.7639, -104.632, -48.7639, 104.632],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagRetL'
    dat_element['components'].append( {
        'corners': [40.7961, -7.9, 40.7961, 7.9, 65.5922, 32.6961, 65.5922, -32.6961, 65.7639, -104.632, 65.7639, 104.632, 114.528, 153.396, 114.528, -153.396],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagRetR'
    dat_element['components'].append( {
        'corners': [-40.7961, 7.9, -40.7961, -7.9, -65.5922, -32.6961, -65.5922, 32.6961, -65.7639, 104.632, -65.7639, -104.632, -114.528, -153.396, -114.528, 153.396],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagTopLeft'
    dat_element['components'].append( {
        'corners': [24.7961, 8, 0, 32.7961, 65.5922, 32.7961, 40.7961, 8, 48.7639, 104.732, 0, 153.496, 114.528, 153.496, 65.7639, 104.732],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagTopRight'
    dat_element['components'].append( {
        'corners': [-40.7961, 8, -65.5922, 32.7961, -0, 32.7961, -24.7961, 8, -65.7639, 104.732, -114.528, 153.496, -0, 153.496, -48.7639, 104.732],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagBotLeft'
    dat_element['components'].append( {
        'corners': [40.7961, -8, 65.5922, -32.7961, 0, -32.7961, 24.7961, -8, 65.7639, -104.732, 114.528, -153.496, 0, -153.496, 48.7639, -104.732],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn4_MagBotRight'
    dat_element['components'].append( {
        'corners': [-24.7961, -8, -0, -32.7961, -65.5922, -32.7961, -40.7961, -8, -48.7639, -104.732, -0, -153.496, -114.528, -153.496, -65.7639, -104.732],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 179.834000
    dat_element['z_center'] = -4043.844000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)



    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'Magn5_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -194.9, 0, 194.9, 3, 191.9, 3, -191.9, 0, -291.9, 0, 291.9, 100, 191.9, 100, -191.9],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn5_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 194.9, -0, -194.9, -3, -191.9, -3, 191.9, -0, 291.9, -0, -291.9, -100, -191.9, -100, 191.9],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagRetL'
    dat_element['components'].append( {
        'corners': [5, -191.9, 5, 191.9, 8, 194.9, 8, -194.9, 105, -191.9, 105, 191.9, 205, 291.9, 205, -291.9],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagRetR'
    dat_element['components'].append( {
        'corners': [-5, 191.9, -5, -191.9, -8, -194.9, -8, 194.9, -105, 191.9, -105, -191.9, -205, -291.9, -205, 291.9],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagTopLeft'
    dat_element['components'].append( {
        'corners': [3, 192, 0, 195, 8, 195, 5, 192, 100, 192, 0, 292, 205, 292, 105, 192],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagTopRight'
    dat_element['components'].append( {
        'corners': [-5, 192, -8, 195, -0, 195, -3, 192, -105, 192, -205, 292, -0, 292, -100, 192],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagBotLeft'
    dat_element['components'].append( {
        'corners': [5, -192, 8, -195, 0, -195, 3, -192, 105, -192, 205, -292, 0, -292, 100, -192],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn5_MagBotRight'
    dat_element['components'].append( {
        'corners': [-3, -192, -0, -195, -8, -195, -5, -192, -100, -192, -0, -292, -205, -292, -105, -192],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 145.193000
    dat_element['z_center'] = -3708.817000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)



    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'Magn6_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -10.9, 0, 10.9, 3, 7.9, 3, -7.9, 0, -272.629, 0, 272.629, 100, 172.629, 100, -172.629],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn6_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 10.9, -0, -10.9, -3, -7.9, -3, 7.9, -0, 272.629, -0, -272.629, -100, -172.629, -100, 172.629],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagRetL'
    dat_element['components'].append( {
        'corners': [50, -7.9, 50, 7.9, 53, 10.9, 53, -10.9, 102, -172.629, 102, 172.629, 202, 272.629, 202, -272.629],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagRetR'
    dat_element['components'].append( {
        'corners': [-50, 7.9, -50, -7.9, -53, -10.9, -53, 10.9, -102, 172.629, -102, -172.629, -202, -272.629, -202, 272.629],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagTopLeft'
    dat_element['components'].append( {
        'corners': [3, 8, 0, 11, 53, 11, 50, 8, 100, 172.729, 0, 272.729, 202, 272.729, 102, 172.729],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagTopRight'
    dat_element['components'].append( {
        'corners': [-50, 8, -53, 11, -0, 11, -3, 8, -102, 172.729, -202, 272.729, -0, 272.729, -100, 172.729],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagBotLeft'
    dat_element['components'].append( {
        'corners': [50, -8, 53, -11, 0, -11, 3, -8, 102, -172.729, 202, -272.729, 0, -272.729, 100, -172.729],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn6_MagBotRight'
    dat_element['components'].append( {
        'corners': [-3, -8, -0, -11, -53, -11, -50, -8, -100, -172.729, -0, -272.729, -202, -272.729, -102, -172.729],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 181.812000
    dat_element['z_center'] = -3371.812000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)



    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] =  'Magn7_MiddleMagL'
    dat_element['components'].append( {
        'corners': [0, -272.629, 0, 272.629, 100, 172.629, 100, -172.629, 0, -272.629, 0, 272.629, 100, 172.629, 100, -172.629],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn7_MiddleMagR'
    dat_element['components'].append( {
        'corners': [-0, 272.629, -0, -272.629, -100, -172.629, -100, 172.629, -0, 272.629, -0, -272.629, -100, -172.629, -100, 172.629],
        'field' : (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (0.000000, -17.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagRetL'
    dat_element['components'].append( {
        'corners': [102, -172.629, 102, 172.629, 202, 272.629, 202, -272.629, 102, -172.629, 102, 172.629, 202, 272.629, 202, -272.629],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagRetR'
    dat_element['components'].append( {
        'corners': [-102, 172.629, -102, -172.629, -202, -272.629, -202, 272.629, -102, 172.629, -102, -172.629, -202, -272.629, -202, 272.629],
        'field' : (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (0.000000, 17.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagTopLeft'
    dat_element['components'].append( {
        'corners': [100, 172.729, 0, 272.729, 202, 272.729, 102, 172.729, 100, 172.729, 0, 272.729, 202, 272.729, 102, 172.729],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagTopRight'
    dat_element['components'].append( {
        'corners': [-102, 172.729, -202, 272.729, -0, 272.729, -100, 172.729, -102, 172.729, -202, 272.729, -0, 272.729, -100, 172.729],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagBotLeft'
    dat_element['components'].append( {
        'corners': [102, -172.729, 202, -272.729, 0, -272.729, 100, -172.729, 102, -172.729, 202, -272.729, 0, -272.729, 100, -172.729],
        'field' : (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (17.000000, 0.000000, 0.000000)
    dat_element['name'] =  'Magn7_MagBotRight'
    dat_element['components'].append( {
        'corners': [-100, -172.729, -0, -272.729, -202, -272.729, -102, -172.729, -100, -172.729, -0, -272.729, -202, -272.729, -102, -172.729],
        'field' : (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    dat_element['field'] = (-17.000000, 0.000000, 0.000000)
    # Magnet finished.
    magnets.append(dat_element)

    magnets_2 = []
    for mag in magnets:
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
    magnets = magnets_2

    detector = {
        "worldPositionX": 0, "worldPositionY": 0, "worldPositionZ": 0, "worldSizeX": 11, "worldSizeY": 11,
        "worldSizeZ": 100,
        "magnets": magnets,
        "type" : 1,
        "limits" : {
            "max_step_length": -1,
            "minimum_kinetic_energy": -1
        }
    }
    return detector


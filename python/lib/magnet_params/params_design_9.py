import numpy as np
#Design 9



def get_design(z_bias=50., force_remove_magnetic_field=False):
    mag_unit =  10.000000
    # nMagnets 9

    magnets = []

    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'MagnAbsorb2_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -179.9, 0, 179.9, 50, 129.9, 50, -129.9, 0, -179.9, 0, 179.9, 50, 129.9, 50, -129.9],
        'field': (0.000000, 16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (0.000000, 16.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 179.9, -0, -179.9, -50, -129.9, -50, 129.9, -0, 179.9, -0, -179.9, -50, -129.9, -50, 129.9],
        'field': (0.000000, 16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (0.000000, 16.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagRetL'
    dat_element['components'].append({
        'corners': [52, -129.9, 52, 129.9, 102, 179.9, 102, -179.9, 52, -129.9, 52, 129.9, 102, 179.9, 102, -179.9],
        'field': (0.000000, -16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (0.000000, -16.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagRetR'
    dat_element['components'].append({
        'corners': [-52, 129.9, -52, -129.9, -102, -179.9, -102, 179.9, -52, 129.9, -52, -129.9, -102, -179.9, -102, 179.9],
        'field': (0.000000, -16.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (0.000000, -16.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagTopLeft'
    dat_element['components'].append({
        'corners': [50, 130, 0, 180, 102, 180, 52, 130, 50, 130, 0, 180, 102, 180, 52, 130],
        'field': (16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (16.000000, 0.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagTopRight'
    dat_element['components'].append({
        'corners': [-52, 130, -102, 180, -0, 180, -50, 130, -52, 130, -102, 180, -0, 180, -50, 130],
        'field': (-16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (-16.000000, 0.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagBotLeft'
    dat_element['components'].append({
        'corners': [52, -130, 102, -180, 0, -180, 50, -130, 52, -130, 102, -180, 0, -180, 50, -130],
        'field': (-16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (-16.000000, 0.000000, 0.000000)
    dat_element['name'] = 'MagnAbsorb2_MagBotRight'
    dat_element['components'].append({
        'corners': [-50, -130, -0, -180, -102, -180, -52, -130, -50, -130, -0, -180, -102, -180, -52, -130],
        'field': (16.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 226.000000
    dat_element['z_center'] = -6468.000000
    # Field: (16.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn1_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -100.9, 0, 100.9, 72, 28.9, 72, -28.9, 0, -96.9, 0, 96.9, 51, 45.9, 51, -45.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn1_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 100.9, -0, -100.9, -72, -28.9, -72, 28.9, -0, 96.9, -0, -96.9, -51, -45.9, -51, 45.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagRetL'
    dat_element['components'].append({
        'corners': [82, -28.9, 82, 28.9, 154, 100.9, 154, -100.9, 59, -45.9, 59, 45.9, 110, 96.9, 110, -96.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagRetR'
    dat_element['components'].append({
        'corners': [-82, 28.9, -82, -28.9, -154, -100.9, -154, 100.9, -59, 45.9, -59, -45.9, -110, -96.9, -110, 96.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagTopLeft'
    dat_element['components'].append({
        'corners': [72, 29, 0, 101, 154, 101, 82, 29, 51, 46, 0, 97, 110, 97, 59, 46],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagTopRight'
    dat_element['components'].append({
        'corners': [-82, 29, -154, 101, -0, 101, -72, 29, -59, 46, -110, 97, -0, 97, -51, 46],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagBotLeft'
    dat_element['components'].append({
        'corners': [82, -29, 154, -101, 0, -101, 72, -29, 59, -46, 110, -97, 0, -97, 51, -46],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn1_MagBotRight'
    dat_element['components'].append({
        'corners': [-72, -29, -0, -101, -154, -101, -82, -29, -51, -46, -0, -97, -110, -97, -59, -46],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 208.000000
    dat_element['z_center'] = -6014.000000
    # Field: (17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn2_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -99.9, 0, 99.9, 54, 45.9, 54, -45.9, 0, -229.9, 0, 229.9, 38, 191.9, 38, -191.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn2_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 99.9, -0, -99.9, -54, -45.9, -54, 45.9, -0, 229.9, -0, -229.9, -38, -191.9, -38, 191.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagRetL'
    dat_element['components'].append({
        'corners': [69, -45.9, 69, 45.9, 123, 99.9, 123, -99.9, 47, -191.9, 47, 191.9, 85, 229.9, 85, -229.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagRetR'
    dat_element['components'].append({
        'corners': [-69, 45.9, -69, -45.9, -123, -99.9, -123, 99.9, -47, 191.9, -47, -191.9, -85, -229.9, -85, 229.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagTopLeft'
    dat_element['components'].append({
        'corners': [54, 46, 0, 100, 123, 100, 69, 46, 38, 192, 0, 230, 85, 230, 47, 192],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagTopRight'
    dat_element['components'].append({
        'corners': [-69, 46, -123, 100, -0, 100, -54, 46, -47, 192, -85, 230, -0, 230, -38, 192],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagBotLeft'
    dat_element['components'].append({
        'corners': [69, -46, 123, -100, 0, -100, 54, -46, 47, -192, 85, -230, 0, -230, 38, -192],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn2_MagBotRight'
    dat_element['components'].append({
        'corners': [-54, -46, -0, -100, -123, -100, -69, -46, -38, -192, -0, -230, -85, -230, -47, -192],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 207.000000
    dat_element['z_center'] = -5589.000000
    # Field: (17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    test_mul = 1
    test_mul = test_mul * 100
    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn3_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -44.9, 0, 44.9, 10, 34.9, 10, -34.9, 0, -61.9, 0, 61.9, 31, 30.9, 31, -30.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn3_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 44.9, -0, -44.9, -10, -34.9, -10, 34.9, -0, 61.9, -0, -61.9, -31, -30.9, -31, 30.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagRetL'
    dat_element['components'].append({
        'corners': [61, -34.9, 61, 34.9, 71, 44.9, 71, -44.9, 42, -30.9, 42, 30.9, 73, 61.9, 73, -61.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagRetR'
    dat_element['components'].append({
        'corners': [-61, 34.9, -61, -34.9, -71, -44.9, -71, 44.9, -42, 30.9, -42, -30.9, -73, -61.9, -73, 61.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagTopLeft'
    dat_element['components'].append({
        'corners': [10, 35, 0, 45, 71, 45, 61, 35, 31, 31, 0, 62, 73, 62, 42, 31],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagTopRight'
    dat_element['components'].append({
        'corners': [-61, 35, -71, 45, -0, 45, -10, 35, -42, 31, -73, 62, -0, 62, -31, 31],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagBotLeft'
    dat_element['components'].append({
        'corners': [61, -35, 71, -45, 0, -45, 10, -35, 42, -31, 73, -62, 0, -62, 31, -31],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn3_MagBotRight'
    dat_element['components'].append({
        'corners': [-10, -35, -0, -45, -71, -45, -61, -35, -31, -31, -0, -62, -73, -62, -42, -31],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 281.000000
    dat_element['z_center'] = -5091.000000
    # Field: (17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn4_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -56.9, 0, 56.9, 3, 53.9, 3, -53.9, 0, -55.9, 0, 55.9, 32, 23.9, 32, -23.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn4_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 56.9, -0, -56.9, -3, -53.9, -3, 53.9, -0, 55.9, -0, -55.9, -32, -23.9, -32, 23.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagRetL'
    dat_element['components'].append({
        'corners': [11, -53.9, 11, 53.9, 14, 56.9, 14, -56.9, 40, -23.9, 40, 23.9, 72, 55.9, 72, -55.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagRetR'
    dat_element['components'].append({
        'corners': [-11, 53.9, -11, -53.9, -14, -56.9, -14, 56.9, -40, 23.9, -40, -23.9, -72, -55.9, -72, 55.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagTopLeft'
    dat_element['components'].append({
        'corners': [3, 54, 0, 57, 14, 57, 11, 54, 32, 24, 0, 56, 72, 56, 40, 24],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagTopRight'
    dat_element['components'].append({
        'corners': [-11, 54, -14, 57, -0, 57, -3, 54, -40, 24, -72, 56, -0, 56, -32, 24],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagBotLeft'
    dat_element['components'].append({
        'corners': [11, -54, 14, -57, 0, -57, 3, -54, 40, -24, 72, -56, 0, -56, 32, -24],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn4_MagBotRight'
    dat_element['components'].append({
        'corners': [-3, -54, -0, -57, -14, -57, -11, -54, -32, -24, -0, -56, -72, -56, -40, -24],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 248.000000
    dat_element['z_center'] = -4552.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn5_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -230.9, 0, 230.9, 22, 208.9, 22, -208.9, 0, -66.9, 0, 66.9, 32, 34.9, 32, -34.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn5_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 230.9, -0, -230.9, -22, -208.9, -22, 208.9, -0, 66.9, -0, -66.9, -32, -34.9, -32, 34.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagRetL'
    dat_element['components'].append({
        'corners': [30, -208.9, 30, 208.9, 52, 230.9, 52, -230.9, 45, -34.9, 45, 34.9, 77, 66.9, 77, -66.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagRetR'
    dat_element['components'].append({
        'corners': [-30, 208.9, -30, -208.9, -52, -230.9, -52, 230.9, -45, 34.9, -45, -34.9, -77, -66.9, -77, 66.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagTopLeft'
    dat_element['components'].append({
        'corners': [22, 209, 0, 231, 52, 231, 30, 209, 32, 35, 0, 67, 77, 67, 45, 35],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagTopRight'
    dat_element['components'].append({
        'corners': [-30, 209, -52, 231, -0, 231, -22, 209, -45, 35, -77, 67, -0, 67, -32, 35],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagBotLeft'
    dat_element['components'].append({
        'corners': [30, -209, 52, -231, 0, -231, 22, -209, 45, -35, 77, -67, 0, -67, 32, -35],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn5_MagBotRight'
    dat_element['components'].append({
        'corners': [-22, -209, -0, -231, -52, -231, -30, -209, -32, -35, -0, -67, -77, -67, -45, -35],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 305.000000
    dat_element['z_center'] = -3989.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn6_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -117.9, 0, 117.9, 33, 84.9, 33, -84.9, 0, -317.9, 0, 317.9, 77, 240.9, 77, -240.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn6_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 117.9, -0, -117.9, -33, -84.9, -33, 84.9, -0, 317.9, -0, -317.9, -77, -240.9, -77, 240.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagRetL'
    dat_element['components'].append({
        'corners': [42, -84.9, 42, 84.9, 75, 117.9, 75, -117.9, 103, -240.9, 103, 240.9, 180, 317.9, 180, -317.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagRetR'
    dat_element['components'].append({
        'corners': [-42, 84.9, -42, -84.9, -75, -117.9, -75, 117.9, -103, 240.9, -103, -240.9, -180, -317.9, -180, 317.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagTopLeft'
    dat_element['components'].append({
        'corners': [33, 85, 0, 118, 75, 118, 42, 85, 77, 241, 0, 318, 180, 318, 103, 241],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagTopRight'
    dat_element['components'].append({
        'corners': [-42, 85, -75, 118, -0, 118, -33, 85, -103, 241, -180, 318, -0, 318, -77, 241],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagBotLeft'
    dat_element['components'].append({
        'corners': [42, -85, 75, -118, 0, -118, 33, -85, 103, -241, 180, -318, 0, -318, 77, -241],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn6_MagBotRight'
    dat_element['components'].append({
        'corners': [-33, -85, -0, -118, -75, -118, -42, -85, -77, -241, -0, -318, -180, -318, -103, -241],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 242.000000
    dat_element['z_center'] = -3432.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.




    # New Magnet:
    dat_element = {}
    dat_element['components'] = []
    dat_element['name'] = 'Magn7_MiddleMagL'
    dat_element['components'].append({
        'corners': [0, -317.9, 0, 317.9, 77, 240.9, 77, -240.9, 0, -317.9, 0, 317.9, 77, 240.9, 77, -240.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn7_MiddleMagR'
    dat_element['components'].append({
        'corners': [-0, 317.9, -0, -317.9, -77, -240.9, -77, 240.9, -0, 317.9, -0, -317.9, -77, -240.9, -77, 240.9],
        'field': (0.000000, -17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (0.000000, -17.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagRetL'
    dat_element['components'].append({
        'corners': [103, -240.9, 103, 240.9, 180, 317.9, 180, -317.9, 103, -240.9, 103, 240.9, 180, 317.9, 180, -317.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagRetR'
    dat_element['components'].append({
        'corners': [-103, 240.9, -103, -240.9, -180, -317.9, -180, 317.9, -103, 240.9, -103, -240.9, -180, -317.9, -180, 317.9],
        'field': (0.000000, 17.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (0.000000, 17.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagTopLeft'
    dat_element['components'].append({
        'corners': [77, 241, 0, 318, 180, 318, 103, 241, 77, 241, 0, 318, 180, 318, 103, 241],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagTopRight'
    dat_element['components'].append({
        'corners': [-103, 241, -180, 318, -0, 318, -77, 241, -103, 241, -180, 318, -0, 318, -77, 241],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagBotLeft'
    dat_element['components'].append({
        'corners': [103, -241, 180, -318, 0, -318, 77, -241, 103, -241, 180, -318, 0, -318, 77, -241],
        'field': (17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (17.000000, 0.000000, 0.000000)
    dat_element['name'] = 'Magn7_MagBotRight'
    dat_element['components'].append({
        'corners': [-77, -241, -0, -318, -180, -318, -103, -241, -77, -241, -0, -318, -180, -318, -103, -241],
        'field': (-17.000000, 0.000000, 0.000000)
    })
    dat_element['dz'] = 10.000000
    dat_element['z_center'] = -3180.000000
    # Field: (-17.000000, 0.000000, 0.000000)
    magnets.append(dat_element)
    # Magnet finished.

    magnets_2 = []
    for mag in magnets:
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




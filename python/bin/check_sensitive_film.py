import time

from muon_slabs import simulate_muon, initialize, collect, set_field_value, kill_secondary_tracks
import json
import numpy as np

detector = {
    "worldPositionX": 0, "worldPositionY": 0, "worldPositionZ": 0, "worldSizeX": 11, "worldSizeY": 11,
    "worldSizeZ": 100,
    "film" : {
        "size_x": 5,
        "size_y": 5,
        "size_z": 0.0001,
        "z_center" : -17,
    }
}


# Initialize muon simulation
initialize(0, 4, 4, 5, 2, json.dumps(detector))

set_field_value(1,0,0)
# set_kill_momenta(65)
kill_secondary_tracks(True)

zpos = -18
for i in range(10000):
    print("Run")
    simulate_muon(0, 0, 20, 0, np.random.normal(0, 0.005), np.random.normal(0, 0.005), zpos)
    time.sleep(1)
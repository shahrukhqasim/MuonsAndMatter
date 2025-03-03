# CUDA Muon Sampling Simulation

## Compile the CUDA package
Starting from the root of the repo
```
source env.sh
cd cuda_muons/faster_muons/faster_muons_torch/
```
build like this:
```
pip3 install -v --user --no-deps --no-build-isolation .
```


## Collect data from Geant4

Study the `collect_step_data_from_geant4.py` file to change paramterers etc.
```
cd cuda_muons/
python3 faster_muons/collect_step_data_from_geant4.py
```
Combine the data with:
```
python3 combine_geant4_data.py
```
And then conver to tfrecords:
```
python3 convert_to_tf_records.py
```
Finally, collect histograms from the tfrecords file:
```
python3 convert_to_tf_records.py
```

Please change these files such that the arguments are taken from command line to make it more consistent.


I'll add more details later.
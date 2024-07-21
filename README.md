# Muon Shield Optimization for the SHiP experiment (2024 and onward)

Warning: The repository is still in very initial phases of development and can change really quickly.

<img src="images/shield.png" alt="Muon Shield Visualization" width="400"/>


## Envrionment
For non-GUI access (such as on servers), download simcontainer2.sif from the following location:

[Containers](https://uzh-my.sharepoint.com/:f:/g/personal/shahrukh_qasim_physik_uzh_ch/En9EVDrRsjpIrBnXWGzLQt0BoT65wN2qzBtGbdEJfapBDA?e=b5b776)

If you are using physik cluster, run the singularity container via the following commands:

```
cd /disk/lhcb_data/`whoami`/images
. /disk/lhcb/scripts/lhcb_setup.sh
export SINGULARITY_TMPDIR=/disk/users/`whoami`/temp
export TMPDIR=/disk/users/`whoami`/tmp
singularity shell --nv -B /cvmfs -B /disk/users/`whoami` -B /run/user/21528 -B /home/hep/`whoami` simcontainer.sif
```

For other clusters, modify the commands accordingly. You should include every directory
you need access to from within the container with `-B` option.

```
git clone git@github.com:shahrukhqasim/MuonsAndMatter.git
```
or 
```
git clone https://github.com/shahrukhqasim/MuonsAndMatter.git
```

```
cd MuonsAndMatter
git submodule update --init --remote --recursive
cd MuonThroughMatter
soure env.sh
```
The following python script will give you the cmake command that you can use:
```
python3 chore/find_cmake_command.py
```
For me, it gave: 
```
Using python: /usr/bin/python3
pybind11 found in: /home/hep/sqasim/.local/lib/python3.10/site-packages/pybind11/share/cmake/pybind11
The following cmake command can be used:
cmake -Dpybind11_DIR=/home/hep/sqasim/.local/lib/python3.10/site-packages/pybind11/share/cmake/pybind11 -DPython_EXECUTABLE=/usr/bin/python3 the/path
```
Take node of the cmake command and run the following commands as per your username:

```
cd cpp/
mkdir build
cmake -Dpybind11_DIR=/home/hep/sqasim/.local/lib/python3.10/site-packages/pybind11/share/cmake/pybind11 -DPython_EXECUTABLE=/usr/bin/python3 ..
make -j
cd ../..
```



## Running visually
```
python3 python/bin/run_full_detector_visually.py
```

## Running multi-core
```
python3 python/bin/run_full_detector_multi_core_2.py --cores 45
```
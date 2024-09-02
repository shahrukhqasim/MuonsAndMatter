export PYTHONPATH=$PYTHONPATH:`readlink -f python`:`readlink -f cpp/build`
python3 chore/find_cmake_command.py
cd cpp/
cd build
cmake -Dpybind11_DIR=/home/hep/lprate/.local/lib/python3.11/site-packages/pybind11/share/cmake/pybind11 -DPython_EXECUTABLE=/usr/bin/python3 ..
make -j
cd ../..
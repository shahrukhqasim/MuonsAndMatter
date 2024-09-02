cd cpp/
cd build
cmake -Dpybind11_DIR=/users/lpratesc/.local/lib/python3.11/site-packages/pybind11/share/cmake/pybind11 -DPython_EXECUTABLE=/usr/bin/python3 ..
make -j
cd ../..
import os.path
import pybind11
import sys

dir = pybind11.__file__
dir = os.path.join(os.path.split(dir)[0], 'share/cmake/pybind11')

print("Using python:", sys.executable)
print("pybind11 found in:",dir)
print("The following cmake command can be used:\n"
      "cmake -Dpybind11_DIR=%s -DPython_EXECUTABLE=%s the/path" % (dir, sys.executable))

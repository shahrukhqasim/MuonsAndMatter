cmake_minimum_required(VERSION 3.12)
project(my_project)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(PYBIND11_FINDPYTHON ON)

# Find pybind11
find_package(pybind11 REQUIRED)
find_package(Geant4 REQUIRED ui_all vis_all)

# Create the Python module
pybind11_add_module(muon_slabs MuonSlabs.cc)

add_executable(MuonSlab main.cc DetectorConstruction.cc PrimaryGeneratorAction.cc)
target_link_libraries(MuonSlab ${Geant4_LIBRARIES})

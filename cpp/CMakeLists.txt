cmake_minimum_required(VERSION 3.12)
project(my_project)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


set(PYBIND11_FINDPYTHON ON)

# Find pybind11
find_package(pybind11 REQUIRED)
find_package(Geant4 REQUIRED ui_all vis_all)
include_directories(/Users/shahrukhqasim/workspace/uzh/Geant4-11.2.2/include/Geant4)

set(SOURCE_FILES
        DetectorConstruction.cc
        PrimaryGeneratorAction.cc
        CustomSteppingAction.cc
        CustomEventAction.cc
        )


add_library(common_sources STATIC ${SOURCE_FILES})

add_executable(MuonSlab main.cc)

# Create the Python module
target_link_libraries(MuonSlab common_sources ${Geant4_LIBRARIES})
#target_link_libraries(muon_slabs ${Geant4_LIBRARIES})

pybind11_add_module(muon_slabs MuonSlabs.cc)
target_link_libraries(muon_slabs PUBLIC common_sources ${Geant4_LIBRARIES})

configure_file(init_vis.mac init_vis.mac COPYONLY)

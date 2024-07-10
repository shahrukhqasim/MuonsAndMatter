#include <pybind11/pybind11.h>
#include "G4PhysicsListHelper.hh"
#include "G4StepLimiterPhysics.hh"
#include "G4UserSpecialCuts.hh"
#include "G4StepLimiter.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4ProcessManager.hh"
#include "G4RunManager.hh"
#include "CustomSteppingAction.hh"
#include "DetectorConstruction.hh"
#include "G4UImanager.hh"
#include "PrimaryGeneratorAction.cc"
#include "FTFP_BERT.hh"
#include "CustomEventAction.hh"
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

namespace py = pybind11;
using namespace py::literals;


G4RunManager* runManager;
G4UImanager *ui_manager;
PrimaryGeneratorAction *primariesGenerator;
DetectorConstruction * detector;
CustomSteppingAction * steppingAction;
//bool collect_full_data;
CLHEP::MTwistEngine *randomEngine;
CustomEventAction *customEventAction;



int add(int a, int b) {
    return a + b;
}

void simulate_muon(double px, double py, double pz, int charge,
                    double x, double y, double z) {
    if (ui_manager == nullptr) {
        G4cout<<"Call initialize(...) before running this function.\n";
        throw std::runtime_error("Forgot to call initialize?");
    }

    primariesGenerator->setNextMomenta(px, py, pz);
    primariesGenerator->setNextPosition(x, y, z);
    primariesGenerator->setNextCharge(charge);

    ui_manager->ApplyCommand(std::string("/run/beamOn ") + std::to_string(1));


}

py::dict collect() {

    std::vector<double>& px = steppingAction->px;
    std::vector<double>& py = steppingAction->py;
    std::vector<double>& pz = steppingAction->pz;

    std::vector<double>& x = steppingAction->x;
    std::vector<double>& y = steppingAction->y;
    std::vector<double>& z = steppingAction->z;

    std::vector<double>& stepLength = steppingAction->stepLength;
    std::vector<double>& chargeDeposit = steppingAction->chargeDeposit;

    std::vector<double> px_copy(px.begin(), px.end());
    std::vector<double> py_copy(py.begin(), py.end());
    std::vector<double> pz_copy(pz.begin(), pz.end());

    std::vector<double> x_copy(x.begin(), x.end());
    std::vector<double> y_copy(y.begin(), y.end());
    std::vector<double> z_copy(z.begin(), z.end());

    std::vector<double> stepLength_copy(stepLength.begin(), stepLength.end());
    std::vector<double> chargeDeposit_copy(chargeDeposit.begin(), chargeDeposit.end());

    py::array np_px = py::cast(px_copy);
    py::array np_py = py::cast(py_copy);
    py::array np_pz = py::cast(pz_copy);

    py::array np_x = py::cast(x_copy);
    py::array np_y = py::cast(y_copy);
    py::array np_z = py::cast(z_copy);

    py::array np_stepLength = py::cast(stepLength_copy);
    py::array np_chargeDeposit = py::cast(chargeDeposit_copy);

    py::dict d = py::dict(
            "px"_a = np_px,
            "py"_a = np_py,
            "pz"_a = np_pz,
            "x"_a = np_x,
            "y"_a = np_y,
            "z"_a = np_z,
            "step_length"_a = np_stepLength,
            "charge_deposit"_a = np_chargeDeposit
    );

    return d;
}

void set_field_value(double strength, double theta, double phi) {
    detector->setMagneticFieldValue(strength, theta, phi);
}

void set_kill_momenta(double kill_momenta) {
    steppingAction->setKillMomenta(kill_momenta);
}

void initialize( int rseed_0,
                 int rseed_1, int rseed_2, int rseed_3) {
    randomEngine = new CLHEP::MTwistEngine(rseed_0);


    long seeds[4] = {rseed_0, rseed_1, rseed_2, rseed_3};

    CLHEP::HepRandom::setTheSeeds(seeds);
    G4Random::setTheSeeds(seeds);

    runManager = new G4RunManager;

    detector = new DetectorConstruction();
    std::cout<<"Detector initializing..."<<std::endl;
    runManager->SetUserInitialization(detector);

    auto physicsList = new FTFP_BERT;
//    physicsList->RegisterPhysics(new G4StepLimiterPhysics());
    runManager->SetUserInitialization(physicsList);

    customEventAction = new CustomEventAction();
    primariesGenerator = new PrimaryGeneratorAction();
    steppingAction = new CustomSteppingAction();
    primariesGenerator->setSteppingAction(steppingAction);
    customEventAction->setSteppingAction(steppingAction);

//    auto actionInitialization = new B4aActionInitialization(detector, eventAction, primariesGenerator);
//    runManager->SetUserInitialization(actionInitialization);

    runManager->SetUserAction(primariesGenerator);
    runManager->SetUserAction(steppingAction);
    runManager->SetUserAction(customEventAction);

    // Get the pointer to the User Interface manager
    ui_manager = G4UImanager::GetUIpointer();

    ui_manager->ApplyCommand(std::string("/run/initialize"));
    ui_manager->ApplyCommand(std::string("/run/printProgress 100"));
}

void kill_secondary_tracks(bool do_kill) {
    steppingAction->setKillSecondary(do_kill);
}

PYBIND11_MODULE(muon_slabs, m) {
    m.def("add", &add, "A function which adds two numbers");
    m.def("simulate_muon", &simulate_muon, "A function which simulates a muon through geant4 and returns the steps");
    m.def("initialize", &initialize, "Initialize geant4 stuff");
    m.def("collect", &collect, "Collect back the data");
    m.def("set_field_value", &set_field_value, "Set the magnetic field value");
    m.def("set_kill_momenta", &set_kill_momenta, "Set the kill momenta");
    m.def("kill_secondary_tracks", &kill_secondary_tracks, "Kill all tracks from resulting cascade");
}

// Compile the C++ code to a shared library
// c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` my_functions.cpp -o my_functions`python3-config --extension-suffix`

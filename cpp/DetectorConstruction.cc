#include "DetectorConstruction.hh"
#include "G4Material.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"
#include "G4Sphere.hh"
#include "G4UserLimits.hh"
#include "G4UniformMagField.hh"
#include "G4ThreeVector.hh"
#include "G4ThreeVector.hh"
#include "G4TransportationManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4NistManager.hh"
#include "G4PVPlacement.hh"
#include "G4Sphere.hh"
#include "G4SystemOfUnits.hh"
#include "G4ThreeVector.hh"
#include "G4UniformMagField.hh"
#include "G4UserLimits.hh"
#include "G4VPhysicalVolume.hh"
#include "G4VisAttributes.hh"
#include "G4FieldManager.hh"
#include "G4TransportationManager.hh"
#include "G4ChordFinder.hh"
#include "G4MagIntegratorStepper.hh"
#include "G4Mag_UsualEqRhs.hh"
#include "G4PropagatorInField.hh"
#include "G4ClassicalRK4.hh"


#include <iostream>

DetectorConstruction::DetectorConstruction()
: G4VUserDetectorConstruction()
{ }

DetectorConstruction::~DetectorConstruction()
{ }

G4VPhysicalVolume* DetectorConstruction::Construct()

{
    double limit_world_time_max_=5000*ns;
    double limit_world_energy_max_=100*eV;

    // Create a user limits object with a maximum step size of 1 mm
    G4double maxStep = 0.0001 * mm;
    G4UserLimits* userLimits =new G4UserLimits(
	        DBL_MAX, //max step length
            10*mm, //max track length
            limit_world_time_max_, //max track time
            limit_world_energy_max_);

    // Get NIST material manager
    G4NistManager* nist = G4NistManager::Instance();

    // Define the material
    G4Material* sphereMaterial = nist->FindOrBuildMaterial("G4_Fe");
    std::cout << "Srq: " << *sphereMaterial << std::endl;



    // Define the radius of the sphere
    G4double sphereRadius = 35.0 * m;

    // Define the world volume
    G4double worldSizeXY = 1.2 * sphereRadius * 2;
    G4double worldSizeZ  = 1.2 * sphereRadius * 2;
    G4Material* worldMaterial = nist->FindOrBuildMaterial("G4_AIR");

    // Create the world volume
    G4Box* solidWorld = new G4Box("WorldX", worldSizeXY / 2, worldSizeXY / 2, worldSizeZ / 2);
    G4LogicalVolume* logicWorld = new G4LogicalVolume(solidWorld, worldMaterial, "WorldY");
    logicWorld->SetUserLimits(userLimits);

    G4VPhysicalVolume* physWorld = new G4PVPlacement(0, G4ThreeVector(), logicWorld, "WorldZ", 0, false, 0, true);

    // Create the iron sphere
    G4Sphere* solidSphere = new G4Sphere("SphereX", 0, sphereRadius, 0, 360 * deg, 0, 180 * deg);
//    G4Box* solidSphere = new G4Box("WorldX", sphereRadius, sphereRadius, sphereRadius);

    G4LogicalVolume* logicSphere = new G4LogicalVolume(solidSphere, sphereMaterial, "SphereY");


    // Associate the user limits with a logical volume
    logicSphere->SetUserLimits(userLimits);


    new G4PVPlacement(0, G4ThreeVector(), logicSphere, "SphereZ", logicWorld, false, 0, true);

    // Define the uniform magnetic field
    G4ThreeVector fieldValue = G4ThreeVector(1*tesla, 0., 0.);
    magField = new G4UniformMagField(fieldValue);

    // Get the global field manager
    G4FieldManager* fieldManager = G4TransportationManager::GetTransportationManager()->GetFieldManager();

    // Set the magnetic field to the field manager
    fieldManager->SetDetectorField(magField);


    // Create the equation of motion and the stepper
    G4Mag_UsualEqRhs* equationOfMotion = new G4Mag_UsualEqRhs(magField);
    G4MagIntegratorStepper* stepper = new G4ClassicalRK4(equationOfMotion);

    // Create the chord finder
//    G4ChordFinder* chordFinder = new G4ChordFinder(magField);
//    fieldManager->SetChordFinder(chordFinder);
    fieldManager->CreateChordFinder(magField);

    logicWorld->SetFieldManager(fieldManager, true);



    // Return the physical world
    return physWorld;
}

void DetectorConstruction::setMagneticFieldValue(double strength, double theta, double phi) {
    G4ThreeVector fieldValue = G4ThreeVector(strength*tesla, theta, phi);

    magField->SetFieldValue(fieldValue);
}

#include "DetectorConstruction.hh"
#include "G4Material.hh"
#include "G4NistManager.hh"
#include "G4Box.hh"
#include "G4LogicalVolume.hh"
#include "G4PVPlacement.hh"
#include "G4SystemOfUnits.hh"

DetectorConstruction::DetectorConstruction()
: G4VUserDetectorConstruction()
{ }

DetectorConstruction::~DetectorConstruction()
{ }

G4VPhysicalVolume* DetectorConstruction::Construct()
{
    // Get NIST material manager
    G4NistManager* nist = G4NistManager::Instance();

    // Define the material
    G4Material* iron = nist->FindOrBuildMaterial("G4_Fe");

    // Define the size of the slab
    G4double slabSizeXY = 10.0*m;
    G4double slabThickness = 1.0*m;

    // Define the world volume
    G4double worldSizeXY = 1.2 * slabSizeXY;
    G4double worldSizeZ  = 1.2 * slabThickness;
    G4Material* worldMaterial = nist->FindOrBuildMaterial("G4_AIR");

    // Create the world volume
    G4Box* solidWorld = new G4Box("World", worldSizeXY/2, worldSizeXY/2, worldSizeZ/2);
    G4LogicalVolume* logicWorld = new G4LogicalVolume(solidWorld, worldMaterial, "World");
    G4VPhysicalVolume* physWorld = new G4PVPlacement(0, G4ThreeVector(), logicWorld, "World", 0, false, 0, true);

    // Create the iron slab
    G4Box* solidSlab = new G4Box("Slab", slabSizeXY/2, slabSizeXY/2, slabThickness/2);
    G4LogicalVolume* logicSlab = new G4LogicalVolume(solidSlab, iron, "Slab");
    new G4PVPlacement(0, G4ThreeVector(), logicSlab, "Slab", logicWorld, false, 0, true);

    // Return the physical world
    return physWorld;
}

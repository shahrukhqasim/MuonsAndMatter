#ifndef DetectorConstruction_h
#define DetectorConstruction_h 1

#include <G4UniformMagField.hh>
#include "G4VUserDetectorConstruction.hh"
#include "G4VPhysicalVolume.hh"

class DetectorConstruction : public G4VUserDetectorConstruction
{
public:
    DetectorConstruction();
    virtual ~DetectorConstruction();

    virtual G4VPhysicalVolume* Construct();
    void setMagneticFieldValue(double strength, double theta, double phi);
private:
    G4UniformMagField* magField;
};

#endif

#ifndef DetectorConstruction_h
#define DetectorConstruction_h 1

#include <G4UniformMagField.hh>
#include "G4VUserDetectorConstruction.hh"
#include "G4VPhysicalVolume.hh"
#include "json/json.h"

class DetectorConstruction : public G4VUserDetectorConstruction
{
public:
    DetectorConstruction();
    virtual ~DetectorConstruction();

    virtual G4VPhysicalVolume* Construct();
    virtual void setMagneticFieldValue(double strength, double theta, double phi);
protected:
    G4UniformMagField* magField;

};

#endif

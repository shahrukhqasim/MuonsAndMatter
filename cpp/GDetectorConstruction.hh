//
// Created by Shah Rukh Qasim on 10.07.2024.
//

#ifndef MY_PROJECT_GDETECTORCONSTRUCTION_HH
#define MY_PROJECT_GDETECTORCONSTRUCTION_HH

//#include <asdl.h>
#include "DetectorConstruction.hh"
#include "json/json.h"
#include "SlimFilmSensitiveDetector.hh"
#include "unordered_set"

class GDetectorConstruction : public DetectorConstruction {
public:
    virtual G4VPhysicalVolume *Construct();
    SlimFilmSensitiveDetector* slimFilmSensitiveDetector;
public:
    GDetectorConstruction(Json::Value detector_data);
protected:
    Json::Value detectorData;
    Json::Value fairShipData;
public:
    void setFairShipData(const Json::Value &fairShipData);

    void ConstructSDandField() override;

protected:
    double detectorWeightTotal;
    G4LogicalVolume* sensitiveLogical;
    std::unordered_set<std::string> toSkip;
public:
    double getDetectorWeight() override;
    void setMagneticFieldValue(double strength, double theta, double phi) override;

    G4LogicalVolume * buildFromFairShip();
    G4LogicalVolume * processNode(const Json::Value &node, const std::string &name, int level,
                                 G4LogicalVolume *logicalVol);
    G4LogicalVolume *handleBBox(const Json::Value &node, const std::string &name, G4LogicalVolume *logicalParent);
    G4LogicalVolume *handleArb8(const Json::Value &node, const std::string &name, G4LogicalVolume *logicalParent);
    G4LogicalVolume *handleTube(const Json::Value &node, const std::string &name, G4LogicalVolume *logicalParent);

};


#endif //MY_PROJECT_GDETECTORCONSTRUCTION_HH

//
// Created by Shah Rukh Qasim on 10.07.2024.
//

#ifndef MY_PROJECT_GDETECTORCONSTRUCTION_HH
#define MY_PROJECT_GDETECTORCONSTRUCTION_HH

#include "DetectorConstruction.hh"
#include "json/json.h"

class GDetectorConstruction : public DetectorConstruction {
public:
    virtual G4VPhysicalVolume *Construct();
public:
    GDetectorConstruction(std::string detector_data);
protected:
    Json::Value detectorData;
public:
    void setMagneticFieldValue(double strength, double theta, double phi) override;

};


#endif //MY_PROJECT_GDETECTORCONSTRUCTION_HH

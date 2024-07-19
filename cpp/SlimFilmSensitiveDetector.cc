//
// Created by Shah Rukh Qasim on 17.07.2024.
//

#include "SlimFilmSensitiveDetector.hh"

SlimFilmSensitiveDetector::SlimFilmSensitiveDetector(const G4String &name) : G4VSensitiveDetector(name) {

}

SlimFilmSensitiveDetector::~SlimFilmSensitiveDetector() {}

void SlimFilmSensitiveDetector::Initialize(G4HCofThisEvent *hce) {

}

G4bool SlimFilmSensitiveDetector::ProcessHits(G4Step *aStep, G4TouchableHistory *ROhist) {
    std::cout<<"Check... "<<aStep->GetTotalEnergyDeposit()<<std::endl;
}

void SlimFilmSensitiveDetector::EndOfEvent(G4HCofThisEvent *hce) {

}
#include "CustomSteppingAction.hh"
#include "G4Step.hh"
#include "G4Track.hh"
#include "G4EventManager.hh"
#include "G4Event.hh"
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"
#include "G4RunManager.hh"
#include "G4ios.hh"
#include "G4FieldManager.hh"
#include "G4TransportationManager.hh"
#include "G4ChordFinder.hh"
#include "G4MagIntegratorStepper.hh"
#include "G4Mag_UsualEqRhs.hh"
#include "G4PropagatorInField.hh"
#include "G4ClassicalRK4.hh"


#include <iostream>

CustomSteppingAction::CustomSteppingAction()
    : G4UserSteppingAction(), eventManager(G4EventManager::GetEventManager())
{
    primaryTrackId=1; // Assume its one; might need to be changed if more than one primary particles are introduced
}

CustomSteppingAction::~CustomSteppingAction()
{}

void CustomSteppingAction::UserSteppingAction(const G4Step* step)
{

//    std::cout<<"Hello from the CustomSteppingAction::UserSteppingAction!\n";
    // Get the track
    G4Track* track = step->GetTrack();

    // Get the volume of the current step
    G4VPhysicalVolume* volume = step->GetPreStepPoint()->GetTouchableHandle()->GetVolume();

    // Get the kinetic energy of the particle
    G4double kineticEnergy = step->GetPreStepPoint()->GetKineticEnergy();

    // Get the energy deposited in this step
    G4double edep = step->GetTotalEnergyDeposit();

    // Get the position of the step
    G4ThreeVector pos = step->GetPostStepPoint()->GetPosition();

//    // Print step information for debug
//    G4cout << "Track ID: " << track->GetTrackID()
//           << " Volume: " << volume->GetName()
//           << " Kinetic Energy: " << G4BestUnit(kineticEnergy, "Energy")
//           << " Energy Deposit: " << G4BestUnit(edep, "Energy")
//           << " Position: " << G4BestUnit(pos, "Length")
//           << G4endl;

    // Example of custom logic: stop the track if it deposits energy above a threshold
//    if (edep > 1.0*MeV)
//    {
//        track->SetTrackStatus(fStopAndKill);
//    }
    num_steps += 1;

    G4StepPoint* preStepPoint = step->GetPreStepPoint();
    G4ThreeVector positiont = preStepPoint->GetPosition();
    G4double position[4];  // [Bx, By, Bz, Ex, Ey, Ez]
    position[0] = positiont[0];
    position[1] = positiont[1];
    position[2] = positiont[2];


    // Get the global field manager
    G4FieldManager* fieldManager = G4TransportationManager::GetTransportationManager()->GetFieldManager();

    // Define a vector to hold the field value
    G4ThreeVector fieldValue;


//    // Check if the field manager and its field are valid
//    if (fieldManager && fieldManager->GetDetectorField())
//    {
//        // Get the field value at the current position
//        fieldManager->GetDetectorField()->GetFieldValue(position, &fieldValue[0]);
//
//        // Print the magnetic field strength
//        G4cout << "Magnetic field at step: "
//               << fieldValue / tesla << " Tesla" << G4endl;
//    }
//    else {
//        G4cout << "No magnetic field found in the stepping action.\n";
//    }

    G4ThreeVector momentum = track->GetMomentum();

//    std::cout<<track->GetPDGID()

//     G4cout << "Step length: " << step->GetStepLength() / mm << " mm" << G4endl;

    if (momentum.mag() / GeV > 40) {
        G4cout << "(" << momentum.x() / GeV << " GeV/c, "
               << momentum.y() / GeV << " GeV/c, "
               << momentum.z() / GeV << " GeV/c) and track id "
               << track->GetTrackID() << " and step size "
               << step->GetStepLength() / mm << " mm"
               << G4endl;
    }

    if (track->GetTrackID() == primaryTrackId) {
        G4ThreeVector position2 = track->GetPosition();

        // Fill the vectors with current step data
        px.push_back(momentum.x());
        py.push_back(momentum.y());
        pz.push_back(momentum.z());

        x.push_back(position2.x());
        y.push_back(position2.y());
        z.push_back(position2.z());

        stepLength.push_back(step->GetStepLength());
        chargeDeposit.push_back(step->GetTotalEnergyDeposit());
    }



    // Get the G4ParticleDefinition from the G4Track
    const G4ParticleDefinition* particleDef = track->GetDefinition();

    // Retrieve the PDG ID
    G4int pdgID = particleDef->GetPDGEncoding();

    // Now you can use pdgID as needed
//    std::cout << "XX: " << pdgID << " ";

//   std::cout<<track->GetKineticEnergy()/GeV<<std::endl;
}


void CustomSteppingAction::clean() {
    px.clear();
    py.clear();
    pz.clear();
    x.clear();
    y.clear();
    z.clear();
    stepLength.clear();
    chargeDeposit.clear();
    std::cout<<"Cleaning!"<<std::endl;
}
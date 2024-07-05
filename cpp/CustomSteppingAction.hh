#ifndef CUSTOMSTEPPINGACTION_HH
#define CUSTOMSTEPPINGACTION_HH

#include "G4UserSteppingAction.hh"
#include "globals.hh"

class G4Step;
class G4EventManager;
class G4Event;

class CustomSteppingAction : public G4UserSteppingAction
{
public:
    CustomSteppingAction();
    virtual ~CustomSteppingAction();

    virtual void UserSteppingAction(const G4Step* step);
    void clean();

private:
    G4EventManager* eventManager;
    G4Event* event;


public:
    // Add any necessary members here
    std::vector<double> px;
    std::vector<double> py;
    std::vector<double> pz;

    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;

    std::vector<double> stepLength;
    std::vector<double> chargeDeposit;

    int primaryTrackId;

public:
    int num_steps;
};

#endif

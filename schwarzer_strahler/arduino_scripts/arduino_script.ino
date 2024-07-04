#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

/*
  You can use any switch you just have to connect them right with the red Pitaya
  STEP_DONE gives a signal to the Red pitaya that he can now measure values
  DO_STEP to check if a step should be done
  ENDSWITCH_END, ENDSWITCH_START are just to check if it got to any of the buttons
  in the monochromator
  INIT to Initialise the position -> motor moves to start
*/
#define STEP_DONE       7
#define DO_STEP         9
#define ENDSWITCH_START 10
#define ENDSWITCH_END   11
#define INIT            12

// used so that the motor is only doing one step
bool can_do_step = true;
bool finished = false;

// Initialising the motor
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_StepperMotor *_Motor = AFMS.getStepper(200 ,2);

// gets executet only ones on startup
void setup() {

  // Serial port einrchten
  Serial.begin(9600);
  AFMS.begin();

  // Initialises the Pins 
  pinMode(INIT, INPUT);
  pinMode(ENDSWITCH_START, INPUT);
  pinMode(ENDSWITCH_END, INPUT);
  pinMode(DO_STEP, INPUT);

  // Output Pins
  pinMode(STEP_DONE, OUTPUT);

  _Motor->setSpeed(30);
}

void loop() {
  // reads from red pitaya if it should make a step
  int do_step_val = digitalRead(DO_STEP);

  // only runs if the motor should get to startung position 
  if (finished) { // stop running }
  else if (digitalRead(INIT) == HIGH) {
    digitalWrite(STEP_DONE, LOW);
    if (digitalRead(ENDSWITCH_START) != HIGH) {
      _Motor->onestep(BACKWARD, DOUBLE);
    }
    else {
      digitalWrite(STEP_DONE, HIGH);
      _Motor->release();
    }
  }
  else if (do_step_val == HIGH && can_do_step) {
    digitalWrite(STEP_DONE, LOW);
    if (digitalRead(ENDSWITCH_END) != HIGH) {
      _Motor->onestep(FORWARD, DOUBLE);
    }
    else {
      finished = true;
    }
    digitalWrite(STEP_DONE, HIGH);
    can_do_step = false;
  }
  else if (do_step_val == LOW) {
    can_do_step = true;
  }
}

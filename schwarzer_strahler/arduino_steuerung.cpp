#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

#define INIT            12
#define ENDSWITCH_START 10
#define ENDSWITCH_END   11
#define DO_STEP         9
#define STEP_DONE       8

bool can_do_step = true;

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_StepperMotor *_Motor = AFMS.getStepper(200 ,2); // 200 Steps pro umdrehung in port 2

/*
* Bei BACKWARD bewegt sich der Motor zum Start Switch
* Bei FORWARD dem End Switch
*/

void setup() {
  // Serial port einrchten
  Serial.begin(9600);
  AFMS.begin();

  // Input Pins
  pinMode(INIT, INPUT);
  pinMode(ENDSWITCH_START, INPUT);
  pinMode(ENDSWITCH_END, INPUT);
  pinMode(DO_STEP, INPUT);

  // Output Pins
  pinMode(STEP_DONE, OUTPUT);

  _Motor->setSpeed(30);
}

void loop() {
  int do_step_val = digitalRead(DO_STEP);

  if (digitalRead(INIT) == HIGH) {
    digitalWrite(STEP_DONE, LOW);
    if (digitalRead(ENDSWITCH_START) != HIGH) {
      _Motor->onestep(BACKWARD, DOUBLE);
    }
    else {
      Serial.print("Initialiserung Fertig\n");
      digitalWrite(STEP_DONE, HIGH);
      _Motor->release();
    }
  }
  else if (do_step_val == HIGH && can_do_step) {
    digitalWrite(STEP_DONE, LOW);
    if (digitalRead(ENDSWITCH_END) != HIGH) {
      _Motor->onestep(FORWARD, DOUBLE);
    }
    digitalWrite(STEP_DONE, HIGH);
    can_do_step = false;
  }
  else if (do_step_val == LOW) {
    can_do_step = true;
  }
}

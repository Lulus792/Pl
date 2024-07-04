#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"


// Definition of the used Pins on the Arduino
#define ENDSWITCH_START 10
#define ENDSWITCH_END   11

// only used to stop the motor once its went to start and end switch
int state = 0;

// Initialising the Motor
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_StepperMotor *_Motor = AFMS.getStepper(200 ,2);

// standard Arduino function only executed once
void setup() {

  // Serial port einrchten
  Serial.begin(9600);
  AFMS.begin();

  // Initialising the used Pins 
  pinMode(ENDSWITCH_START, INPUT);
  pinMode(ENDSWITCH_END, INPUT);

  // setting Motor speed
  // doesn't run smoothly on higher speed
  _Motor->setSpeed(30);
}

// runs as long as the arduino gets power
void loop() {

  /*
    Moves to the start switch, and checks if they are on (1) or off (0)
    If they are pressed they are on which means it is going to read HIGH
    then it moves forward to the other switch and ones it reaches it it
    is going to stop moving, cause we now know that the switches work. The
    release is neccesarry cause we allocated memmory at the beginning line 14
  */
  if (digitalRead(ENDSWITCH_START) != HIGH && state == 0) {
    _Motor->onestep(BACKWARD, DOUBLE);
  }
  else if (digitalRead(ENDSWITCH_END) != HIGH && state == 1) {
    _Motor.onestep(FORWARD, DOUBLE);
  }
  else {
    if (digitalRead(ENDSWITCH_START) == HIGH) {
      state = 1;
    }
    else if (digitalRead(ENDSWITCH_END) == HIGH) {
      state == 2;
    }
    else if (state == 2) {
      _Motor->release();
    }
    else { // do nothing }
  }
  
}

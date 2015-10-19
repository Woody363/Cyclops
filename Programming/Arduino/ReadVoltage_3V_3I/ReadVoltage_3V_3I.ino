/*
  Analog input, analog output, serial output

 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.

 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground

 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin0 = A0;  // Analog input pin that the potentiometer is attached to
const int analogInPin1 = A1;  // Analog input pin that the potentiometer is attached to
const int analogInPin2 = A2;  // Analog input pin that the potentiometer is attached to
const int analogInPin3 = A3;  // Analog input pin that the potentiometer is attached to
const int analogInPin4 = A4;  // Analog input pin that the potentiometer is attached to
const int analogInPin5 = A5;  // Analog input pin that the potentiometer is attached to

const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot

float voltage1 = 0;
float voltage2 = 0;
float voltage3 = 0;

float current1 = 0;
float current2 = 0;
float current3 = 0;

float power1 = 0;
float power2 = 0;
float power3 = 0;

int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(115200);
}

void loop() {
  // read the analog in value:
  voltage1 = analogRead(analogInPin0);
  voltage2 = analogRead(analogInPin2);
  voltage3 = analogRead(analogInPin4);

  current1 = analogRead(analogInPin1);
  current2 = analogRead(analogInPin3);
  current3 = analogRead(analogInPin5); 
        
  // map it to the range of the analog out:
  //outputValue = map(sensorValue, 0, 1023, 0, 285);
  voltage1 = ((voltage1 * 5.0)*57.0) / 1023.0; //calculates voltage which comes through a potential divider.
  voltage2 = ((voltage2 * 5.0)*57.0) / 1023.0;
  voltage3 = ((voltage3 * 5.0)*57.0) / 1023.0;

  current1 = ((((current1 * 5000.0)) / 1023.0)-600.0)/(60.0/1000.0); //calculates current from hall sensors
  current2 = ((((current2 * 5000.0)) / 1023.0)-600.0)/(60.0/1000.0);
  current3 = ((((current3 * 5000.0)) / 1023.0)-600.0)/(60.0/1000.0);

  power1 = (voltage1)*(current1/1000);
  power2 = (voltage2)*(current2/1000);
  power3 = (voltage3)*(current3/1000);

  
  // print the results to the serial monitor:
//  Serial.print("Voltage 1 = ");
//  Serial.println(voltage1);
//  Serial.print("Current 1 = ");
//  Serial.println(current1); 
//  Serial.print("Voltage 2 = ");
//  Serial.println(voltage2);
//  Serial.print("Current 2 = ");
//  Serial.println(current2);
  Serial.print("Power 2 = ");
  Serial.println(power2);
//  Serial.print("Voltage 3 = ");
//  Serial.println(voltage3);
//  Serial.print("Current 3 = ");
//  Serial.println(current3);


  

//  Serial.print("aAAV");
//  Serial.print(outputValue);
//  Serial.println("0000-----");
  

  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(1000);
}

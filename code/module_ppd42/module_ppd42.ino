/*
  JST Pin 1 (Black Wire)  => Arduino GND
  JST Pin 3 (Red wire)    => Arduino 5VDC
  JST Pin 4 (Yellow wire) => Arduino Digital Pin
*/
#include <movingAvg.h>
movingAvg avg(10);

int pin = 28; // B12 for BluePill

unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 60000;
unsigned long lowpulseoccupancy = 0;
float ratio = 0;
float concentration = 0;

#include <Wire_slave.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, 1);
  
  Serial.begin(9600);
  pinMode(pin, INPUT);
  starttime = millis();
  avg.begin();
  Wire.begin(8);
  Wire.onRequest(requestEvent);

  digitalWrite(LED_BUILTIN, 0);
  delay(200);
  digitalWrite(LED_BUILTIN, 1);
  delay(200);
  digitalWrite(LED_BUILTIN, 0);
  delay(200);
  digitalWrite(LED_BUILTIN, 1);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()
void requestEvent()
{
  Wire.write("hello ");
  digitalWrite(LED_BUILTIN, 0);
  delay(100);
  digitalWrite(LED_BUILTIN, 1);
}

void loop() {
  duration = pulseIn(pin, LOW);
  lowpulseoccupancy = lowpulseoccupancy + duration;

  if ((millis() - starttime) > sampletime_ms)
  {
    ratio = lowpulseoccupancy / (sampletime_ms * 10.0); // Integer percentage 0=>100
    concentration = 1.1 * pow(ratio, 3) - 3.8 * pow(ratio, 2) + 520 * ratio + 0.62; // using spec sheet curve
    //    Serial.print(lowpulseoccupancy);
    //    Serial.print(",");
    //    Serial.print(ratio);
    //    Serial.print(",");
    int average = avg.reading(concentration);
    Serial.print(concentration);
    Serial.print(",");
    Serial.print(average);
    Serial.println("");
    lowpulseoccupancy = 0;
    starttime = millis();
  }
}

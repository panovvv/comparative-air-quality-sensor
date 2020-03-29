#include <Wire_slave.h>

// **********    User defined variables    **********

// Pick a unique address for this sensor on I2C network.
// Addresses 0 to 7 and 120 to 127 are reserved.
#define I2C_ADDRESS 8

// Generate a unique identifier for the sensor:
// https://en.wikipedia.org/wiki/Universally_unique_identifier
// E.g. here https://www.uuidgenerator.net/
#define MY_UUID "c2a74b6a-7698-4526-942b-781ab957c2c4"

// ********** End of user defined variables **********


/*  Shinyei PPD42 pinout:
    JST Pin 1 => GND
    JST Pin 2 => P2 (PM2.5)
    JST Pin 3 => 5VDC
    JST Pin 4 => P1 (PM1)
    JST Pin 5 => threshold for P2 (not used)
*/
int pm25Pin = 28;     // B12 on BluePill
int pm1Pin =  29;     // B13 on BluePill

#define SENSOR_MODEL "Shinyei PPD42"

// Calculate dust concentration every 60 sec.
#define SAMPLE_PERIOD_MS 60000

// Send negative values until the measurements are ready.
double concentration25 = -1;
double concentration1 = -1;

// String buffers for data received/sent over I2C
char input_buffer[32];
char output_buffer[32];

enum data_types {
  UUID,
  MODEL,
  POLLUTANTS,
  SAMPLE_PERIOD,
  PM1,
  PM25,
  NA
} current_data_type;

/* Master writes a string to a slave to let it know what kind of
   data it wants to receive on subsequent read. */
void requestEvent() {
  switch (current_data_type)
  {
    case UUID:
      Wire.write(MY_UUID);
      break;
    case MODEL:
      Wire.write(SENSOR_MODEL);
      break;
    case POLLUTANTS:
      Wire.write("PM1,PM2.5");
      break;
    case SAMPLE_PERIOD:
      sprintf(output_buffer, "%d", SAMPLE_PERIOD_MS / 1000);
      Wire.write(output_buffer);
      break;
    case PM1:
      sprintf(output_buffer, "%.3lf", concentration1);
      Wire.write(output_buffer);
      break;
    case PM25:
      sprintf(output_buffer, "%.3lf", concentration25);
      Wire.write(output_buffer);
      break;
    default:
      Wire.write("n/a");
      break;
  }
}

// function that executes whenever data is received over I2C
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  memset(input_buffer, 0, sizeof input_buffer);
  uint8_t input_chars = 0;
  while (Wire.available()) {
    input_buffer[input_chars] = Wire.read();
    input_chars++;
  }
  input_buffer[input_chars] = '\0';

  if (strstr(input_buffer, "get_uuid")) {
    current_data_type = UUID;
  } else if (strstr(input_buffer, "get_model"))  {
    current_data_type = MODEL;
  } else if (strstr(input_buffer, "get_pollutants"))  {
    current_data_type = POLLUTANTS;
  } else if (strstr(input_buffer, "get_sample_period_seconds"))  {
    current_data_type = SAMPLE_PERIOD;
  } else if (strstr(input_buffer, "get_PM1"))  {
    current_data_type = PM1;
  } else if (strstr(input_buffer, "get_PM2.5"))  {
    current_data_type = PM25;
  } else {
    current_data_type = NA;
  }
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, 1);

  pinMode(pm1Pin, INPUT);
  pinMode(pm25Pin, INPUT);
  Wire.begin(I2C_ADDRESS);
  Wire.onRequest(requestEvent);
  Wire.onReceive(receiveEvent);

  digitalWrite(LED_BUILTIN, 0);
  delay(200);
  digitalWrite(LED_BUILTIN, 1);
  delay(200);
  digitalWrite(LED_BUILTIN, 0);
  delay(200);
  digitalWrite(LED_BUILTIN, 1);
}

void loop() {
  // 3 minutes to heat up
  for (int i = 0; i < 900; i++) {
    digitalWrite(LED_BUILTIN, 1);
    delay(1000);
    digitalWrite(LED_BUILTIN, 0);
    delay(1000);
  }
  concentration25 = conversion25(getConcentration(pm25Pin));
  concentration1 = conversion1(getConcentration(pm1Pin));
}

const double pi = 3.14159;
// Convert pcs/0.01cf to ug/m3 for PM2.5
double conversion25(double concentration_pcs) {
  double density = 1.65 * pow (10, 12);
  double r25 = 0.44 * pow (10, -6);
  double vol25 = (4 / 3) * pi * pow (r25, 3);
  double mass25 = density * vol25;
  double K = 3531.5;
  return concentration_pcs * K * mass25;
}

// Convert pcs/0.01cf to ug/m3 for PM1
float conversion1(double concentration_pcs) {
  double density = 1.65 * pow (10, 12);
  double r10 = 0.44 * pow (10, -6);
  double vol10 = (4 / 3) * pi * pow (r10, 3);
  double mass10 = density * vol10;
  double K = 3531.5;
  return concentration_pcs * K * mass10;
}

// Returns particle concentration, pcs/0.01cf (particles per 1/100 of a cubic foot)
// This function is blocking, returns after SAMPLE_PERIOD_MS milliseconds.
double getConcentration(uint8_t pin) {
  uint32_t startTime = millis();
  uint32_t lowPulseOccupancy = 0;
  while (1) {
    uint32_t duration = pulseIn(pin, LOW);
    lowPulseOccupancy += duration;
    if ((millis() - startTime) > SAMPLE_PERIOD_MS) {
      double ratio = lowPulseOccupancy / (SAMPLE_PERIOD_MS * 10.0);
      double concentration_pcs = 1.1 * pow(ratio, 3) - 3.8 * pow(ratio, 2) + 520 * ratio + 0.62;
      lowPulseOccupancy = 0;
      return concentration_pcs;
    }
  }
}

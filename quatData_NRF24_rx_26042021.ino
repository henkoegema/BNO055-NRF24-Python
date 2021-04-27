/* NANO RX  */
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
RF24 radio(9, 10); // CE, CSN
const byte address[6] = "00001";

float imu[10];

void setup() {
  Serial.begin(2000000);
  radio.begin();
  radio.openReadingPipe(0, address);
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}
void loop() {
  if (radio.available()) {
    radio.read(imu, sizeof(imu));

    //Send following data to Python script
    Serial.print(imu[0]);
    Serial.print(",");
    Serial.print(imu[1]);
    Serial.print(",");
    Serial.print(imu[2]);
    Serial.print(",");
    Serial.println(imu[3]);
    
  }
}

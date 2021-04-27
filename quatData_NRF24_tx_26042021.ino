/* NANO TX */
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>

#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055();

RF24 radio(9,10); // CE, CSN
const byte address[6] = "00001";
float quatData[10];

void setup(){
  Serial.begin(2000000);
  radio.begin();
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.setAutoAck(1);
  radio.enableAckPayload();
  radio.stopListening();

  myIMU.begin();
  delay(1000);
  int8_t temp=myIMU.getTemp();
  myIMU.setExtCrystalUse(true);
}

void loop(){

  uint8_t system, gyro, accel, mg = 0;
  myIMU.getCalibration(&system, &gyro, &accel, &mg);

  imu::Quaternion quat=myIMU.getQuat();

  quatData[0] = quat.w();
  quatData[1] = quat.x();
  quatData[2] = quat.y();
  quatData[3] = quat.z();
 
  radio.write(quatData,sizeof(quatData));

  /* Serial.print(quatData[0]);
  Serial.print(",");
  Serial.print(quatData[1]);
  Serial.print(",");
  Serial.print(quatData[2]);
  Serial.print(",");
  Serial.println(quatData[3]); */
   
  delay(100);
}

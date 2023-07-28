//htu21d-m module: https://www.hestore.hu/prod_getfile.php?id=8627
//https://roboticsbackend.com/wiringpi-i2c-tutorial-rasperry-pi-adxl345/

#include <iostream>
#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>

#include "wiringPi.h"
#include "wiringPiI2C.h"


#define   HTU21D_I2C_ADDR 0x40

#define   HTU21D_TEMP     0xF3
#define   HTU21D_HUMID    0xF5

#define DEVICE_ID 0x40
#define READ_ACCESS 0x81

#define REG_TEMP 0xE3
#define REG_HUM 0xE5
#define WRITE_USER_REG 0xE6
#define READ_USER_REG 0xE7
#define SOFT_RESET 0xFE

// Get temperature
double getTemperature(int fd)
{
	unsigned char buf [4];
	wiringPiI2CWrite(fd, REG_TEMP);
	delay(100);
	read(fd, buf, 3);
	unsigned int temp = (buf [0] << 8 | buf [1]) & 0xFFFC;
	// Convert sensor reading into temperature.
	// See page 14 of the datasheet
	double tSensorTemp = temp / 65536.0;
	return -46.85 + (175.72 * tSensorTemp);
}

// Get humidity
double getHumidity(int fd)
{
	unsigned char buf [4];
	wiringPiI2CWrite(fd, REG_HUM);
	delay(100);
	read(fd, buf, 3);
  	unsigned int humid = (buf [0] << 8 | buf [1]) & 0xFFFC;
	// Convert sensor reading into humidity.
	// See page 15 of the datasheet
	double tSensorHumid = humid / 65536.0;
	return -6.0 + (125.0 * tSensorHumid);
}

int main (void)
{
    // Setup I2C communication
    int fd = wiringPiI2CSetup(DEVICE_ID);
    if (fd == -1) {
        std::cout << "Failed to init I2C communication.\n";
        return -1;
    }
    std::cout << "I2C communication successfully setup.\n";

    while(1){
    printf("%5.2fC\n", getTemperature(fd));
	printf("%5.2f%%rh\n", getHumidity(fd));
    delay(5000);
    }
    
    return 0;
}

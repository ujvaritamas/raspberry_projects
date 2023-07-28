#include <iostream>
#include "wiringPi.h"

using namespace std;

#define RED_LED_PIN 29

void setup(){

	pinMode(RED_LED_PIN, OUTPUT);
	cout<<"Ledpin setupt finished" << endl;
}

int main(void){

    if(wiringPiSetup()<0){
		cout<<"setup wiring pi failed"<<endl;
		return 1;
	}

    setup();
    // Main program loop
    while(1)
    {
        // Toggle the LED
        digitalWrite(0, HIGH);
        cout << "write to high"<<endl;
        delay(500); 	// Delay 500ms
        digitalWrite(0, LOW);
        cout << "write to low"<<endl;
        delay(500); 	// Delay 500ms
    }


    return 0;
}
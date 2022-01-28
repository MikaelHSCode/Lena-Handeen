String serData;

#include <Servo.h>

Servo servo_left_orange; // This servo controls pinky and ring finger 
Servo servo_right_blue; // This servo controls the middle and index finger

int pos; //the servos current position
int default_pos; //which default value the servo has
int step_value;  // 1 or -1 

void setup() {
  Serial.begin(9600); // starts serial communication, send out commands through the USB connection
  Serial.println("Arduino is ready!");
  servo_left_orange.attach(9); // using pin 9 for orange cable
  servo_right_blue.attach(7); // using pin 7 for blue cable
  
  Rock_servo();
}

void loop() {
  while (Serial.available()> 0){ // something has been sent serially
    char rec = Serial.read();   // Our arduino reads one serial character at a time
        serData += rec;         //Building the string

    if(rec == '\n'){          // If recieved char is a new line
      if(serData == "R\n"){
        Serial.print("Message recieved: R ");
        Serial.print(serData);  
        serData = "";
        
        Rock_servo();
        delay(1000);
      }
      else if(serData == "S\n"){
        Serial.print("Message recieved: S ");
        Serial.print(serData);  
        serData = "";
        
        Scissors_servo();
        delay(1000);
        Rock_servo();
        delay(1000);
        
      }
      else if(serData == "P\n"){
        Serial.print("Message recieved: P");
        Serial.print(serData);  
        serData = "";

        Paper_servo();
        delay(1000);
        Rock_servo();
        delay(1000);
      }
      else {
        Serial.print("Unknown Symb");
        Serial.print(serData); 
      }
    }
  }

}

void Rock_servo(){
  servo_right_blue.write(170); //closed
  servo_left_orange.write(10); //closed
}

void Paper_servo(){
  servo_right_blue.write(10); //open
  servo_left_orange.write(170); //open
}

void Scissors_servo(){
 servo_right_blue.write(10);  //open
 servo_left_orange.write(10); //closed
}

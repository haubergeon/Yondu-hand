#include <Servo.h>
Servo finger1;
Servo finger2;
Servo finger3;
Servo finger4;
double angle;
String str;
void setup() {
 finger1.attach(9);
 finger2.attach(10);
 finger3.attach(11);
 finger4.attach(5);
 Serial.begin(9600);


 finger1.write(0.00);
 finger2.write(0.00); 
 finger3.write(0.00);  
 finger4.write(0.00);
 
}

void loop() {

  if (Serial.available() > 0){
    finger1.write(0.00);
    finger2.write(0.00); 
    finger3.write(0.00);  
    finger4.write(0.00);
    
    str = Serial.readString();
    Serial.println(str);
    fold(str);
  }   
}

void fold(String str){
  
  if(str.charAt(0)== '1'){finger1.write(180.00);}
  if(str.charAt(1)== '1'){finger2.write(180.00);}
  if(str.charAt(2)== '1'){finger3.write(180.00);}
  if(str.charAt(3)== '1'){finger4.write(180.00);}
  
}

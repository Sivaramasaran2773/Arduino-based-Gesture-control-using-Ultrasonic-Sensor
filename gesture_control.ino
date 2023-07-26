                          ////// Arduino code for gesture control using ULTRASONIC sensor////

// setting trig and echo pins
const int trigPin = 9;
const int echoPin = 10;
// declaring variables
double duration;
double distance;
// Setting of trigpin as output and echopin as input
void setup() {
pinMode(trigPin, OUTPUT); 
pinMode(echoPin, INPUT); 
Serial.begin(9600); // Starts the serial communication
}

void loop() {
// Clearing the tring pin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// For 10 microseconds,setting the trigpin as high
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Distance caluculation
distance= duration*0.034/2;// in cm
// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
delayMicroseconds(60);//recommended to send trigger signal after 60us
 
}

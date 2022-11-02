int sensor = 2;
int led = 13;
int sensor_value = 0;
bool active = false;

void setup() {
  pinMode(sensor, INPUT); 
  pinMode(led, OUTPUT); 
  Serial.begin(9600); // open the serial port at 9600 bps:
}

void loop() {
  sensor_value = digitalRead(sensor);

  if (sensor_value == HIGH && !active)
  {
    Serial.println("1");
    active = true;
    digitalWrite(led, HIGH);
  }
  else if (sensor_value == LOW && active)
  {
    Serial.println("0");
    active = false;
    digitalWrite(led, LOW);
  }
}

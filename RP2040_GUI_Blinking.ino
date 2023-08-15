String command;

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.readString();
    
    if (command == "turn on") {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    
    if (command == "turn off") {
      digitalWrite(LED_BUILTIN, LOW);
    }
    
    if (command == "blink") {
      for (int i = 0; i < 60; i++) {
        delay(150);
        digitalWrite(LED_BUILTIN, HIGH);
        delay(150);
        digitalWrite(LED_BUILTIN, LOW);
      } // Blink for loop
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
}

int i = 0;
void loop() {
  // put your main code here, to run repeatedly:
  i = i + 1;
  Serial.print("msg ");Serial.println(i);
  delay(10);
}

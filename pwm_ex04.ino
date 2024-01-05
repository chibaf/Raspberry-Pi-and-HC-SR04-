// example 04 fade in and fade out of LED

const int LED=9;
int i=0;

void setup() {
  pinMode(LED,OUTPUT);
}

void loop() {
  for (i=0;i<255;i++){
    analogWrite(LED,i);
    delay(10);
  }
  delay(500);
  for (i=255;i>0;i--){
    analogWrite(LED,i);
    delay(10);
  }
}

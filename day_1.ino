int state = 0;
int i = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(D1,OUTPUT);
  pinMode(D0,INPUT);
}
void loop() {
 state = digitalRead(D0);
 Serial.println(state);
 if (state == HIGH && i==255){
  for (i = 255;i>1;i--){
    if (i==1){
      break;
    }
    analogWrite(D1,i);
    delay(10);
  }
  i = 0;
 }
 else if(state == LOW){
  i = 255;
  analogWrite(D1,i);  
 }
}

int pins[] = {7,5,8,6,4,2,9,3};
int counter = 215;
byte inByte = 00000000;
char myChar[] = "Hello World!";

void setup() {
  // put your setup code here, to run once:
  for (int i = 0; i < 8; i++) {
    pinMode(pins[i], OUTPUT);
  }



}

void loop() {
    inByte = byte('o');
    for(int i=0; i < 8; i+=0) {
      for(int mask = 00000001; mask > 0; mask <<= 1) {
        if (inByte & mask) {
          digitalWrite(pins[i], 1);
        }
  
        else {
          digitalWrite(pins[i], 0);
              
        }
        i++;
      }
    }
  }

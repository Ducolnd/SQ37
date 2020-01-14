//The 8 LEDs

#define LED1 7
#define LED2 5
#define LED3 8
#define LED4 6
#define LED5 4
#define LED6 2
#define LED7 9
#define LED8 3

int pins[] = {7,5,8,6,4,2,9,3};

//The 1/1 buttons

#define PushBTN1 10
#define PushBTN2 11

//Submit button

#define PushBTN3 12

int howFar = 1;
int counter = 0;
byte inByte = 00000000;


void setup() {
  // The 8 LEDs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  pinMode(LED6, OUTPUT);
  pinMode(LED7, OUTPUT);
  pinMode(LED8, OUTPUT);

  //The 1/2 buttons
  pinMode(PushBTN1, INPUT);
  pinMode(PushBTN2, INPUT);

  //Submit button
  pinMode(PushBTN3, INPUT);

  for (int i = 0; i < 8; i++) {
    digitalWrite(pins[i], 1);
    delay(100);
    digitalWrite(pins[i], 0);
    if (i <= 7) {
      digitalWrite(pins[i+1], 1);
      
    }
    else {
      digitalWrite(pins[i], 1);
    }
  }




  

}

void loop() {
  if (digitalRead(PushBTN1) == 1) {

      if (counter >= 255) {
        counter = 0;
      }
      
      if (counter <= 255) {
      inByte = byte(counter);
      counter++;
      }

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
      delay(100);
  }
}
   

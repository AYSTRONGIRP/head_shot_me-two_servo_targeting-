String loc[2];
String temp ="";
int counter = 0;
void setup() {
  Serial.begin(9600); 
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
  delay(100);
  if (Serial.available() > 0) { 
    String msg = Serial.readString();
    counter=0;
    loc[0]="";
    loc[1]="";
    temp = "";
    for(int i = 0 ; i < msg.length();i++)
    {
      if(counter==1)
        temp=temp+msg[i];
      if(msg[i]==',')
      {
        loc[counter]=temp;
        temp = "" ;
        if(counter==0)
        counter=1;
        else
        counter=0;
        continue;
      }
      if(counter==0)
      temp=temp+msg[i];
    }
    loc[1]=temp;

    Serial.println(loc[1]);
   
  }
  
}

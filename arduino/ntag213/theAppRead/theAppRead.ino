  #include <SPI.h>
  #include <MFRC522.h>


  #define SS_PIN          10
  #define RST_PIN         9

  MFRC522 mfrc522(SS_PIN, RST_PIN);  
  MFRC522::StatusCode status; 

  byte buffer[18];  //data transfer buffer (16+2 bytes data+CRC)
  byte size = sizeof(buffer);

  uint8_t pageAddr = 0x06;  //In this example we will write/read 16 bytes (page 6,7,8 and 9).
                            //Ultraligth mem = 16 pages. 4 bytes per page. 
                            //Pages 0 to 4 are for special functions.           
  int last = -1;
void setup() {
  Serial.begin(9600); // Initialize serial communications with the PC
  SPI.begin(); // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card 
  memcpy(buffer,"yo WORLD! ;-)",16);
}

void loop() {
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent())
    return;

  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial())
    return;


 



  // Read data ***************************************************
  //data in 4 block is read at once.
  status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(pageAddr, buffer, &size);
  if (status != MFRC522::STATUS_OK) {
    Serial.print(F("MIFARE_Read() failed: "));
    Serial.println(mfrc522.GetStatusCodeName(status));
    return;
  }
  int a = buffer[0];
  if(a!=last){
    Serial.println(a);
    last=a;
  }

  mfrc522.PICC_HaltA();

}

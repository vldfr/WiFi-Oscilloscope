#include <SPI.h>
#include <WiFi.h>
#include <WebSocketsClient.h>

#define AUTH_NAME "TestTemperature"
#define AUTH_PASS "YHae75JTr9peb7D"
#define INPUTS "\"temp\":{\"type\":\"Temperature\"}"

#define USE_SERIAL Serial

char ssid[] = "tmc2Ghz";          //  your network SSID (name) 
char pass[] = "@tmc2guest";   // your network password
bool registered = false;
bool logged_in = false;

WebSocketsClient webSocket;

void hexdump(const uint8_t* pData, uint32_t length) {
  char ascii[80];
  char hex[80];
  char tempBuf[80];
  uint32_t lineNumber = 0;

  ESP_LOGV(LOG_TAG, "     00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f");
  ESP_LOGV(LOG_TAG, "     -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --");
  strcpy(ascii, "");
  strcpy(hex, "");
  uint32_t index = 0;
  while (index < length) {
    sprintf(tempBuf, "%.2x ", pData[index]);
    strcat(hex, tempBuf);
    if (isprint(pData[index])) {
      sprintf(tempBuf, "%c", pData[index]);
    } else {
      sprintf(tempBuf, ".");
    }
    strcat(ascii, tempBuf);
    index++;
    if (index % 16 == 0) {
      ESP_LOGV(LOG_TAG, "%.4x %s %s", lineNumber * 16, hex, ascii);
      strcpy(ascii, "");
      strcpy(hex, "");
      lineNumber++;
    }
  }
  if (index %16 != 0) {
    while (index % 16 != 0) {
      strcat(hex, "   ");
      index++;
    }
    ESP_LOGV(LOG_TAG, "%.4x %s %s", lineNumber * 16, hex, ascii);
  }
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {

  switch(type) {
    case WStype_DISCONNECTED:
      USE_SERIAL.printf("[WSc] Disconnected!\n");
      logged_in = false;
      registered = false;
      break;
    case WStype_CONNECTED: {
      USE_SERIAL.printf("[WSc] Connected to url: %s\n", payload);

      // send message to server when Connected
//      webSocket.sendTXT("Connected");
    }
      break;
    case WStype_TEXT:
      USE_SERIAL.printf("[WSc] get text: %s\n", payload);

      // send message to server
      // webSocket.sendTXT("message here");
      break;
    case WStype_BIN:
      USE_SERIAL.printf("[WSc] get binary length: %u\n", length);
      hexdump(payload, length);

      // send data to server
      // webSocket.sendBIN(payload, length);
      break;
        case WStype_PING:
            // pong will be send automatically
            USE_SERIAL.printf("[WSc] get ping\n");
            break;
        case WStype_PONG:
            // answer to a ping we send
            USE_SERIAL.printf("[WSc] get pong\n");
            break;
    }

}


int status = WL_IDLE_STATUS;
IPAddress server(192,168,1,178);  // MAX Local server


void setup() {
  USE_SERIAL.begin(9600);
  USE_SERIAL.println("Attempting to connect to network...");
  USE_SERIAL.print("SSID: ");
  USE_SERIAL.println(ssid);

  WiFi.begin(ssid, pass);
  while(WiFi.status() != WL_CONNECTED){
    USE_SERIAL.print(".");
    delay(5);
  }
  USE_SERIAL.println("\nConnected");

  webSocket.begin("192.168.1.178", 8000, "/device/TestTemperature/");

  webSocket.onEvent(webSocketEvent);

  webSocket.setReconnectInterval(5000);
}

void loop() {
  webSocket.loop();
  if(!logged_in){
    char request_login[50] = {0};
    strcat(request_login, "{\"request\":\"login\", \"data\":\"");
    strcat(request_login, AUTH_PASS);
    strcat(request_login, "\"}");
    if(webSocket.sendTXT(request_login))
      logged_in = true;
    delay(500);
  }
  else{
    if(!registered){
      char request_register[50] = {0};
      strcat(request_register, "{\"request\":\"register\", \"data\":{\"name\":\"Test Sensor\", \"sensors\":{");
      strcat(request_register, INPUTS);
      strcat(request_register, "}}}");
      if(webSocket.sendTXT(request_register))
        registered = true;
      delay(500);
    }
    else{
      USE_SERIAL.println("sending");
      // Send message:

      char request_send[50]={0};
      strcat(request_send, "{\"request\":\"send\", \"data\":{\"sensors\":{\"temp\":\"");
      char sends[50];
      itoa(millis(), sends, 10);
      strcat(request_send, sends);
      strcat(request_send, " degC\"}}}");
      webSocket.sendTXT(request_send);
      delay(1000);
    }
  }
}

'''
Het request van esp_1_brightspace was eerst:

GET http://1.1.1.1/index.html HTTP/1.0
Host: www.avans.nl
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us

Volgens https://datatracker.ietf.org/doc/html/rfc2616#section-14.23 moet dit worden:

GET /index.html HTTP/1.0
Host: www.avans.nl
User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us

Nadat de ESP-01 handmatig is ingelogd dmv SSID en wachtwoord is de output:

xxx

Dit werkt dus niet.
'''

################################################################################
# desc: testcase connecting and retrieving a website using #
# AT commands on ESP8266 #
# #
# file: F04.get website.py #
# author: JSC #
# date: 2019-08-28 #
# copyright: JSC - 2019 #
# #
################################################################################
# Version history #
################################################################################
# 2019-08-28 - JSC - initial version
#
# #
# #
################################################################################
import time
import serial

def read_from_port(ser):
    while (ser.in_waiting > 0): #if incoming bytes are waiting to be read from the serial input buffer
        data_str = ser.read(ser.in_waiting ).decode('ascii') #read the bytes and convert from binary array to ASCII
        print(data_str, end='') #print the incoming string without putting a newline ('\n') automatically after every print()
    #Put the rest of your code you want here

# send data to serial port and read its response
# ser: serial port
# data: data to be send (byte array)
def send_and_read(ser,data):
    wait_time = 0.1 # in seconds
    time.sleep(wait_time)
    ser.write(data)
    time.sleep(wait_time)
    read_from_port(ser)
    time.sleep(wait_time)

# Open serial port
esp8266 = serial.Serial("COM4", 115200, timeout=60)
try:
    # get status
    send_and_read(esp8266, b'AT+CIFSR\r\n')
    send_and_read(esp8266, b'AT+CIPSTART="TCP","avans.nl",80\r\n')
 
    # sending http request
    # 1. send length of request
    # 2. send actual message
    request = 'GET /index.html HTTP/1.0\r\n' \
    'Host: www.avans.nl\r\n' \
    'User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)\r\n' \
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n' \
    'Accept-Language: en-us\r\n' \
    '\r\n\r\n'
    send_and_read(esp8266, ('AT+CIPSEND=' + str(len(request)) + '\r\n').encode())
    send_and_read(esp8266, b'AT+CIPSEND\r\n')
    send_and_read(esp8266, (request).encode())
    time.sleep(1)
    read_from_port(esp8266)

    # close connection
    send_and_read(esp8266, b'AT+CIPCLOSE\r\n')
finally:
    esp8266.close()

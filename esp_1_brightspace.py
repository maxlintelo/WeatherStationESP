import time
import serial

def send_and_read(ser,data):
    time.sleep(0.1)
    ser.write(data)
    time.sleep(0.1)
    while (ser.in_waiting > 0): #if incoming bytes are waiting to be read from the serial input buffer
        data_str = ser.read(ser.in_waiting ).decode('ascii') #read the bytes and convert from binary array to ASCII
        print(data_str, end='')
    time.sleep(0.1)

# Open serial port
esp8266 = serial.Serial("COM4", 115200, timeout=60)
try:
    # get status
    send_and_read(esp8266, b'AT+CIFSR\r\n')
    send_and_read(esp8266, b'AT+CIPSTART="TCP","avans.nl",80\r\n')
 
    # sending http request
    # 1. send length of request
    # 2. send actual message
    request = 'GET / HTTP/1.0\r\n' \
    'Host: www.avans.nl\r\n' \
    '\r\n\r\n'

    send_and_read(esp8266, ('AT+CIPSEND=' + str(len(request)) + '\r\n').encode())
    # send_and_read(esp8266, b'AT+CIPSEND\r\n')
    send_and_read(esp8266, (request).encode())
    time.sleep(1)

    # close connection
    send_and_read(esp8266, b'AT+CIPCLOSE\r\n')
finally:
    esp8266.close()

import time
import serial

def read_from_port(ser):
    while (ser.in_waiting > 0): #if incoming bytes are waiting to be read from the serial input buffer
        data_str = ser.read(ser.in_waiting ).decode('ascii') #read the bytes and convert from binary array to ASCII
        print(data_str, end='') #print the incoming string without putting a newline ('\n') automatically after every print()

def send_and_read(ser,data):
    wait_time = 0.1
    time.sleep(wait_time)
    ser.write(data)
    time.sleep(wait_time)
    read_from_port(ser)
    time.sleep(wait_time)

esp8266 = serial.Serial("COM4", 115200, timeout=60)
try:
    send_and_read(esp8266, b'AT+CIFSR\r\n')
    send_and_read(esp8266, b'AT+CIPSTART="TCP","81.207.176.52",8081\r\n')

    request = 'GET / HTTP/1.1' \
    '\r\n\r\n'
    send_and_read(esp8266, ('AT+CIPSEND=' + str(len(request)) + '\r\n').encode())
    time.sleep(1)
<<<<<<< HEAD
    # send_and_read(esp8266, b'AT+CIPSEND\r\n')
=======
>>>>>>> acf14a5457366c93f2c4a191dfba41e45e960261
    send_and_read(esp8266, (request).encode())
    time.sleep(1)
    read_from_port(esp8266)

    send_and_read(esp8266, b'AT+CIPCLOSE\r\n')
finally:
    esp8266.close()
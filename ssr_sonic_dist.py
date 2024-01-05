import RPi.GPIO as GPIO
import serial

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
ser=serial.Serial("/dev/ttyACM0",9600)

while True:
  try:
    line = ser.readline()
    dist=float(line.decode('utf-8'))
    print(dist)
    if dist < 10.0:
      GPIO.output(14,GPIO.HIGH)
    else:
      GPIO.output(14,GPIO.LOW)
  except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
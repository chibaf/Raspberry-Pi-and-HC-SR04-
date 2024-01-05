import RPi.GPIO as GPIO
from sonic_sensor_class import sonic_sensor

while True:
  try:
    sonic=sonic_sensor(23,24)
    distance=sonic.dist(23,24)
    print(distance)
  except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
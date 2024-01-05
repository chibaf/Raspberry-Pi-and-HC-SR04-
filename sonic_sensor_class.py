class sonic_sensor:

  def __init__(self,TRIG,ECHO): #TRIG=23 #ECHO=24
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
#    print("Wating for sensor to settle")
    time.sleep(1)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

  def dist(self,TRIG,ECHO):
    import RPi.GPIO as GPIO
    import time
    while GPIO.input(ECHO)==0:
      pulse_start=time.time()
    while GPIO.input(ECHO)==1:
      pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    return distance

#print("distance:",distance,"cm")
#GPIO.cleanup()

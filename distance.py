import RPi.GPIO as GPIO
import time

TRIG = 23  # 초음파 트리거 핀
ECHO = 24  # 초음파 에코 핀

def setup_distance_pin():
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
      
def measure_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False) 
    start, stop = 0, 0
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()
    distance = int((stop - start) * 34300 / 2)
    return distance

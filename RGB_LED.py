import RPi.GPIO as GPIO
import time

RGB_PINS = {'R': 26, 'G': 6, 'B': 13}  # RGB LED 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(list(RGB_PINS.values()), GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        print("Red LED ON")
        GPIO.output(RGB_PINS['R'], 1)
        time.sleep(1)
        GPIO.output(RGB_PINS['R'], 0)

        print("Green LED ON")
        GPIO.output(RGB_PINS['G'], 1)
        time.sleep(1)
        GPIO.output(RGB_PINS['G'], 0)

        print("Blue LED ON")
        GPIO.output(RGB_PINS['B'], 1)
        time.sleep(1)
        GPIO.output(RGB_PINS['B'], 0)
        
        print("Yellow LED ON")  # 노란색 (빨강 + 초록)
        GPIO.output(RGB_PINS['R'], 1)
        GPIO.output(RGB_PINS['G'], 1)
        time.sleep(1)
        GPIO.output(RGB_PINS['R'], 0)
        GPIO.output(RGB_PINS['G'], 0)
except KeyboardInterrupt:
    GPIO.cleanup()

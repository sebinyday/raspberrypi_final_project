import RPi.GPIO as GPIO
import time

BUZZER = 25  # 부저 핀

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

try:
    while True:
        GPIO.output(BUZZER, GPIO.HIGH)  # 부저 켜기
        time.sleep(0.5)
        GPIO.output(BUZZER, GPIO.LOW)   # 부저 끄기
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()

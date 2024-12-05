import RPi.GPIO as GPIO
import time

RGB_PINS = {'R': 26, 'G': 6, 'B': 13}

def setup_rgb_pins():
    GPIO.setup(list(RGB_PINS.values()), GPIO.OUT, initial=GPIO.LOW)
    
# 각 색깔을 켜는 함수들
def red_led_on():
    print("Red LED ON")
    GPIO.output(RGB_PINS['R'], 1)
    
def red_led_off():
    GPIO.output(RGB_PINS['R'], 0)

def green_led_on():
    print("Green LED ON")
    GPIO.output(RGB_PINS['G'], 1)

def green_led_off():
    GPIO.output(RGB_PINS['G'], 0)

def purple_led_on():
    print("Purple LED ON")
    GPIO.output(RGB_PINS['B'], 1)
    GPIO.output(RGB_PINS['R'], 1)

def purple_led_off():
    GPIO.output(RGB_PINS['B'], 0)
    GPIO.output(RGB_PINS['R'], 0)

def yellow_led_on():
    print("Yellow LED ON")  # 노란색은 빨강 + 초록
    GPIO.output(RGB_PINS['R'], 1)
    GPIO.output(RGB_PINS['G'], 1)

def yellow_led_off():
    GPIO.output(RGB_PINS['R'], 0)
    GPIO.output(RGB_PINS['G'], 0)

def all_led_off():
    GPIO.output(RGB_PINS['R'], 0)
    GPIO.output(RGB_PINS['G'], 0)
    GPIO.output(RGB_PINS['B'], 0)

# try:
#     while True:
#         red_led_on()
#         time.sleep(1)
#         red_led_off()

#         green_led_on()
#         time.sleep(1)
#         green_led_off()

#         blue_led_on()
#         time.sleep(1)
#         blue_led_off()

#         yellow_led_on()
#         time.sleep(1)
#         yellow_led_off()

# except KeyboardInterrupt:
#     GPIO.cleanup()

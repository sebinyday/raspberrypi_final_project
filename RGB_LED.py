import RPi.GPIO as GPIO
import time

RGB_PINS = {'R': 26, 'G': 12, 'B': 13}

def setup_rgb_pins():
    GPIO.setup(list(RGB_PINS.values()), GPIO.OUT, initial=GPIO.LOW)

# 각 색깔을 켜고 끄는 함수들
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
    print("Yellow LED ON") 
    GPIO.output(RGB_PINS['R'], 1)
    GPIO.output(RGB_PINS['G'], 1)

def yellow_led_off():
    GPIO.output(RGB_PINS['R'], 0)
    GPIO.output(RGB_PINS['G'], 0)

def all_led_off():
    GPIO.output(RGB_PINS['R'], 0)
    GPIO.output(RGB_PINS['G'], 0)
    GPIO.output(RGB_PINS['B'], 0)


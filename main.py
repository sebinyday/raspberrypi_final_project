import RPi.GPIO as GPIO
from BUZZER import *
from RGB_LED import *
from LCD import *
from distance import *
from face_recognition_def import *
import smbus
import cv2
import numpy as np

# GPIO 초기화 (한 번만 호출)
GPIO.setmode(GPIO.BCM)

# 각 모듈에서 GPIO 핀 설정을 하도록 변경
setup_rgb_pins()
setup_buzzer_pin()
setup_distance_pin()
lcd_init()

family = ["sebin", "mom","dad"]
distance = measure_distance()

# 거리 조건이 만족되지 않으면 경고 반복
while distance < 20 or distance > 60:
    
    purple_led_on()
    print_sound_false()  # 거리 경고 소리
    time.sleep(1)
    purple_led_off()
    if distance <20 :
        lcd_message(f"Please step back.", 1)
        lcd_message(f"Distance: {distance} cm", 2)
    elif distance >60 :
        lcd_message(f"Please come closer.", 1)
        lcd_message(f"Distance: {distance} cm", 2)
    
    # 거리 재측정 (다시 정상 범위가 될 때까지 기다림)
    distance = measure_distance()  # 거리 측정 함수 호출
    time.sleep(1)

user_id, face_recognized, confidence = recognize_face()
print(f"User ID: {user_id}, Face Recognized: {face_recognized},Confidence: {confidence}")

# 거리 조건이 맞으면 얼굴 인식 시작
while not face_recognized:  # 얼굴 인식 실패 시 반복
    user_id, face_recognized, confidence = recognize_face()  # 얼굴 인식 재시도
    yellow_led_on()  # 노란색 LED
    print_sound_false()  # 오답 소리
    time.sleep(0.5)
    yellow_led_off()
    lcd_message("Try Again.", 1)  # 첫 번째 줄 출력
    time.sleep(2)
    print("얼굴 인식 실패, 다시 시도합니다.")
    print(f"User ID: {user_id}, Face Recognized: {face_recognized}, Confidence: {confidence}")
    lcd_init()

# 얼굴 인식 성공 시 처리
if face_recognized:
    if user_id in family:
        green_led_on()  # 초록색 LED
        print_sound_true()  # 정답 소리
        time.sleep(0.5)
        green_led_off()
        lcd_message(f"Welcome! {user_id}:)", 1)  # 첫 번째 줄 출력
        lcd_message("Have a Good Day.", 2)  # 두 번째 줄 출력
        time.sleep(2)
        lcd_init()
    elif user_id == "Unknown":
        red_led_on()  # 빨간색 LED
        print_sound_false()  # 오답 소리
        time.sleep(0.5)
        red_led_off()
        lcd_message("Hello, Stranger!", 1)  # 첫 번째 줄 출력
        lcd_message("Who are you? :(", 2)  # 두 번째 줄 출력
        time.sleep(2)
        lcd_init()

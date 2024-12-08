import RPi.GPIO as GPIO
import time
from BUZZER import *
from RGB_LED import *
from LCD import *
from distance import *
from face_recognition_def import *

# GPIO 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# 모듈별 핀 설정
setup_rgb_pins()
setup_buzzer_pin()
setup_distance_pin()
lcd_init()

# 가족 목록
family = ["sebin", "mom", "dad"]

try:
    while True:
        # 거리 측정
        distance = measure_distance()

        # 1m 이상이면 아무 동작도 하지 않음
        if distance >= 100:
            # print(f"Distance is {distance} cm (Out of range). No action taken.")
            time.sleep(2)  # 대기 후 다시 거리 측정
            continue

        # 거리 경고 루프 
        while distance < 20 or (distance > 60 and distance < 100):  
            purple_led_on()
            print_sound_false() 

            if distance < 20:
                lcd_message("Plz step back.", 1)
                lcd_message(f"Distance: {distance} cm", 2)
            elif distance > 60:
                lcd_message("Plz come closer.", 1)
                lcd_message(f"Distance: {distance} cm", 2)
            time.sleep(2)
            purple_led_off()
            lcd_init()
            # 거리 재측정
            distance = measure_distance()
            time.sleep(1)

        # 거리 조건 만족 시 얼굴 인식 시작
        user_id, face_recognized, confidence = recognize_face()
        # print(f"User ID: {user_id}, Face Recognized: {face_recognized}, Confidence: {confidence}")

        # 얼굴 인식 실패 시 반복
        while not face_recognized:
            user_id, face_recognized, confidence = recognize_face()  # 얼굴 인식 재시도
            yellow_led_on()
            print_sound_false()  # 얼굴 인식 실패 소리
            lcd_message("Try Again.", 1)
            time.sleep(2)
            yellow_led_off()
            lcd_init()
            # print("얼굴 인식 실패, 다시 시도합니다.")

        # 얼굴 인식 성공 시 처리
        if face_recognized:
            if user_id in family:
                green_led_on()
                print_sound_true()  # 환영음
                lcd_message(f"Welcome {user_id} :)", 1)
                lcd_message("Have a Good Day.", 2)
                time.sleep(2)
                green_led_off()
                lcd_init()
                # print(distance)

            elif user_id == "Unknown":
                red_led_on()
                print_sound_false()  # 경고음
                time.sleep(0.5)
                print_sound_false()  # 경고음
                lcd_message("Hello, Stranger!", 1)
                lcd_message("Who are you? :(", 2)
                time.sleep(2)
                red_led_off()
                lcd_init()
                # print(distance)

        time.sleep(5)  
        # 시스템 초기화 및 대기 상태 복귀
        print("Resetting system to initial state...")
        lcd_init()  # LCD 초기화
        all_led_off()  # 모든 LED 끄기 
        distance = measure_distance()  # 새로운 거리 측정 시작
        time.sleep(1) 
finally:
    GPIO.cleanup()  # GPIO 리소스 정리
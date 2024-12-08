import RPi.GPIO as GPIO
import time

BUZZER_PIN = 25

def setup_buzzer_pin():
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    
# 부저로 소리 내기 함수
def sound_buzzer(frequency, duration):
    pwm = GPIO.PWM(BUZZER_PIN, frequency)
    pwm.start(50)  # 듀티 사이클 50%
    time.sleep(duration)  # 지속 시간
    pwm.stop()

# 정답 소리 함수 (딩동댕동)
def print_sound_true():
    sound_buzzer(261.63, 0.3)  # 도 (C)
    sound_buzzer(329.63, 0.3)  # 미 (E)
    sound_buzzer(392.00, 0.3)  # 솔 (G)
    sound_buzzer(523.25, 0.3)  # 높은 도 (2C) 
    time.sleep(1)  

# 오답 소리 함수 (오답 소리)
def print_sound_false():
    sound_buzzer(500, 0.2)  # 주파수 500Hz
    time.sleep(0.1)
    sound_buzzer(500, 0.2)  
    time.sleep(0.1)
    sound_buzzer(500, 0.2)  
    time.sleep(1)

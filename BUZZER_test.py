import RPi.GPIO as GPIO
import time

# 부저 핀 설정
BUZZER_PIN = 25

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 부저로 소리 내기 함수
def sound_buzzer(frequency, duration):
    pwm = GPIO.PWM(BUZZER_PIN, frequency)
    pwm.start(50)  # 듀티 사이클 50%
    time.sleep(duration)  # 지정된 시간동안 소리 내기
    pwm.stop()

# 정답 소리 함수 (띠링 소리: 도미솔도)
def print_sound_true():
    sound_buzzer(261.63, 0.3)  # 도 (C) 261.63Hz, 0.3초
    sound_buzzer(329.63, 0.3)  # 미 (E) 329.63Hz, 0.3초
    sound_buzzer(392.00, 0.3)  # 솔 (G) 392.00Hz, 0.3초
    sound_buzzer(523.25, 0.3)  # 높은 도 (2C) 523.25Hz, 0.3초
    time.sleep(1)  # 잠깐 멈춤

# 오답 소리 함수 (오답 소리)
def print_sound_false():
    sound_buzzer(500, 0.2)  # 주파수 500Hz, 0.2초
    time.sleep(0.1)
    sound_buzzer(500, 0.2)  # 주파수 500Hz, 0.2초
    time.sleep(0.1)
    sound_buzzer(500, 0.2)  # 주파수 500Hz, 0.2초
    time.sleep(1)

# 메인 코드 예시
try:
    while True:
        # 정답일 때
        print("정답입니다!")
        print_sound_true()  # 정답 소리 출력

        # 오답일 때
        print("오답입니다!")
        print_sound_false()  # 오답 소리 출력

except KeyboardInterrupt:
    GPIO.cleanup()  # 종료 시 GPIO 정리

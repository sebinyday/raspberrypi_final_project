import smbus
import time

# I2C 설정
I2C_ADDR = 0x27  # I2C 주소 (sudo i2cdetect -y 1로 확인)
LCD_WIDTH = 16   # LCD 한 줄의 문자 수
bus = smbus.SMBus(1)

# LCD 초기화
def lcd_init():
    lcd_byte(0x33, 0)  # 초기화 명령
    lcd_byte(0x32, 0)  # 4비트 모드 설정
    lcd_byte(0x28, 0)  # 2줄 모드
    lcd_byte(0x0C, 0)  # 디스플레이 켜기, 커서 숨김
    lcd_byte(0x06, 0)  # 글자 쓰기 후 커서 이동
    lcd_byte(0x01, 0)  # 화면 지우기
    time.sleep(0.005)

# 명령어 및 문자 전송
def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | 0x08  # 상위 비트
    bits_low = mode | ((bits << 4) & 0xF0) | 0x08  # 하위 비트
    bus.write_byte(I2C_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(I2C_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

# LCD 활성화 신호
def lcd_toggle_enable(bits):
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits | 0x04))  # Enable 신호 ON
    time.sleep(0.0005)
    bus.write_byte(I2C_ADDR, (bits & ~0x04))  # Enable 신호 OFF
    time.sleep(0.0005)

# 메시지 출력 함수
def lcd_message(message, line):
    if line == 1:
        lcd_byte(0x80, 0)  # 첫 번째 줄
    elif line == 2:
        lcd_byte(0xC0, 0)  # 두 번째 줄
    message = message.ljust(LCD_WIDTH, " ") 
    for char in message:
        lcd_byte(ord(char), 1)

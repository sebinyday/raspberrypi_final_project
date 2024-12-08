# 스마트 가족 보안 시스템 (Smart Family Security System)

이 프로젝트는 라즈베리파이를 이용하여 얼굴 인식 및 거리 측정을 기반으로 보안 시스템을 구현한 프로젝트입니다. 주된 기능은 사용자가 적절한 거리 범위 내에 있을 경우, 사용자 얼굴을 인식하고 가족 구성원에 속하는지 아닌지를 구분하는 것입니다. 이 시스템은 인식된 얼굴이 가족 구성원에 속하면 환영 메시지를 출력하고, 외부인 또는 거리 범위를 벗어난 경우 경고 메시지를 출력합니다.

## 기능

- **얼굴 인식**: 웹 카메라를 사용하여 등록된 사용자의 얼굴을 인식하고, 해당 사용자에게 환영 메시지를 출력합니다.
  - 사용자의 얼굴을 등록하기 위해, 100장의 이미지를 찍어 데이터셋으로 저장하고, trainer.py를 통해 학습합니다.

- **거리 측정**: 초음파 센서를 이용하여 사용자와의 거리를 측정하고, 특정 범위 내에 있을 경우 얼굴 인식을 진행합니다.
- **LED 표시**: 초록색, 빨간색, 노란색, 보라색 등 상황에 맞게 다양한 LED 색상을 사용하여 상태를 표시합니다.
- **부저**: 사용자 인식 여부와 거리 범위에 따라 경고음을 출력합니다.

## 동작 흐름

1. **거리 측정**:
   - 시스템은 먼저 초음파 센서를 이용해 사용자의 거리를 측정합니다.
        - 거리가 너무 가까운 경우 ("Plz step back.") 
        - 거리가 너무 먼 경우 ("Plz come closer.") \
        LCD에 경고 메시지와 "distance :[거리]cm" 를 출력합니다.

2. **얼굴 인식**:
   - 적절한 거리 범위(30cm ~ 60cm) 내에서 얼굴 인식을 진행합니다.
   - 등록된 사용자가 인식되면 환영 메시지 "Welcome [ID] :) Have a Good Day."와 함께 LED가 초록색으로 켜지고, 긍정적인 소리(딩동댕동)가 출력됩니다.
   - 얼굴이 인식되지 않은 경우 얼굴이 인식될때까지 재시도합니다. "Try Again."이라는 문구와 동시에 LED가 노란색으로 켜지고 경고음이 출력됩니다.
    - 등록되지 않은 사용자가 인식되면 "Hello, Stranger! Who are you? :(" 라는 문구와 빨간색 LED, 경고음이 출력됩니다.


## 요구사항

- **하드웨어**:
  - Raspberry Pi
  - USB 웹캠
  - 초음파 센서 (HC-SR04)
  - RGB LED (Red, Green, Blue)
  - 부저 (Buzzer)
  - LCD 디스플레이

- **소프트웨어**:
  - Python 3
  - OpenCV (얼굴 인식)
  - RPi.GPIO (라즈베리파이 GPIO 제어)

## 설치

1. 라즈베리파이에 Python 3.x를 설치합니다.
2. 필요한 라이브러리를 설치합니다:
   ```bash
   pip install opencv-python RPi.GPIO numpy
3. 프로젝트 파일을 클론하거나 다운로드합니다:
    ```bash
    git clone <프로젝트 URL>
    cd <프로젝트 폴더>
    ```
4. 얼굴 인식 모델을 준비합니다:
- OpenCV의 얼굴 인식 모델(haarcascade_frontalface_default.xml)과 학습된 얼굴 인식 파일(trainer.yml)을 준비하고 프로젝트에 포함시킵니다.
    ```bash
    wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
    ```
5. 시스템을 실행합니다:
    ```bash
    python main.py
    ```

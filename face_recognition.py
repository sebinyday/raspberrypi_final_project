### test용 얼굴인식 웹버전

from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

# LBPH 얼굴 인식 모델 로드
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# 얼굴 인식용 Haar Cascade 로드
faceCascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

# ID와 이름 설정 (예시)
names = ["?",'sebin','mom','dad']

# 웹캠 열기
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # 비디오 가로 크기 설정
cam.set(4, 480)  # 비디오 세로 크기 설정

# 얼굴 인식 결과를 이미지로 스트리밍하는 함수
def gen_frames():
    while True:
        ret, img = cam.read()
        #img = cv2.flip(img, -1)  # 이미지 반전

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            # 얼굴 주변에 사각형 그리기
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # 얼굴 부분 예측
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            # 신뢰도가 100보다 작으면 얼굴 인식 성공
            if confidence < 100:
                id = names[id]
                confidence = f"  {round(100 - confidence)}%"
            else:
                id = "Unknown"
                confidence = f"  {round(100 - confidence)}%"

            # 얼굴 ID와 신뢰도를 화면에 출력
            cv2.putText(img, str(id), (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)

        # 이미지 스트리밍을 위한 JPEG 인코딩
        ret, buffer = cv2.imencode('.jpg', img)
        img_bytes = buffer.tobytes()

        # 스트리밍을 위한 응답 생성
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + img_bytes + b'\r\n')

# 기본 페이지 라우팅
@app.route('/')
def index():
    return render_template('index2.html')

# 비디오 스트리밍 라우팅
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

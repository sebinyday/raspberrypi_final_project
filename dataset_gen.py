from flask import Flask, render_template, Response
import cv2
import os
import time

app = Flask(__name__)

# OpenCV 설정
capture = cv2.VideoCapture(0)  # 기본 카메라 사용
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Haar Cascade 로드 (얼굴 감지용)
face_cascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

# 데이터셋 폴더 설정
dataset_folder = "dataset"  # 얼굴 이미지를 저장할 폴더
if not os.path.exists(dataset_folder):
    os.makedirs(dataset_folder)

# 얼굴 이미지 저장 카운트
face_id = "1"  # 사용자 ID
name = "sebin"  # 사용자 이름
count = 0
capturing = True  # 데이터 수집 여부를 결정하는 변수

# 마지막 사진을 찍은 시간 기록
last_capture_time = time.time()

def gen_frames():
    global count, capturing, last_capture_time
    while capturing:
        ret, frame = capture.read()
        if not ret:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

            # 얼굴이 감지되고, 마지막 촬영 시간 이후 0.1초가 지났으면 사진 촬영
            if len(faces) > 0 and time.time() - last_capture_time >= 0.1:
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 얼굴에 박스 그리기

                    # 얼굴 이미지를 dataset 폴더에 저장
                    face_image = gray[y:y + h, x:x + w]
                    cv2.imwrite(f"{dataset_folder}/User_{face_id}_{name}_{count + 1}.jpg", face_image)
                    count += 1

                    # 마지막 촬영 시간 갱신
                    last_capture_time = time.time()

                    if count >= 100:  # 얼굴 이미지를 100장 찍으면 종료
                        capturing = False
                        break

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # 종료 후 추가 처리
    print("100장 촬영 완료! 데이터 수집을 종료합니다.")
    capture.release()
    cv2.destroyAllWindows()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

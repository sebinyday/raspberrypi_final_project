import cv2
import numpy as np
import os

# LBPH 얼굴 인식 모델 로드
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

# 얼굴 인식용 Haar Cascade 로드
faceCascade = cv2.CascadeClassifier('../haarcascade_frontalface_default.xml')

# ID와 이름 설정 (예시)
names = ["?", 'sebin', 'mom', 'dad']

# 얼굴 인식 함수
def recognize_face():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("카메라를 열 수 없습니다.")
        return "Unknown", False,None

    cam.set(3, 640)  # 비디오 가로 크기 설정
    cam.set(4, 480)  # 비디오 세로 크기 설정

    ret, img = cam.read()
    if not ret:
        print("이미지 캡처 실패")
        cam.release()
        return "Unknown", False,None

    #print("이미지 캡처 성공")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if len(faces) == 0:
        #print("얼굴이 감지되지 않았습니다.")
        cam.release()
        return "Unknown", False, None

    print(f"얼굴이 {len(faces)}개 감지되었습니다.")

    user_id = "Unknown"
    face_recognized = False

    # 저장할 폴더 경로 지정
    save_dir = 'test'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for i, (x, y, w, h) in enumerate(faces):
        # 얼굴 예측
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if confidence < 100:
            user_id = names[id]
            confidence = f"  {round(100 - confidence)}%"
            face_recognized = True
        else:
            user_id = "Unknown"
            confidence = f"  {round(100 - confidence)}%"
            face_recognized = True

        # 얼굴 ID와 신뢰도 출력 (디버그용)
        # print(f"Predicted ID: {user_id}, Confidence: {confidence}")

        # 얼굴 영역 추출
        face_img = img[y:y + h, x:x + w]

        # 이미지 파일로 저장 (예: test/face_0.jpg, face_1.jpg, ...)
        img_filename = os.path.join(save_dir, f"face_{i}.jpg")
        cv2.imwrite(img_filename, face_img)
        #print(f"얼굴 이미지를 저장했습니다: {img_filename}")

    cam.release()  # 웹캠 닫기
    return user_id, face_recognized, confidence

# 테스트
# user_id, face_recognized = recognize_face()
# print(f"User ID: {user_id}, Face Recognized: {face_recognized}")

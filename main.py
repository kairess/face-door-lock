from dynamikontrol import Module
import cv2
from deepface import DeepFace
from pathlib import Path
# 아래 링크에서 파일을 다운로드 받아, {HOME_FOLDER}/.deepface/weights 폴더에 복사하세요.
# https://drive.google.com/uc?id=1CPSeum3HpopfomUEK1gybeuIVoeJT_Eo
home = str(Path.home())
print('HOME_FOLDER is ', home)

my_img = 'db/brad/05.jpg'

cap = cv2.VideoCapture(0)

module = Module()
module.motor.angle(-85)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    result = DeepFace.verify(img1_path=my_img, img2_path=img, enforce_detection=False)

    if result['verified']:
        text = 'Open'
        color = (0, 255, 0)
        module.motor.angle(85)
    else:
        text = 'Close'
        color = (0, 0, 255)
        module.motor.angle(-85)

    cv2.putText(img, text=text, org=(int(img.shape[1] / 2), int(img.shape[0] / 2)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=color, thickness=3)

    cv2.imshow('Face Lock', img)
    if cv2.waitKey(5000) == ord('q'):
        break

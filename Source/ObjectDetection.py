import cv2
from gtts import gTTS
import os
from deep_translator import GoogleTranslator
import pygame
from tkinter import messagebox
import Function

pygame.mixer.init()

# Thong tin ten vat the
classNames = []
classFile = "./Models/coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

# Thong tin hinh dang vat the
configPath = "./Models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "./Models/frozen_inference_graph.pb"

# Khoi tao mo hinh DNN
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    if len(objects) == 0:
        objects = classNames
    objectInfo = []
    dist = None
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

                    img, dist = get_dist(box, img)
                break
    return img, objectInfo, dist

def get_dist(rectangle_params, image):
    known_width = 10.0
    focal_length = 615

    pixels = rectangle_params[2]
    dist = (known_width * focal_length) / pixels
    org = (rectangle_params[0], rectangle_params[1] - 10)

    image = cv2.putText(image, f'Cach vat the khoang: {dist:.2f} cm', org, cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2, cv2.LINE_AA)

    return image, dist

def speak(text):
    tts = gTTS(text=text, lang='vi')
    if os.path.exists("./object.mp3"):
        os.remove("./object.mp3")
    tts.save("./object.mp3")
    pygame.mixer.music.load("./object.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    os.remove("./object.mp3")
    
def process_video_feed(mode=2):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        if mode == 1:
            result, objectInfo, dist = getObjects(img, 0.45, 0.2)
            if objectInfo:
                for obj in objectInfo:
                    translated_text = GoogleTranslator(source='auto', target='vi').translate(obj[1])
                    print(f"Xác định vật thể: {translated_text}")
                    speak(f"Xác định vật thể: {translated_text}")
                    print(f"Khoảng cách đến {translated_text} là: {dist:.2f} cm")
                    speak(f"Khoảng cách đến {translated_text} là: {dist:.2f} cm")
            mode = 2
        elif mode == 2:
            result, objectInfo, _ = getObjects(img, 0.45, 0.2)
            cv2.imshow("Press 'q' to exit or 'c' to capture object", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            mode = 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def object_from_image():
    if not Function.pfile:
        messagebox.showerror("Error", "Please select image file first.")
        return
    img = cv2.imread(Function.pfile)
    result, objects, dist = getObjects(img, 0.45, 0.2)
    cv2.imshow('Detection Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
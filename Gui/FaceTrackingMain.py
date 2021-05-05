import cv2
import mediapipe as mp
import time

def faceTrack():
    cap = cv2.VideoCapture(0)
    pTime = 0

    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(0.75)

    while True:
        success, img = cap.read()

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
        results = faceDetection.process(imgRGB)
        print(results)

        if results.detections:
            for id, detection in enumerate(results.detections):
                print(id, detection)
                print(detection.score)
                print(detection.location_data.relative_bounding_box)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(img, bbox, (255, 0, 255), 2)
                cv2.putText(img, f' {int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0))

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (500, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))

        cv2.imshow("Image", img)
        cv2.waitKey(2)
        if cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) <1:
            break
cv2.destroyAllWindows()


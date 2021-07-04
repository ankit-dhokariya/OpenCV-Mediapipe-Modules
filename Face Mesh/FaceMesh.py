import cv2
import time
import FaceMeshModule as fm

cap = cv2.VideoCapture(0)
prevTime = 0
detector = fm.FaceMeshDetector()

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img)
    # "faces" contains a list of 468 landmarks for number of faces detected.

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime

    cv2.putText(img, f"FPS: {int(fps)}", (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)

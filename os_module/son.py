import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera nahi chal raha")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == 27:  # ESC press
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()

# val: str = input("Select Port: COM")


serial_inst.baudrate = 9600
serial_inst.port = "COM4"
serial_inst.open()

cap = cv2.VideoCapture(0)

pts = []
while 1:
    # Take each frame
    ret, izuku = cap.read()

    gray = cv2.cvtColor(izuku, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier("haar_face.xml")

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    if len(faces_rect) == 0:
        continue
    for x, y, w, h in faces_rect:
        cv2.rectangle(
            izuku,
            (x + w // 2, y + h // 4 - 1),
            (x + (w // 2), y + (h // 4)),
            (0, 255, 0),
            thickness=3,
        )
    x, y, w, h = faces_rect[0]

    command: str = str(x + w // 2) + "," + str(y + h // 4)
    serial_inst.write(command.encode("utf-8"))

    data = serial_inst.readline().decode().strip()
    print(data)

    cv2.imshow("Track Laser", izuku)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
serial_inst.close()

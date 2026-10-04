# Adapted/maintained by Adit Patidar.
# Original project: https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface
# See README.md for attribution and project notes.

import cv2 as cv
class C:
    def __init__(s, src=0):
        s.cap = cv.VideoCapture(src)
        if not s.cap.isOpened():

            raise IOError("Cannot open webcam.")
    def rd(s):
        ret, frm = s.cap.read()

        
        if not ret:
            return None
        return cv.flip(frm, 1)

    def rel(s):
        s.cap.release()
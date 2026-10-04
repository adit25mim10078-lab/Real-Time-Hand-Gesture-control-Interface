# Adapted/maintained by Adit Patidar.
# Original project: https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface
# See README.md for attribution and project notes.

import mediapipe as mp
import cv2 as cv
import math 

class HD:
    def __init__(s):
        s.mph = mp.solutions.hands
        s.hnd = s.mph.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def is_finger_extended(s, hand_landmarks):
        finger_status = [False] * 5
        
        thumb_tip = hand_landmarks.landmark[4]
        if thumb_tip.y < hand_landmarks.landmark[2].y:
             finger_status[0] = True
        
        tip_ids = [8, 12, 16, 20]
        
        for i, tip_id in enumerate(tip_ids):
            tip = hand_landmarks.landmark[tip_id]
            pip = hand_landmarks.landmark[tip_id - 2]
            
            if tip.y < pip.y:
                finger_status[i+1] = True

        return finger_status


    def get_advanced_gesture(s, finger_status):
        t, i, m, r, p = finger_status
        
        if all(finger_status):
            return "All Open"
        elif not any(finger_status):
            return "Closed Fist"
        elif t and not i and not m and not r and not p:
            return "Thumbs Up"
        elif not t and i and not m and not r and not p:
            return "Index Up (Pointing)"
        elif not t and not i and m and not r and not p:
            return "FUCK OFF!!!"
        elif not t and i and m and not r and not p:
            return "Peace Sign (V)"
        elif i and m and r and p and not t:
            return "STOP Hand"
        elif not t and not i and not m and not r and p:
            return "WASHROOM!"
        return "Other Gesture"
    def find(s, frm):
        frm_rgb = cv.cvtColor(frm, cv.COLOR_BGR2RGB)
        res = s.hnd.process(frm_rgb)
        if res.multi_hand_landmarks:
            lms = res.multi_hand_landmarks[0]
            finger_status = s.is_finger_extended(lms)
            gesture_name = s.get_advanced_gesture(finger_status)
            return frm, lms, gesture_name

        return frm, None, "NO HAND"

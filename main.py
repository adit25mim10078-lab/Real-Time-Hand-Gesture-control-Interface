# Adapted/maintained by Adit Patidar.
# Original project: https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface
# See README.md for attribution and project notes.

import cv2 
from vision_engine.Camera import C
from vision_engine.HandDetector import HD
from gesture_analyzer.FeatureExtractor import FE
from gesture_analyzer.GestureClassifier import GC
from data_viz.OverlayManager import OM

def main_run():
    try:
        cam = C()
        detector = HD()
        extractor = FE()
        classifier = GC()
        overlay = OM()
        

    except IOError as e:
        print(f"ERROR: {e}")
        return
    
    print("Starting AI Hand Gesture Control Interface - Adit Patidar")
    print("Press 'q' to exit.")
    
    while True:
        frm = cam.rd()
        if frm is None: break

        frm, lms, h_label = detector.find(frm)
        
        g_name = "NO HAND"
        
        if lms:
        
            h, w, c = frm.shape
            
            f_stat = extractor.extract(lms, h)
            
        
            g_name = classifier.classify(f_stat)
            
    
            display_name = f"{g_name} ({h_label})"
            overlay.draw(frm, lms, display_name)
        else:
            overlay.draw(frm, None, g_name)
            
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.rel()
    

    
    cv2.destroyAllWindows() 
    print("Simulation Ended. Resources Released.")

if __name__ == '__main__':
    main_run()
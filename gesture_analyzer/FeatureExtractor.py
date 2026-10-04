# Adapted/maintained by Adit Patidar.
# Original project: https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface
# See README.md for attribution and project notes.

class FE:
    def __init__(s):
        s.tips = [4, 8, 12, 16, 20] 
        s.knuck = [3, 6, 10, 14, 18] 


    def extract(s, lms, h):
        lms_pix = []
        for lm in lms.landmark:
            lms_pix.append(int(lm.y * h))
        
        fngr_stat = [] 
        
        


        if lms_pix[s.tips[0]] < lms_pix[s.knuck[0]]:
            fngr_stat.append(1) 
        else:
            fngr_stat.append(0) 
        for i in range(1, 5):
            if lms_pix[s.tips[i]] < lms_pix[s.knuck[i]]:
                fngr_stat.append(1) 
            else:
                fngr_stat.append(0) 


        return fngr_stat 
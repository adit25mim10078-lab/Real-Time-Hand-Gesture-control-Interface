# Adapted/maintained by Adit Patidar.
# Original project: https://github.com/KushagraCloud/-Real-Time-Hand-Gesture-Control-Interface
# See README.md for attribution and project notes.

class GC:
    def classify(s, fs):
        if fs is None or len(fs) != 5:

            return "NO HAND"
        

        thumb, index, middle, ring, pinky = fs
        
       
        if all(fs):
            return "OPEN HAND / HI"
        
        if not any(fs):


            return "FIST / STOP"
            

     
        if index == 1 and middle == 0 and ring == 0 and pinky == 0:
            return "INDEX POINT"
            
       
        if index == 1 and middle == 1 and ring == 0 and pinky == 0:
            return "PEACE / V"
            

        if index == 1 and middle == 1 and ring == 1 and pinky == 0:
            return "THREE FINGERS"
            
        
        if thumb == 1 and index == 0 and middle == 0 and ring == 0 and pinky == 0:
            return "THUMBS UP"
            
       

        if thumb == 0 and index == 0 and middle == 1 and ring == 1 and pinky == 1:
            
            return "OKAY (SIMPLE)"
        if thumb==0 and index==0 and middle==1 and ring==0 and pinky==0:
            return "FUCK OFF"
            
        return "OTHER GESTURE"

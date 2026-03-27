#webcam / video capture

import cv2

class VideoCapture:
    def __init__(self, source="teste.mp4"):
        """
        source = 0 -> webcam
        source = 1 -> video file

        """
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise ValueError("Could not open video source: {}".format(source))
        
    def get_frame(self):
        
        ret, frame = self.cap.read()

        if not ret:
            raise ValueError("Could not read frame from video source")
        
        return frame
    
    def release(self):
        """
        libera a camera
        """ 
        self.cap.release()
#ponto de entrada do programa

import cv2

from video.capture import VideoCapture
from pose.yolo_pose import YoloPose
from processing.key_points import KeyPointsExtractor
def main():

    #inicializa captura
    video_capture = VideoCapture(0) #0 para webcam, ou caminho para video file

    #inicializa modelo de pose
    yolo_pose = YoloPose()

    #inicializa extrator de key points
    key_points_extractor = KeyPointsExtractor()
    keypoints = None
    
    while True:
        
        #pega o frame da webcam / video
        frame = video_capture.get_frame()

        #joga o frame no modelo para fazer a deteção
        results = yolo_pose.detect(frame)

        #desenha o resultado no frame
        annotated_frame = yolo_pose.draw(frame, results)

        #extrai os key points dos resultados do modelo
        keypoints = key_points_extractor.extract(results)
        right_hand = key_points_extractor.get_right_hand(keypoints)

        if right_hand is not None:
            print(f"Right hand key point: {right_hand}")
            
        cv2.imshow("Pose Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    #libera a captura e fecha as janelas
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


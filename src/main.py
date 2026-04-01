#ponto de entrada do programa

import cv2

from video.capture import VideoCapture
from pose.yolo_pose import YoloPose
from processing.key_points import KeyPointsExtractor
from processing.motion import MotionAnalyzer
from detection.punch import PunchDetector
def main():

    #inicializa captura
    video_capture = VideoCapture(0) #0 para webcam, ou caminho para video file

    #inicializa modelo de pose
    yolo_pose = YoloPose()

    #inicializa extrator de key points
    key_points_extractor = KeyPointsExtractor()
    keypoints = None
    
    #inicializa analisador de movimento
    motion_analyzer = MotionAnalyzer()

    #inicializa detector de golpes
    punch_detector = PunchDetector()

    #contador de frames
    frame_count = 0
    #cont jabs
    cont_jabs = 0
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

        #analisa o movimento da mão direita
        movement = motion_analyzer.compute_movement(right_hand)

        #detecta jab
        is_jab = punch_detector.detect_jab(movement)

        
        if is_jab:
            cont_jabs += 1

        cv2.putText(
            annotated_frame,
            f"Jabs: {cont_jabs}",
            (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 0, 255),
            3
        )
        
        # if movement is not None:
        #     dx, dy = movement

        #     if frame_count % 5 == 0: #printa a cada 10 frames para não poluir o console
        #         print(f"Right hand movement: dx={dx}, dy={dy}")

        # if right_hand is not None:

        #      if frame_count % 10 == 0: #printa a cada 10 frames para não poluir o console
                # print(f"Right hand key point: {right_hand}")
            
        cv2.imshow("Pose Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        frame_count += 1
    #libera a captura e fecha as janelas
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


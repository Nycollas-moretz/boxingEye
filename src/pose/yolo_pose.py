#vai apenas rodar o modelo de pose, para que possamos ter as coordenadas dos pontos de cada boxeador, e para que possamos usar essas coordenadas para fazer a identificação dos golpes, e para que possamos usar essas coordenadas para fazer o desenho na tela, para que possamos vizualizar o que o modelo está vendo, e para mostrar as informações de cada boxeador

from ultralytics import YOLO

class YoloPose:
    def __init__(self, model_path="yolo11n-pose.pt"):
        """
        carrega o modelo YOLO
        """
        self.model = YOLO(model_path)

    def detect(self, frame):
        """
        roda inferencia no frame
        """
        results = self.model(frame)
    
        return results
    
    def draw(self, frame, results):
        """
        desenha o resultado (keypoints + skeleton)
        """
        annotated_frame = results[0].plot() #desenha os keypoints e o skeleton no frame

        return annotated_frame
    
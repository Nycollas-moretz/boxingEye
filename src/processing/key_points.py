#vai extrair os key points, para que possamos usar eles para identificar os golpes, e para mostrar na tela, para que possamos vizualizar o que o modelo está vendo, e para mostrar as informações de cada boxeador

class KeyPointsExtractor:

    def __init__(self):
        pass

    def extract(self, results):
        #aqui vamos extrair os key points dos resultados do modelo
        if results[0].keypoints is not None:
            return results[0].keypoints.xy
        else:
            return None
        
    def get_right_hand(self, keypoints):
        #aqui vamos pegar os key points da mao direita, para identificar golpes
        if keypoints is None or len(keypoints) == 0:
            return None
        
        return keypoints[0][10] #indice 10 é a mao direita, de acordo com a documentação do modelo
    
#vai analisar o movimento, para que possamos identificar os golpes, e para mostrar na tela, para que possamos vizualizar o que o modelo está vendo, e para mostrar as informações de cada boxeador

class MotionAnalyzer:
    def __init__(self):
        #vai guardar pos anterior
        self.prev_right_hand = None

    def compute_movement(self, current_right_hand):
        #calcula movimento da mao direita

        if current_right_hand is None:
            return None
        
        if self.prev_right_hand is None:
            #primeira execução, não tem movimento
            self.prev_right_hand = current_right_hand
            return None
        
        #calcula a diferença entre a posição atual e a anterior
        dx = current_right_hand[0] - self.prev_right_hand[0]
        dy = current_right_hand[1] - self.prev_right_hand[1]

        #atualiza a posição anterior
        self.prev_right_hand = current_right_hand

        return (dx, dy)
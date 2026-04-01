#Vai fazer a identificação, é um jab? Um direto? Um gancho? E vai mostrar a porcentagem de cada um, para que possamos ter uma ideia do que o modelo está vendo, e para que possamos melhorar o modelo, caso ele esteja errando muito em alguma categoria.

import time

class PunchDetector:
    def __init__(self, threshold=50, coldown_time=0.5):
        self.threshold = threshold
        self.coldown_time = coldown_time
        self.last_punch_time = 0
    def detect_jab(self, movement):

        if movement is None:
            return None
        
        dx, dy = movement
        current_time = time.time()


        if current_time - self.last_punch_time < self.coldown_time:
            return False
        
        if abs(dx) > self.threshold and abs(dy) < 30:
            self.last_punch_time = current_time
            return True
        
        return False
        

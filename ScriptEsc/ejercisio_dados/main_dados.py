
from random import randint

class Die:
    def __init__(self, num_lados = 6) -> None:
        self.lados = num_lados
        
    def roll(self):
        return randint(1, self.lados)
    
    

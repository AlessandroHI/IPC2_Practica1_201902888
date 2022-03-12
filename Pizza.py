from Cola import Cola

class Pizza(Cola):
    def __init__(self, noPizza, ingredients, tiempo1):
        self.noPizza = noPizza
        self.ingredients = ingredients
        self.tiempo1  = tiempo1
        super().__init__()
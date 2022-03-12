from Cola import Cola

class Orden(Cola):
    def __init__(self, Nombre, NIT, Pizzas, tiempo):
        self.Nombre = Nombre
        self.NIT = NIT
        self.Pizzas = Pizzas
        self.tiempo = tiempo
        super().__init__()
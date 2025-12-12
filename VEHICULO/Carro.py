class Carro:
    def __init__(self,modelo,color, n_puertas,capacidad_pasajeros):
        self.modelo = modelo
        self.color = color
        self.n_puertas = n_puertas
        self.capacidad_pasajeros

    def arrancar(self):
        print(f"{self.modelo}: motor encendido")
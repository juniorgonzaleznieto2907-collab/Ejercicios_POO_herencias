class Base_datos():
    def _inint_(self):
        self.lista_animales = []

    def agregar_animal(self, nuevo_animal):
        self.lista_animales.append(nuevo_animal) 

    def imprimi_lista_animal(self):
        for animal in self.lista_animales: 
             print(f"lista animales: {self.lista_animales}")
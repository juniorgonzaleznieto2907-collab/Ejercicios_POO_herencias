class Base_datos:
    def __init__(self):
        self.lista_botellas = []
    def agregar_botellas(self,botella):
        self.lista_botellas.append(botella)
    def extender_lista(self,botella):
        self.lista_botellas.extend(botella)
    def eliminar_objeto(self):
        if self.lista_botellas:
             self.lista_botellas.pop()
    def copiar_lista(self):
        self.lista_botellas.copy()
    def limpiar_lista(self):
        self.lista_botellas.clear()
    def invertir_lista(self):
        self.lista_botellas.reverse()
    def ordenar_lista(self):
        self.lista_botellas.sort()

    def imprimir_info(self):
        for i, botella in self.lista_botellas:
             print(f"capacidad: {self.capacidad}- forma: {self.forma} - diseño: {self.diseño} - tapa: {self.tapa}")

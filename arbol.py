class Nodo:
    def __init__(self, valor, id,costo):
        self.valor = valor
        self.id = id  # Atributo único
        self.costo = costo  # Costo asociado al nodo
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
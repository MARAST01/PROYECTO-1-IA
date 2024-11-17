class Nodo:
    def __init__(self, valor, id, costo, heuristica=1, padre=None):
        self.valor = valor
        self.id = id
        self.costo = costo
        self.heuristica = heuristica
        self.padre = padre
        self.hijos = []
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
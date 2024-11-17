class Nodo:
    def __init__(self, valor, id, costo, heuristica=1):
        self.valor = valor
        self.id = id  # Atributo único
        self.costo = costo  # Costo asociado al nodo
        self.heuristica = heuristica  # Heurística asociada al nodo (por defecto, 1)
        self.hijos = []  # Lista de hijos

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

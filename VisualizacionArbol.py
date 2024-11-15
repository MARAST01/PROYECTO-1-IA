import networkx as nx
import matplotlib.pyplot as plt
import time

class VisualizacionArbol:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.posiciones = {}
        self.nivel = {}
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.separacion_nivel = 2  # Separación vertical entre niveles
        self.espacio_hojas = 1.5  # Espacio horizontal entre nodos
        self.pos_x = 0  # Controla la posición horizontal de las hojas en el árbol
        self.nodo_id = {}  # Diccionario para manejar nodos repetidos

    def agregar_nodo(self, nodo, padre=None):
        # Generar un nuevo identificador para nodos repetidos
        nodo_real = nodo if nodo not in self.nodo_id else (nodo[0], nodo[1] + self.nodo_id[nodo])
        self.nodo_id[nodo] = self.nodo_id.get(nodo, 0) + 1  # Incrementar el conteo para el nodo

        # Añadir el nodo al grafo
        self.grafo.add_node(nodo_real)

        if padre is not None:
            self.grafo.add_edge(padre, nodo_real)
            self.nivel[nodo_real] = self.nivel[padre] + 1
        else:
            self.nivel[nodo_real] = 0  # Nodo raíz

        # Calcular la posición del nodo en el árbol
        self._calcular_posiciones(nodo_real)

        # Redibujar el gráfico
        self._dibujar_grafico()
        time.sleep(0.5)  # Pausa para visualizar cada paso

    def _calcular_posiciones(self, nodo):
        # Verificar si la posición del nodo ya fue calculada
        if nodo in self.posiciones:
            return

        hijos = list(self.grafo.successors(nodo))
        
        if not hijos:  # Si el nodo no tiene hijos, es una hoja
            self.posiciones[nodo] = (self.pos_x, -self.nivel[nodo] * self.separacion_nivel)
            self.pos_x += self.espacio_hojas  # Incrementar para la siguiente hoja
        else:
            # Calcular posiciones para los hijos primero (recursivamente)
            for hijo in hijos:
                self._calcular_posiciones(hijo)

            # Calcular la posición del nodo padre centrado entre sus hijos
            x_min = self.posiciones[hijos[0]][0]
            x_max = self.posiciones[hijos[-1]][0]
            self.posiciones[nodo] = ((x_min + x_max) / 2, -self.nivel[nodo] * self.separacion_nivel)

    def _dibujar_grafico(self):
        self.ax.clear()
        nx.draw(self.grafo, pos=self.posiciones, with_labels=True, node_color='lightblue', ax=self.ax,
                font_weight='bold', arrows=True)
        plt.draw()
        plt.pause(0.001)  # Actualiza la visualización en tiempo real

    def finalizar(self):
        plt.show()

# Prueba del árbol con nodos repetidos (mismos nodos como padres e hijos)
visualizador = VisualizacionArbol()
visualizador.agregar_nodo((0, 2))  # Nodo raíz
visualizador.agregar_nodo((0, 1), (0, 2))  # Primer hijo
visualizador.agregar_nodo((0, 3), (0, 2))  # Segundo hijo
visualizador.agregar_nodo((1, 3), (0, 1))  # Hijo del nodo (0, 1)
visualizador.agregar_nodo((1, 0), (0, 3))  # Hijo del nodo (0, 3)
visualizador.agregar_nodo((2, 3), (0, 3))  # Hijo del nodo (0, 3)
visualizador.agregar_nodo((2, 0), (1, 0))  # Hijo del nodo (1, 0)
visualizador.agregar_nodo((2, 2), (1, 0))  # Hijo del nodo (1, 0)
visualizador.agregar_nodo((3, 0), (2, 2))  # Hijo del nodo (2, 2)
visualizador.agregar_nodo((1, 3), (2, 3))  # Repetición del nodo (1, 3) como hijo de (0, 1)
visualizador.agregar_nodo((3, 2), (2, 2))  # Hijo repetido del nodo (2, 2)
visualizador.agregar_nodo((3, 1), (2, 0))  # Hijo del nodo (2, 0)
visualizador.agregar_nodo((1, 3), (2, 3))  # Repetición del nodo (1, 3) como hijo del nodo (2, 3)

visualizador.finalizar()
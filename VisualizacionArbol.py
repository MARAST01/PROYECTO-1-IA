import networkx as nx
import matplotlib.pyplot as plt
import time

class visualizacionArbol:
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.posiciones = {}
        self.nivel = {}
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        self.separacion_nivel = 2  # Separación vertical entre niveles
        self.pos_x = 0  # Controla la posición horizontal en el árbol

    def agregar_nodo(self, nodo, padre=None):
        # Añadir el nodo al grafo
        self.grafo.add_node(nodo)
        
        if padre is not None:
            self.grafo.add_edge(padre, nodo)
            self.nivel[nodo] = self.nivel[padre] + 1
        else:
            self.nivel[nodo] = 0  # Nodo raíz

        # Calcular la posición del nodo en el árbol
        self._calcular_posiciones(nodo)

        # Redibujamos el gráfico
        self._dibujar_grafico()
        time.sleep(0.5)  # Pausa para visualizar cada paso

    def _calcular_posiciones(self, nodo):
        # Verificar si la posición del nodo ya fue calculada
        if nodo in self.posiciones:
            return

        hijos = list(self.grafo.successors(nodo))
        if not hijos:  # Si el nodo no tiene hijos, es una hoja
            self.posiciones[nodo] = (self.pos_x, -self.nivel[nodo] * self.separacion_nivel)
            self.pos_x += 2  # Incrementar para la siguiente hoja
        else:
            # Calcular posiciones para los hijos primero (recursivamente)
            for hijo in hijos:
                self._calcular_posiciones(hijo)

            # Promediar las posiciones de los hijos para la posición del nodo actual
            x_hijos = [self.posiciones[hijo][0] for hijo in hijos]
            x_promedio = sum(x_hijos) / len(hijos)
            self.posiciones[nodo] = (x_promedio, -self.nivel[nodo] * self.separacion_nivel)

    def _dibujar_grafico(self):
        self.ax.clear()
        nx.draw(self.grafo, pos=self.posiciones, with_labels=True, node_color='lightblue', ax=self.ax, font_weight='bold', arrows=True)
        plt.draw()
        plt.pause(0.001)  # Actualiza la visualización en tiempo real

    def finalizar(self):
        plt.show()

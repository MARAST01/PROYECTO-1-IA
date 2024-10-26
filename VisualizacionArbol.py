import networkx as nx
import matplotlib.pyplot as plt
import time

class visualizacionArbol:
    def __init__(self):
        # Inicializamos el grafo y el dibujo
        self.grafo = nx.DiGraph()
        self.posiciones = {}
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        
    def agregar_nodo(self, nodo, padre=None):
        # Agrega un nodo y, si existe, una conexión al padre
        self.grafo.add_node(nodo)
        if padre:
            self.grafo.add_edge(padre, nodo)
        
        # Definimos posiciones para cada nodo para mantener la jerarquía
        self.posiciones = nx.spring_layout(self.grafo)
        
        # Dibujamos la gráfica actualizada
        self._dibujar_grafico()
        time.sleep(0.5)  # Pausa para visualizar el paso a paso

    def _dibujar_grafico(self):
        # Limpiamos el gráfico para redibujar
        self.ax.clear()
        # Dibujamos el grafo con las posiciones especificadas
        nx.draw(self.grafo, pos=self.posiciones, with_labels=True, node_color='lightblue', ax=self.ax, font_weight='bold')
        plt.draw()
        plt.pause(0.001)  # Actualiza la visualización en tiempo real

    def finalizar(self):
        # Muestra la gráfica final
        plt.show()

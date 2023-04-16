# Areli Sarai García Medina | 20310380

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1, 2, {'peso': 2}), (1, 3, {'peso': 4}), (1, 4, {'peso': 1}),
                  (2, 3, {'peso': 3}), (2, 4, {'peso': 2}), (2, 5, {'peso': 3}),
                  (3, 5, {'peso': 5}), (4, 5, {'peso': 4})])

pos = nx.spring_layout(G)
nx.draw(G, pos)
etiquetas_aristas = nx.get_edge_attributes(G,'peso')
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas)
plt.show()

arbol_par_minimo = nx.minimum_spanning_tree(G)
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edges(arbol_par_minimo, pos, edge_color='r', width=2)
nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_aristas)
plt.show()
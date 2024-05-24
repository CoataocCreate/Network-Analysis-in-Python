import networkx as nx
import matplotlib.pyplot as plt

# Create a simple graph
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

# Visualize the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=15)
plt.title("Simple Network Graph")
plt.show()

# Calculate network metrics
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Average clustering coefficient:", nx.average_clustering(G))
print("Average shortest path length:", nx.average_shortest_path_length(G))

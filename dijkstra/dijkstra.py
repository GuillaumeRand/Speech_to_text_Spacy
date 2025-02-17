import sys
import pandas as pd

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]




# The function takes two arguments: graph and start_node. graph is an instance of the Graph class that we created in the previous step, 
# whereas start_node is the node from which we’ll start the calculations. 
def dijkstra_algorithm(graph, start_node):
    # We’ll call the get_nodes() method to initialize the list of unvisited nodes:
    unvisited_nodes = list(graph.get_nodes())
    # shortest_path will store the best-known cost of visiting each city in the graph starting from the start_node
    shortest_path = {}
    # previous_nodes will store the trajectory of the current best known path for each node.
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    # Add the start node manually
    path.append(start_node)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    

# get all depart from csv
def get_all_locations():
    locations = []
    df = pd.read_csv('D:\\Users\\Documents\\Dev\\Python\\T-AIA-901-MPL_7\\dijkstra\\clearData.csv')
    for index, row in df.iterrows():
        locations.append(str(row['depart']).upper())
        if row['destination'] not in locations:
            locations.append(str(row['destination']).upper())
    return locations


def get_2_random_locations():
    df = pd.read_csv('clearData.csv')
    depart = df['depart'].sample().iloc[0]
    destination = df['destination'].sample().iloc[0]
    return depart, destination
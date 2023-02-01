"""
This script allows for the creation of two dictionaries that form a graph

A graph is made out of 2 dictionaries 

one to hold the possible edges (keys) with their corresonding distances (values), 

the second holds all possible edges from every start node (keys) to every neighbouring node (values)
Note: different use of edge and edges

"""

import re

class GraphCreator():
    
    def __init__(self, name):
        self.name = name
        self.edge_distances = dict()
        self.edges = dict()


    def add_edge(self, edge):
        
        # checks if the edge input is in the correct format
        if re.match(r'^[A-E]{2}[0-9]$', edge):
            
            # if check is passed : creates variables to store the edge name and distance
            edge_distances_key = edge[:2]
            edge_distances_value = int(edge[2])
            
            # checks if the start node of the edge is already known in the edges dictionary, if not adds it and the corresponding edge
            if edge[0] not in self.edges:
                self.edges[edge[0]] = [edge[1]]
            
            # if the start node is already known, adds the new edge
            else:
                self.edges[edge[0]].append(edge[1])
            
            # adds the input to the edge_distances dictionary
            self.edge_distances[edge_distances_key] = edge_distances_value
            
        else:
            print("Error: Invalid input, please enter in the form of two capital letters A-E followed by an integer 0-9")
            
    def get_edges_dict(self):
        # function to get the edges dictionary of the graph
        return self.edges
    
    def get_edge_distances_dict(self):
        # function to get the edge_distances dictionary of the graph
        return self.edge_distances
    
    def __str__(self):
        # this function determines what happens when the object is printed
        return f"Graph: {self.name}\n This graph has the following edges : {self.edges}\n and the following edge distances : {self.edge_distances}"
    
    
    
    
    
    
    
    
    
    
    
    
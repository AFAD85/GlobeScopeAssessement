import re
import unittest


class RouteFinder():
    
    def __init__(self, name):
        self.name = name
        
        # creates 2 dictionaries one to hold the possible edges (keys) with their corresonding distances (values), 
        # the second holds all possible edges from every start node (keys) to every neighbouring node (values)
        # Note: different use of edge and edges
        self.edge_distances = dict()
        self.edges = dict()
        
        
    def add_edge(self, edge):
        
        # checks if the edge input is in the correct format
        if re.match(r'^[A-E]{2}[0-9]$', edge):
            
            # creates variables to store the edge name and distance
            self.edge_distances_key = str()
            self.edge_distances_value = 0
            
            # adds the node letters to the edge distances dictionary as key, and the distance as value
            for character in edge:

                digits = '0123456789'
                
                # finds the digits in the edge string and adds them to the value variable
                if character in digits:
                    self.edge_distances_value += int(character)
                    
                else:
                    self.edge_distances_key += character
                    
                    
            # checks if the start node is already in the edges dictionary, if not it adds it as a key with the end node as a value 
            if not edge[0] in self.edges.keys():
                
                self.edges_key = edge[0]
                self.edges_value = [edge[1]]
                self.edges.update({self.edges_key : self.edges_value})
            
            else:
                self.edges[edge[0][0]].append(edge[1])
            

                    
            self.edge_distances.update({self.edge_distances_key : self.edge_distances_value})

        else:
            print("Error: Invalid input, please enter in the form of two capital letters A-E followed by an integer 0-9")
        
        
    def get_route_distance(self, nodes):
        distance = 0
        
        # splits the nodes string into pairs of 2 
        node_pairs = [nodes[i:i+2] for i in range(0, (len(nodes)-1), 1)]
        
        # gets the distance of each pair of towns from the routes dictionary and adds these to the distance variable
        for town_pair in node_pairs:
            if town_pair in self.edge_distances:
                sub_distance = self.edge_distances.get(town_pair)
                distance += sub_distance
            else:
                print("NO SUCH ROUTE")
        return distance
            
        
    def get_possible_routes(self, Town1, Town2, max_stops=None, exact_stops=None, max_distance=None):
        
        # finds all possible routes between two towns, optionally with a maximum number of stops, exact number of stops, or maximum distance
        self.start = Town1
        self.end = Town2
        self.max_stops = max_stops
        self.exact_stops = exact_stops
        self.max_distance = max_distance
        
        # User should define either max_stops, exact_stops or max_distance
        if not (max_stops or exact_stops or max_distance):
            return ValueError("Missing arguements, please define exactly one of max_stops, exact_stops or max_distance")
        
        # Counter to check how many arguements have been defined
        args_count = 0
        
        # Check if max_stops is defined
        if max_stops != None:
            args_count += 1
        
        # Check if exact_stops is defined
        if exact_stops != None:
            args_count += 1
            
        # Check if max_distance is defined
        if max_distance != None:
            args_count += 1

        # If more than one arguement is defined, raise an error
        if args_count > 1:
            return ValueError("Too many arguements, please define exactly one of max_stops, exact_stops or max_distance")

        # If max_stops is defined, call the _find_routes function with the max_stops arguement
        if max_stops:
            possible_routes = self._find_routes(self.edges, self.start, self.end, max_stops=max_stops)
            return possible_routes
        
        # If exact_stops is defined, call the _find_routes functions with the max_stops arguement, 
        # and after running removes the routes that do not meet the exact stops requirement
        if exact_stops:
            possible_routes = self._find_routes(self.edges, self.start, self.end, max_stops=exact_stops)
            
            # checks if the route lenght is equal to the exact_stops arguement, if not removes it from the list
            for route in possible_routes:
                if len(route) != exact_stops:
                    possible_routes.remove(route)
                    
            return possible_routes
        
        # If max_distance is defined, call the _find_routes function with the max_distance arguement
        if max_distance:
            possible_routes = self._find_routes(self.edges, self.start, self.end, max_distance=max_distance)
            return possible_routes
        
        
    def _find_routes(self, graph, start, end, routes=None, max_stops=None, max_distance=None):
    
    

        # initializes the routes list if it isn't already made
        if routes is None:
            routes = []
        
        # checks to see if the start is a node in the graph
        if not start in graph:
            return ValueError("Start town not in routefinder")
        
        route = []
        if max_stops:
            # if max stop is set, calls the recursive_find function, which will find all the routes, that adhere to the max stops
            self._recursive_find(graph, start, end, route, routes, 0, max_stops)
            return routes
        
        if max_distance:
            # if max distance is set calls the recursive_find_distance function, which will find all the routes, that adhere to the max distance
            self._recursive_find_distance(graph, start, end, route, routes, 0, max_distance)
            
            new_routes = []
            for i in range(len(routes)):
                if routes[i] not in new_routes:
                    new_routes.append(routes[i])
                    
            return new_routes

        return routes


    def _recursive_find(self, graph, start, end, route, routes, visited, max_stops):
        
        # initializes the new_route list by copying the route list used to call the function
        new_route = route.copy()
        new_route.append(start)
        
        # checks to see if the route is complete, if so adds the new route to the list of routes    
        if start == end and visited > 0:
            routes.append(new_route)
        
        # checks to see if the max number of visits has been reached, if so ends the function call    
        if visited == max_stops:
            return
        
        # keeps track of the number of nodes visited, and feed that number into the next recursive call
        current_visited = visited+1

        # loops through all the nodes connected to the start node, and calls the recursive function on each of them
        for i in range (len(graph[start])):
            self._recursive_find(graph, graph[start][i], end, new_route , routes, current_visited, max_stops)
        return routes


    def _recursive_find_distance(self, graph, start, end, route, routes, distance_travelled, max_distance):
        
        # checks to see if the max number of visits has been reached, if so ends the function call    
        if distance_travelled >= max_distance:
            return
        
        # initializes the new_route list by copying the route list used to call the function
        new_route = route.copy()
        new_route.append(start)
        
        # checks to see if the route is complete, if so adds the new route to the list of routes    
        if start == end and distance_travelled > 0:
            routes.append(new_route)
        

        

        # loops through all the nodes connected to the start node, and calls the recursive function on each of them
        for i in range (len(graph[start])):
            # keeps track of the number of nodes visited, and feed that number into the next recursive call
            current_distance = distance_travelled + self.get_route_distance(start+graph[start][i])
            print(f"{new_route},{current_distance}")
            
            self._recursive_find_distance(graph, graph[start][i], end, new_route , routes, current_distance, max_distance)
            
        return routes


    def get_shortest_route(self, Town1, Town2):
        # first finds all routes between the two towns(nodes) with the max amount of stops set to the number of nodes in the graph
        # then finds the shortest route by comparing the distances of each route
        all_routes = self.get_possible_routes(Town1, Town2, max_stops=len(self.edges))
        route_distances = []
        
        for route in all_routes:
            route_string = ""
            for nodes in route:
                route_string += nodes
            route_distances.append(self.get_route_distance(route_string))
        

        shortest_distance = route_distances[0]
        for distance in route_distances:
            if distance < shortest_distance:
                shortest_distance = distance
        
        shortest_route = all_routes[route_distances.index(shortest_distance)]
        
        return shortest_route, shortest_distance
        
        
        
                
                
        
        
        

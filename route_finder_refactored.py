import re


class RouteFinder():

 
    def __init__(self, name, graph):
        self.name = name
        self.graph = graph

        
    def get_route_distance(self, nodes):
        
        distance = 0
        
        # splits the nodes string into pairs of 2 
        node_pairs = [nodes[i:i+2] for i in range(0, (len(nodes)-1), 1)]
        
        # gets the distance of each pair of towns from the routes dictionary and adds these to the distance variable
        for town_pair in node_pairs:
            if town_pair in self.graph.edge_distances:
                sub_distance = self.graph.edge_distances.get(town_pair)
                distance += sub_distance
            else:
                return "NO SUCH ROUTE"
            
        return distance
            
        
    def get_possible_routes(self, Town1, Town2, max_stops=None, exact_stops=None, max_distance=None):
        
        # finds all possible routes between two towns, optionally with a maximum number of stops, exact number of stops, or maximum distance
        start = Town1
        end = Town2
        max_stops = max_stops
        exact_stops = exact_stops
        max_distance = max_distance
        
        # User should define either max_stops, exact_stops or max_distance
        # if none are defined or too many are defined an error is raised
        args_count = sum(1 for arg in [max_stops, exact_stops, max_distance] if arg is not None)
        if args_count != 1:
            return "Error : Please define exactly one of max_stops, exact_stops, or max_distance"
        

        # If max_stops is defined, call the _find_routes function with the max_stops arguement
        if max_stops:
            possible_routes = self._find_routes(self.graph.edges, start, end, max_stops=max_stops)
            return possible_routes
        
        # If exact_stops is defined, call the _find_routes functions with the max_stops arguement, 
        # and after running removes the routes that do not meet the exact stops requirement
        if exact_stops:
            possible_routes = self._find_routes(self.graph.edges, start, end, max_stops=exact_stops)
            
            # checks if the route lenght is equal to the exact_stops arguement, if not removes it from the list
            for route in possible_routes:
                if len(route) != exact_stops:
                    possible_routes.remove(route)
                    
            return possible_routes
        
        # If max_distance is defined, call the _find_routes function with the max_distance arguement
        if max_distance:
            possible_routes = self._find_routes(self.graph.edges, start, end, max_distance=max_distance)
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
            
            # ensures that no duplicate routes are stored in the list
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
            # calls the recursive function on the next node
            self._recursive_find_distance(graph, graph[start][i], end, new_route , routes, current_distance, max_distance)
            
        return routes


    def get_shortest_route(self, Town1, Town2):
        # first finds all routes between the two towns(nodes) with the max amount of stops set to the number of nodes in the graph
        # then finds the shortest route by comparing the distances of each route
        all_routes = self.get_possible_routes(Town1, Town2, max_stops=len(self.graph.edges))
        route_distances = []
        
        # loops through all the routes and finds the distance of each route
        for route in all_routes:
            route_string = ""
            for nodes in route:
                route_string += nodes
            route_distances.append(self.get_route_distance(route_string))
        
        # finds the shortest distance and returns that distance
        shortest_distance = route_distances[0]
        for distance in route_distances:
            if distance < shortest_distance:
                shortest_distance = distance
        
        # shortest_route = all_routes[route_distances.index(shortest_distance)]
        
        return shortest_distance
        
        
        
                
                
        
        
        

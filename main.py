

"""
Instructions for use are found in the README.txt file
"""

from route_finder import RouteFinder
from graph_creator import GraphCreator


def main():
    
    # initialize your graph here (name goes in parentheses)
    graph = GraphCreator("graph")
    
    # initialize the route finder here (name goes in parentheses, followed by the object you created above)
    route_finder = RouteFinder("routefinder", graph)
    
    # adds the edges in the form of two capital letters A-E followed by an integer 0-9 on the spots of XX0    
    # the leters represent the start and end node, the number represents the distance between them
    graph.add_edge("XX0")
    
    # this function will allow you to get the distance of a route, this can be any route as long as it is connected as you specify. 
    # enter a string in the form of two capital letters A-E on the spots of XX, longer strings will also work
    route_finder.get_route_distance("XX")
    
    # this function will allow you to get the number of possible routes between two nodes, you have to specify one of the following : max_stops, exact_stops, max_distance    
    route_finder.get_possible_routes("XX", max_stops=None, exact_stops=None, max_distance=None)
    
    # this function will allow you to get the shortest route between two nodes call the function with two strings in parentheses
    route_finder.get_shortest_route("X","X")






if __name__ == "__main__":
    main()
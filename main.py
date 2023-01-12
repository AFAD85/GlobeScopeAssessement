from route_finder import RouteFinder

"""
Instructions for use are found in the README.txt file
"""
def main():
    
    route_finder = RouteFinder()
    
    route_finder.add_edge("XX0")
    
    route_finder.get_route_distance("XX")
    
    route_finder.get_possible_routes("XX", max_stops=None, exact_stops=None, max_distance=None)
    
    route_finder.get_shortest_route("X","X")






if __name__ == "__main__":
    main()
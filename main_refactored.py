from route_finder_refactored import RouteFinder
from graph_creator import GraphCreator



"""
Instructions for use are found in the README.txt file
"""
def main():

    graph = GraphCreator()
    
    # initialize the route finder
    route_finder = RouteFinder("route_finder", graph)
    
    # adds the edges
    route_finder.add_edge("AB5")
    route_finder.add_edge("BC4")         
    route_finder.add_edge("CD8")     
    route_finder.add_edge("DC8")      
    route_finder.add_edge("DE6")      
    route_finder.add_edge("AD5")      
    route_finder.add_edge("CE2")      
    route_finder.add_edge("EB3")      
    route_finder.add_edge("AE7")

    # runs the routefinder with specified input (from requirements)
    input_1 = route_finder.get_route_distance("ABC")

    input_2 = route_finder.get_route_distance("AD")

    input_3 = route_finder.get_route_distance("ADC")

    input_4 = route_finder.get_route_distance("AEBCD")

    input_5 = route_finder.get_route_distance("AED")

    input_6 = len(route_finder.get_possible_routes("C", "C", max_stops=3))

    input_7 = len(route_finder.get_possible_routes("A", "C", exact_stops=4))

    input_8 = route_finder.get_shortest_route("A", "C")

    input_9 = route_finder.get_shortest_route("B", "B") 

    input_10 = len(route_finder.get_possible_routes("C", "C", max_distance=30))

    print(f"Route finder completed requests.\n\n Output #1 :{input_1}\n Output #2 : {input_2}\n Output #3 : {input_3}\n Output #4 : {input_4}\n Output #5 : {input_5}\n Output #6 : {input_6}\n Output #7 : {input_7}\n Output #8 : {input_8}\n Output #9 : {input_9} \n Output #10 : {input_10}\n\n",route_finder)




if __name__ == "__main__":
    main()
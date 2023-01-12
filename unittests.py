from route_finder import RouteFinder

def main():
    # initialize the test route finder object
    test_route_finder = RouteFinder()

def setup_test_route_finder():

    # keeps track of error count
    errors = 0
    
    # adds the edges, that will not be tested to the test route finder object for use in further tests
    test_route_finder.add_edge("BC4")         
    test_route_finder.add_edge("CD8")     
    test_route_finder.add_edge("DC8")      
    test_route_finder.add_edge("DE6")      
    test_route_finder.add_edge("AD5")      
    test_route_finder.add_edge("CE2")      
    test_route_finder.add_edge("EB3")      
    test_route_finder.add_edge("AE7")

def test_add_edge_valid_input():
    
    # inputs edge AB with distance 5 into the test object
    test_route_finder.add_edge("AB5")
    
    # checks if edge AB is entered into the edges dictionary
    if not test_route_finder.edges["AB"]:
        print("Error : The edge AB5 was not correctly added to the edges dictionary")
        errors += 1
        
    # tests if the edge AB and corresponding distance 5 is correctly entered into the edge_distances dictionary
    if test_route_finder.edge_distances["AB"] != 5:
        print("Error : The edge AB5 was not correctly added to the edge_distances dictionary")
        errors += 1
        
def test_get_route_distance_valid_input():
    # this function tests the get_route_distance function and stores the results of the function calls for use in program validation
            
    # tests wether the distance of route ABC is correctly computed and stores it in variable solution_1
    solution_1 = test_route_finder.get_route_distance("ABC")
    if solution_1 != 9:
        print( "Error : The distance of the route ABC is not correct")
        errors += 1
        
    # tests wether the distance of route AD is correctly computed and stores it in variable solution_2
    solution_2 = test_route_finder.get_route_distance("AD")
    if solution_2 != 5:
        print("Error : The distance of the route AD is not correct")
        errors += 1
        
    # tests wether the distance of route ADC is correctly computed and stores it in variable solution_3
    solution_3 = test_route_finder.get_route_distance("ADC")
    if solution_3 != 13:
        print("Error : The distance of the route ADC is not correct")
        errors += 1
        
    # tests wether the distance of route AEBCD is correctly computed and stores it in variable solution_4
    solution_4 = test_route_finder.get_route_distance("AEBCD")
    if solution_4 != 22:
        print("Error : The distance of the route AEBCD is not correct")
        errors += 1
    
def test_get_route_distance_invalid_input():
    # this function tests the get_route_distance function with invalid input and stores the results of the function call for use in program validation

    # tests wether the distance of route AEBCD is correctly computed and stores it in variable solution_4
    solution_5 = test_route_finder.get_route_distance("AED")
    if solution_5 != "NO SUCH ROUTE":
        print("Error : The distance of the route AED is not correct")
        
def test_get_possible_routes_max_stops():
    # this function tests the get_possible routes function with max_stops defined and stores the results of the function call for use in program validation

    solution_6 = len(test_route_finder.get_possible_routes("C", "C", max_stops=3))
    if solution_6 != 2:
        print("Error : The routes between nodes C and C given 3 maximum stops have not been found correctly")

def test_get_possible_routes_max_stops():
    # this function tests the get_possible routes function with max_stops defined and stores the results of the function call for use in program validation
    solution_7 = len(test_route_finder.get_possible_routes("A", "C", exact_stops=4))
    if solution_7 !=2:
        print("Error : The routes between nodes A and C given exactly 4 stops have not been found correctly")
    
def test_get_shortest_route(self):
solution_8 = test_routefinder.get_shortest_route("A", "C")
solution_9 = test_routefinder.get_shortest_route("B", "B")
solution_10 = len(test_routefinder.get_possible_routes("C", "C", max_distance=30))
print(f"Output #1 :{solution_1}\n Output #2 : {solution_2}\n Output #3 : {solution_3}\n Output #4 : {solution_4}\n Output #5 : {solution_5}\n Output #6 : {solution_6}\n Output #7 : {solution_7}\n Output #8 : {solution_8}\n Output #9 : {solution_9} \n Output #10 : {solution_10}")




        # print(test_route_finder.edges)
        # print(test_route_finder.edge_distances)







# AC_routes = test_routefinder.get_possible_routes("A", "C", max_stops=4)
# print(AC_routes)


"""
1. The distance of the route A-B-C.
2. The distance of the route A-D.
3. The distance of the route A-D-C.
4. The distance of the route A-E-B-C-D.
5. The distance of the route A-E-D.
6. The number of trips starting at C and ending at C with a maximum of 3 stops. In the sample
data below, there are two such trips: C-D-C (2 stops). and C-E-B-C (3 stops).
7. The number of trips starting at A and ending at C with exactly 4 stops. In the sample data
below, there are three such trips: A to C (via B,C,D); A to C (via D,C,D); and A to C (via
D,E,B).
8. The length of the shortest route (in terms of distance to travel) from A to C.
9. The length of the shortest route (in terms of distance to travel) from B to B.
10. The number of different routes from C to C with a distance of less than 30. In the sample data,
the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.

Output #1: 9
Output #2: 5
Output #3: 13
Output #4: 22
Output #5: NO SUCH ROUTE
Output #6: 2
Output #7: 3
Output #8: 9
Output #9: 9
Output #10: 7

"""





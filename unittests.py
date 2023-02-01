
"""
This program tests the RouteFinder class and its functions on the use case as presented in the assessment description

First it initializes the RouteFinder object and then adds the edges AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7 to the object

The program then runs a test where it determines if using the add_edge function works properly by adding AB5 to the object,
and checks if the edge AB is in the edges dictionary, and if the edge and distance are stored in the edge_distances dictionary of the edge AB is 5
these 2 tests are not numbered or stored as they are not required for the validation of the program given the assignment. 
They will however return an error message should the test fail.

The program then runs test 1 through 10 which are designed to also store the required output as per the assignment description.

Test 1 through 4 test the get_route_distance function with valid input,

Test 5 tests the get_route_distance function with invalid input.

Test 6 tests the get_possible_routes function with max_stops defined.

Test 7 tests the get_possible_routes function with exact_stops defined.

Test 8 tests the get_shortest_route function with valid input.

Test 9 tests the get_shortest_route function with invalid input.

Test 10 tests the get_possible_routes function with max_distance defined.

Finally the program checks wether or not all tests were completed succesfully, and if so prints out the output and the test objects contents.



For quick reference here is the assignment description:
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

from route_finder import RouteFinder


def main():

    # initialize the route finder test object
    test_route_finder = RouteFinder("test_route_finder")
    print("Running tests on RouteFinder class\n")
    
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

    
    # inputs edge AB with distance 5 into the test object
    test_route_finder.add_edge("AB5")
    
    # checks if edge AB is entered into the edges dictionary
    if not "AB" in test_route_finder.edge_distances:
        print("Error : The edge AB5 was not correctly added to the edges dictionary")
        errors += 1
        
    # tests if the edge AB and corresponding distance 5 is correctly entered into the edge_distances dictionary
    if test_route_finder.edge_distances["AB"] != 5:
        print("Error : The edge AB5 was not correctly added to the edge_distances dictionary")
        errors += 1

    # tests 1 through 4 test the distance finder with valid input

    # tests wether the distance of route ABC is correctly computed and stores it in variable test_1
    test_1 = test_route_finder.get_route_distance("ABC")
    if test_1 != 9:
        print( "Error : The distance of the route ABC is not correct")
        errors += 1
        
    # tests wether the distance of route AD is correctly computed and stores it in variable test_2
    test_2 = test_route_finder.get_route_distance("AD")
    if test_2 != 5:
        print("Error : The distance of the route AD is not correct")
        errors += 1
        
    # tests wether the distance of route ADC is correctly computed and stores it in variable test_3
    test_3 = test_route_finder.get_route_distance("ADC")
    if test_3 != 13:
        print("Error : The distance of the route ADC is not correct")
        errors += 1
        
    # tests wether the distance of route AEBCD is correctly computed and stores it in variable test_4
    test_4 = test_route_finder.get_route_distance("AEBCD")
    if test_4 != 22:
        print("Error : The distance of the route AEBCD is not correct")
        errors += 1
    

    # test 5 tests the get_route_distance function with invalid input and stores the results of the function call for use in program validation
    test_5 = test_route_finder.get_route_distance("AED")
    if test_5 != "NO SUCH ROUTE":
        print("Error : The distance of the route AED is not correct")
        errors += 1
        

    # test 6 tests the get_possible routes function with max_stops defined and stores the results of the function call for use in program validation
    test_6 = len(test_route_finder.get_possible_routes("C", "C", max_stops=3))
    if test_6 != 2:
        print("Error : The routes between nodes C and C given 3 maximum stops have not been found correctly")
        errors += 1

    # test 7 tests the get_possible routes function with max_stops defined and stores the results of the function call for use in program validation
    test_7 = len(test_route_finder.get_possible_routes("A", "C", exact_stops=4))
    if test_7 !=3:
        print("Error : The routes between nodes A and C given exactly 4 stops have not been found correctly")
        errors += 1    


    # tests 8 and 9 test the get_shortest_route function with valid input and stores the results of the function call for use in program validation
    test_8 = test_route_finder.get_shortest_route("A", "C")
    if test_8 != 9:
        print("Error : The shortest route between nodes A and C has not been found correctly")
        errors += 1
            
    test_9 = test_route_finder.get_shortest_route("B", "B")
    if test_9 != 9:
        print("Error : The shortest route between nodes B and B has not been found correctly")
        errors += 1
          
                
    # test 10 tests the get_possible routes function with max_distance defined and stores the results of the function call for use in program validation
    test_10 = len(test_route_finder.get_possible_routes("C", "C", max_distance=30))
    if test_10 != 7:
        print("Error : The number of routes between nodes C and C given a maximum distance of 30 have not been found correctly")
        errors += 1

    # Checks wether or not any errors were found, if not, prints the output gathered with the testing
    if errors == 0:
        print(f"All tests completed succesfully.\n\n Output #1 :{test_1}\n Output #2 : {test_2}\n Output #3 : {test_3}\n Output #4 : {test_4}\n Output #5 : {test_5}\n Output #6 : {test_6}\n Output #7 : {test_7}\n Output #8 : {test_8}\n Output #9 : {test_9} \n Output #10 : {test_10}\n\n",test_route_finder)

    else:
        print(f"Tests completed with {errors} errors")





if __name__ == "__main__":
    main()

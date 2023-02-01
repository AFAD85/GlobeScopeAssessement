

Requirements:
The program was tested on python version 3.9 however it should work on any 3.x version.

Testing:
In order to test the program, run main_refactored.py by double clicking it or running it manualy from your terminal. 
This will run the input as specified and compute and print the required output


Usage:
As per the assignment: 
run main_refactored.py
this will run the code as specified in the assignment



In order to use the program outside the scope of the assignment. Follow these steps:

-   Edit the main.py file in the same directory as route_finder.py
-   These instructions can also be found inside the file


-   Initialize your graph : {graphcreator_object_variable_name} = GraphCreator("object_name")
-   Input desired edges : {graphcreator_object_variable_name}.add_edge("XX0") where XX are two capital letters from A-E and 0 is the desired edge weight


-   Initialize your routefinder : {routefinder_object_variable_name} = RouteFinder("object_name")


-   To check to see if the input went through simply print({object_variable_name})
-   After adding the edges the following functions can be used :
    -   get_route_distance("XX")
    -   get_possible_routes("X","X", max_stops=None, exact_stops=None, max_distance=None) 
        Note : define exactly one of the 3 arguements (max_stops or exact_stops or max_distance)
    -   get_shortest_route("X","X")


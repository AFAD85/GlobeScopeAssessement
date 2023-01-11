

def find_routes(graph, start, end, routes=None, max_visit=3):

    if routes is None:
        routes = []
        

    if not start in graph:
        return ValueError("Start town not in routefinder")
    
    
    route = []
    
    recursive_find(graph, start, end, route, routes, 0, max_visit)
    print(routes)
    # for node in graph[start]:
    #     if node not in routes:
    #         new_routes = find_routes(graph, node, end, routes, max_visit)
    #         for new_route in new_routes:
    #             routes.append(new_route)
    return routes
    
def recursive_find(graph, start, end, route, routes, visited, max_visit):
    

    new_route = route.copy()
    new_route.append(start)
    
    if start == end and visited > 0:
        routes.append(new_route)
        
    if visited == max_visit:
        return
    
    current_visited = visited+1

    
    for i in range (len(graph[start])):
        recursive_find(graph, graph[start][i], end, new_route , routes, current_visited, max_visit)
    return routes
    
    
    
    
    
    
    
    
    
    
    
    # if path is None:
    #     path = []
        
    # visitedNodes = len(path)
    # if visitedNodes >= max_visit:
        
    #     if start == end:
    #         visitedNodes+=1
    #         return path
        
    #     visitedNodes+=1
    #     path.append(start)
    #     return path
    
    # # Recursive case
    # visitedNodes+=1
    # path.append(start) 
    
       
    # return find_routes(graph, graph[start][0], end, path)

    # if (start == end) and ( visitedNodes <= max_visit):
    #     return path
    
    # if not start in graph:
    #     return []
    
    # routes = []
    
    # for node in graph[start]:
    #     if path.count(node) < max_visit:
    #         new_routes = find_routes(graph, node, end, path, max_visit)
    #         for new_route in new_routes:
    #             routes.append(new_route)
    # return routes




# graph = {'A': ['B', 'D', 'E'], 'B': ['C', 'E'], 'C': ['D','E'], 'D': ['C'], 'E': ['B']}

graph = {'A': ['B', 'D', 'E'],
         'B': ['C'],
         'C': ['D','E'],
         'D': ['C','E'],
         'E': ['B']
        }

routes = find_routes(graph, 'C', 'C')

# if routes:
#     for route in routes:
#         print(f"{route}\n")





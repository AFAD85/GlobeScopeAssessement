import unittest
from GlobeScopeAssessement.route_finder import RouteFinder

class TestAddEdge():
    
    def test_add_edge(self):
        self.assertEqual(add_edge("AB5"), "AB5")
        
        
test_routefinder = RouteFinder("test_routefinder")
#AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
test_routefinder.add_edge("AB5")
test_routefinder.add_edge("BC4")
test_routefinder.add_edge("CD8")
test_routefinder.add_edge("DC8")
test_routefinder.add_edge("DE6")
test_routefinder.add_edge("AD5")
test_routefinder.add_edge("CE2")
test_routefinder.add_edge("EB3")
test_routefinder.add_edge("AE7")
print(test_routefinder)


AC_routes = test_routefinder.get_possible_routes("A", "C", max_stops=4)
# print(AC_routes)
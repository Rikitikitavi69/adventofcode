"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""

from collections import defaultdict
from itertools import permutations

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.weight = {}

    def addVertex(self, vertex):
        self.vertices.add(vertex)

    def addEdge(self, start, end, weight):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)
        self.edges[start].append(end)
        self.edges[end].append(start)
        self.weight[tuple(sorted([start, end]))] = weight

    def __str__(self):
        return self.vertices

def open_file(filename):
    return [x.strip().split(' ') for x in open(filename).readlines()]

def min_distance(graph):
    minDistance = -1
    for p in permutations(g.vertices):
        tempMinDistance = 0
        for i in range(len(p)-1):
            key = tuple(sorted([p[i],p[i+1]]))
            tempMinDistance += graph.weight[key]
        if minDistance < 0:
            minDistance = tempMinDistance
        if minDistance > tempMinDistance:
            minDistance = tempMinDistance

    return minDistance

def max_distance(graph):
    maxDistance = -1
    for p in permutations(g.vertices):
        tempMaxDistance = 0
        for i in range(len(p)-1):
            key = tuple(sorted([p[i],p[i+1]]))
            tempMaxDistance += graph.weight[key]
        if maxDistance < 0:
            maxDistance = tempMaxDistance
        if maxDistance < tempMaxDistance:
            maxDistance = tempMaxDistance

    return maxDistance
    

if __name__ == "__main__":

    g = Graph()
    src = open_file("9.txt")
    for l in src:
        g.addEdge(l[0], l[2], int(l[4]))         

    print("Part 1: ", min_distance(g))
    print("Part 2: ", max_distance(g))
    
"""
The graph abstract data type (ADT) is defined as follows:

Graph() creates a new, empty graph.
addVertex(vert) adds an instance of Vertex to the graph.
addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
getVertex(vertKey) finds the vertex in the graph named vertKey.
getVertices() returns the list of all vertices in the graph.
in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.


This is an implementation of graph using adjacency lists
"""
import sys;
import os;
import unittest;

class Vertex:
    def __init__(self, key):
        """

        :type key: can be any string or number
        """
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize #distance
        self.pred = None #predecessor
        self.disc = 0 #discovery time
        self.fin = 0 #finish time

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def setColor(self,color):
        self.color = color

    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime

    def setFinish(self,ftime):
        self.fin = ftime

    def getFinish(self):
        return self.fin

    def getDiscovery(self):
        return self.disc

    def getPred(self):
        return self.pred

    def getDistance(self):
        return self.dist

    def getColor(self):
        return self.color

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        '''
        Member Variables
        vertList: contains a dictionary that maps vertex names to vertex objects
        numVertices: integer>0 contains no. of vertices in the graph
        '''
        self.vertList = {}
        self.numVertices = 0
        self.edgeList={}

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        query Vertex Node object using key
        :param n: key
        :return:
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertList

    def getAllEdges(self):
        return list(self.edgeList.keys())

    def addEdge(self, f, t, cost=0):
        '''
        adds edge from f to t
        :param f: Vertex or Key f
        :param t: Vertex or key t
        :param cost: weight of edge
        :return: None
        '''
        nv1=None
        nv2=None
        if f not in self.vertList:
            nv1 = self.addVertex(f)
        if t not in self.vertList:
            nv2 = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.edgeList[(f,t)]=cost

    def getVertices(self):
        '''

        :return: name of all vertices on graph
        '''
        return list(self.vertList.keys())

    def __iter__(self):
        '''
        makes it easy to iterate over all vertices in a graph
        :return:generator object
        use: for vertex in graph:
            vertex.colo
        '''
        return iter(self.vertList.values())


class adjGraphTests(unittest.TestCase):
    def setUp(self):
        self.tGraph=Graph()

    def testMakeGraph(self):

        for i in range(6):
            self.tGraph.addVertex(i)
        print(self.tGraph.vertList)
        self.tGraph.addEdge(0, 1, 5)
        self.tGraph.addEdge(0, 5, 2)
        self.tGraph.addEdge(1, 2, 4)
        self.tGraph.addEdge(2, 3, 9)
        self.tGraph.addEdge(3, 4, 7)
        self.tGraph.addEdge(3, 5, 3)
        self.tGraph.addEdge(4, 0, 1)
        self.tGraph.addEdge(5, 4, 8)
        self.tGraph.addEdge(5, 2, 1)
        for v in self.tGraph:
            for w in v.getConnections():
                print("(%s,%s)" % (v.getId(), w.getId()))

if __name__ == "__main__":
    unittest.main()



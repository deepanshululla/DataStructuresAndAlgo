import unittest
from random import randint
from pythonds.graphs import PriorityQueue
from graphs import Graph, Vertex;

def build_graph():
    g = Graph()
    # a->b->c->d->a, d->b
    g.addEdge('s', 'a', 10)
    g.addEdge('b', 'a', 1)
    g.addEdge('c', 'b', -2)
    g.addEdge('d', 'c', -1)
    g.addEdge('e', 'd', 1)
    g.addEdge('s', 'e', 8)
    g.addEdge('d', 'a', -4)
    g.addEdge('a', 'c', 2)
    return g

def relax(u,v):
    """

    :param u: Vertex Node u
    :param v: Vertex Node v
    :return: None
    """
    if not isinstance(u,Vertex) or not isinstance(v,Vertex):
        raise Exception("Node must be vertex")
    wt=u.getWeight(v)
    du=u.getDistance()
    dv=v.getDistance()

    if du!=float('Inf') and du+wt<dv:
        v.setDistance(du+wt)
        v.setPred(u)




def bellman_ford(g,start):
    """
    The pythonds graph implementation was modified a little to accomodate Bellman ford.
    An extra list was introduced in graph which was a list of all edges in a graph
    Alternatively one can maintain a seperate list without any changes in pythonds datastructure
    getAllEdges() was the function which returned keys in the form of tuples for connected
    vertices(u,v) with u->v.

    :param g:
    :param start:
    :return:
    """

    if not isinstance(start, Vertex) or not isinstance(g,Graph):
        raise Exception("Invalid arguments")
    pq = PriorityQueue()
    dist_list={}
    for v in g:
        v.setDistance(float('Inf'))
        #setting all nodes at infinite distance initially
    start.setDistance(0)  # we set the distance of source from itself as 0
    vert_list=g.getVertices()
    edge_list=g.getAllEdges()
    for i in range(0,len(vert_list)-1):
        #iterating v-i times where v is no. of vertices
        for (u,v) in edge_list:
            uNode=g.getVertex(u)
            vNode=g.getVertex(v)
            relax(uNode,vNode)
    for u,v in edge_list:
        #checking for negative cycles
        uNode=g.getVertex(u)
        vNode=g.getVertex(v)
        wt=uNode.getWeight(vNode)
        du=uNode.getDistance()
        dv=vNode.getDistance()

        if du!=float('Inf') and du+wt<dv:
            print("graph contains no negative cycle")



    return g



class BFTest(unittest.TestCase):
    def setUp(self):
        self.tGraph = build_graph()

    #def test_graph(self):
    #    print("Edges and their weights")
    #    for v in self.tGraph:
    #        for w in v.getConnections():
    #           print("(%s->%s,%d)" % (v.getId(), w.getId(), v.getWeight(w)))

    def test_bellman_ford(self):
        print("Running bellmann ford")
        start = self.tGraph.getVertex('s')
        self.tGraph = bellman_ford(self.tGraph, start)

        for v in self.tGraph:
            print("The distance from s to %s is %d" % (v.getId(), v.getDistance()))


if __name__ == "__main__":
    unittest.main()





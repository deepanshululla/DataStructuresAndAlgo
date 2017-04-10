import unittest;
from pythonds.graphs import PriorityQueue
from pythonds.graphs import Graph, Vertex;

def build_graph():
    g = SpecialGraph()
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

class SpecialGraph(Graph):
    def __init__(self):
        """
        Inheriting the Graph class to create the child as parent class didn;t have
        member variables such as a list of all edges and their weights
        """
        super().__init__()
        self.edges_list={}
        self.vertList=self.vertices
        #in pyhton ds library vertList is implemented as vertices

    def addEdge(self,f,t,cost=0):
        '''
        adds edge from f to t
        :param f: Key f
        :param t: key t
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
        self.edges_list[(f,t)]=cost


    def get_all_edges(self):
        return list(self.edges_list.keys())

    def get_all_edge_map(self):
        return self.edges_list

    def get_vert_list(self):
        return self.vertList



class BellmannFord:
    def shortest_path(self,g,start):
        """

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
        edge_list=g.get_all_edges()
        for i in range(0,len(vert_list)-1):
            #iterating v-i times where v is no. of vertices
            for u,v in edge_list:
                uNode=g.getVertex(u)
                vNode=g.getVertex(v)
                self._relax(uNode,vNode)
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

    def _relax(self,u,v):
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



class BFTest(unittest.TestCase):
    def setUp(self):
        self.tGraph = build_graph()

    def test_graph(self):
        print("Edges and their weights")
        for v in self.tGraph:
            for w in v.getConnections():
               print("(%s->%s,%d)" % (v.getId(), w.getId(), v.getWeight(w)))

    def test_bellman_ford(self):
        print("Running bellmann ford")
        start = self.tGraph.getVertex('s')
        bf=BellmannFord()
        self.tGraph = bf.shortest_path(self.tGraph, start)

        for v in self.tGraph:
            print("The distance from s to %s is %d" % (v.getId(), v.getDistance()))


if __name__ == "__main__":
    unittest.main()





"""
Floyd warshall algorithm is used to find shortest path from all pairs of nodes
 Running time O(v^3)
 handles negative weights but not negative cycles

"""
import unittest
from pythonds.graphs import Graph, Vertex;

class FGGraph(Graph):
    def __init__(self):
        """
        Inheriting the Graph class to create the child as parent class didn;t have
        member variables such as a list of all edges and their weights
        """
        super(FGGraph,self).__init__()
        self.edges_list={}
        self.vertList=self.vertices
        #in python ds library vertList is implemented as vertices

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

    @property
    def get_all_edges(self):
        return list(self.edges_list.keys())

    def get_all_edge_map(self):
        return self.edges_list

    def get_vert_list(self):
        return self.vertList




class FloydWarshall:
    def __init__(self,graph):
        self.graph=graph
        self.vertList=graph.getVertices()
        self.num_vertices=len(self.vertList)
        self.dist={}#path distances are stored in this hashmap
        edge_map=self.graph.get_all_edge_map()
        for u in self.graph:
            for v in self.graph:
                u_id=u.getId()
                v_id=v.getId()
                if u_id==v_id:
                    self.dist[(u_id,v_id)]=0
                elif (u_id,v_id) in edge_map.keys():
                    self.dist[(u_id,v_id)]=edge_map[(u_id,v_id)]
                else:
                    self.dist[(u_id,v_id)]=float("Inf")
        #print(self.dist)
        for k in self.graph:
            for u in self.graph:
                for v in self.graph:
                    u_id=u.getId()
                    v_id=v.getId()
                    k_id=k.getId()
                    if self.dist[(u_id,v_id)]>self.dist[(u_id,k_id)]+self.dist[(k_id,v_id)]:
                        self.dist[(u_id,v_id)]=self.dist[(u_id,k_id)]+self.dist[(k_id,v_id)]


    def print_shortest_distance_matrix(self):
        for u_id,v_id in self.dist:
            if u_id!=v_id and self.dist[u_id,v_id]!=float('Inf'):
                #u=self.graph.getVertex(u_id)
                #v=self.graph.getVertex(v_id)
                print("The distance from %s to %s is %d"%(u_id,v_id,self.dist[(u_id,v_id)]))
        print("The other pair of matrices are not reachable")

    def get_shortest_distance_between(self,u,v):
        assert(u in self.vertList and v in self.vertList)
        return self.dist[(u,v)]


class FloydWarshallTest(unittest.TestCase):
    def setUp(self):
        # Let us create the following weighted graph
        """
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3
        """
        g=FGGraph()
        g.addEdge(0,1,5)
        g.addEdge(1,2,3)
        g.addEdge(2,3,1)
        g.addEdge(0,3,10)
        self.graph=g

    def test_floyd_warshall(self):
        """
        Expected solution
        Following matrix shows the shortest distances between every pair of vertices
            0       1      2     3
        0|  0      5      8      9
        1| INF      0      3      4
        2| INF    INF      0      1
        3| INF    INF    INF      0
        :return:
        """
        fw=FloydWarshall(self.graph)
        fw.print_shortest_distance_matrix()

if __name__=="__main__":
    unittest.main()


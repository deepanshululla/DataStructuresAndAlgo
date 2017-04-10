import unittest
from pythonds.graphs import Graph, Vertex;


class CycleDetector:
    def __init__(self,graph):
        assert(isinstance(graph,Graph))
        self.graph=graph
        self.cycle_exists=False


    def cycle_exists_directed(self):
        """
        uses DFS to detect cycles.
        Cycle exists if we have a node whoose neighbour has color gray,wich means it is
        already processed
        True if cycle exists else False
        :return:Boolean
        """

        for vertex in self.graph:
            vertex.setColor('white')
        #setting color of all vertices to white
        for vertex in self.graph:
            if self.cycle_exists:
                break
            self.dfs_detect(vertex)
        #print(self.cycle_exists)
        return not self.cycle_exists

    def dfs_detect(self,vertex):
        assert(isinstance(vertex,Vertex))
        vertex.setColor('gray')
        for nbr in vertex.getConnections():
            if nbr.getColor()=="gray":
                self.cycle_exists=True
            if nbr.getColor()=="white":
                nbr.setPred(vertex)
                self.dfs_detect(nbr)
        vertex.setColor('black')

    @property
    def get_all_edges(self):
        return list(self.edges_list.keys())

    def get_all_edge_map(self):
        return self.edges_list

class CycleTesting(unittest.TestCase):

    def test_positive_detection_cycle(self):
        graph=Graph()
        graph.addEdge(1, 0);
        graph.addEdge(0, 2);
        graph.addEdge(2, 0);
        graph.addEdge(0, 3);
        graph.addEdge(3, 4);
        cd=CycleDetector(graph)
        print (cd.cycle_exists_directed())

    def test_negative_detection_cycle(self):
        graph1=Graph()
        graph1.addEdge(0,1)
        graph1.addEdge(1,2)
        cd=CycleDetector(graph1)
        print (cd.cycle_exists_directed())


if __name__=="__main__":
    unittest.main()


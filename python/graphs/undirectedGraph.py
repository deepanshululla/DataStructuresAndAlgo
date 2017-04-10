from pythonds.graphs import Graph, Vertex;


class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
        self.vertList=self.vertices
        self.edges_list={}

    def addEdge(self, f, t, cost=0):
        """
        adds edge from f to t
        :param f: Key f
        :param t: key t
        :param cost: weight of edge
        :return: None
        """
        nv1=None
        nv2=None
        if f not in self.vertList:
            nv1 = self.addVertex(f)
        if t not in self.vertList:
            nv2 = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)
        self.edgeList[(f,t)]=cost

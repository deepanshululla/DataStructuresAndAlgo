'''
Given a directed graph, a source vertex ‘s’
and a destination vertex ‘d’, print if 'd' is reachable from ‘s’.
'''

from pythonds.graphs import Vertex,Graph;
from pythonds.basic import Queue;
import unittest;


class ReachGraph(Graph):
    def __init__(self):
        super().__init__()
    def isReachable(self,u,v):
        """

        :param u: Key
        :param v: Key
        :return:
        """
        vertList=self.getVertices()
        assert(u in vertList and v in vertList)
        start=self.getVertex(u)
        end=self.getVertex(v)
        start.setDistance(0)
        start.setPred(None)
        vertQueue=Queue()
        vertQueue.enqueue(start)
        while(vertQueue.size()!=0):
            currentVert=vertQueue.dequeue()
            if currentVert.getId()==end.getId():
                return True
            for nbr in currentVert.getConnections():
                if nbr.getColor()=="white":

                    nbr.setColor('gray')
                    nbr.setPred(currentVert)
                    nbr.setDistance(currentVert.getDistance()+1)
                    vertQueue.enqueue(nbr)

            currentVert.setColor('black')
        return False





class ReachabilityTest(unittest.TestCase):
    def setUp(self):
        g=ReachGraph()
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)
        self.graph=g

    def test_reach(self):
        print(self.graph.isReachable(1,3))


if __name__=="__main__":
    unittest.main()

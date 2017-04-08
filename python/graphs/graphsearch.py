from graphs import Vertex,Graph;
from pythonds.basic import Queue;
from wordladder import buildGraph;
import unittest;

class BFS:
    def __init__(self,g,start):
        '''
        The general algorithm is based on 3 colors
        white: not visited not processed
        grey: visited but not processed
        black: visited and processed
        The term processed means all adjacent vertices have been visited.
        hence a black node can't have a white neighbor but can have grey or black neighbors

        We maintain a queue of nodes to be visited and we run the algo until the queue is empty
        Then for every neighbor of the currentNode, we check if it is white,set it to gray,
        increment distance by 1,change neighbor's parent to current node and add neighbor to queue

        Running time: O(V+E)
        :param g: Graph
        :param start: starting node or string
        :return: None
        '''
        if not isinstance(start,Vertex) or not isinstance(g,Graph):
           raise Exception("Invalid paramaters")
        start.setDistance(0)
        start.setPred(None)
        self.vertQueue=Queue()
        self.vertQueue.enqueue(start)
        while (self.vertQueue.size()>0):
            currentVert=self.vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if nbr.getColor()=='white':
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance()+1)
                    nbr.setPred(currentVert)
                    self.vertQueue.enqueue(nbr)
                currentVert.setColor('black')
            #print((vertQueue))

    def traverse(self,y):
        '''
        following the predecessor links to print out the word ladder.
        :param y: Node in a graph
        :return: None
        '''

        x = y
        while (x.getPred()):
            print(x.getId())
            x = x.getPred()
        print(x.getId())

class DFS:
    def __init__(self, graph, start=None):
        """

        The general algorithm is based on 3 colors
        white: not visited not processed
        grey: visited but not processed
        black: visited and processed
        The term processed means all adjacent vertices have been visited.
        hence a black node can't have a white neighbor but can have grey or black neighbors
        :param graph: Graph object
        :param start: start vertex
        """

        assert isinstance(graph, Graph)
        if start:
            assert isinstance(start,Vertex)
            self.start=start
            self.start.setPred(None)
        self.graph=graph

        self.current_time=0
        if start:
            self.dfs_wrapper()
        else:
            self.dfs_wrapper_complete()

    def dfs_wrapper(self):
        """
        wrapper for tracing source to destination
        :return:
        """
        for vertex in self.graph:
            vertex.setColor('white')
        self.dfs_visit(self.start)

    def dfs_wrapper_complete(self):
        """
        wrapper for running DFs on all vertices
        :return:
        """
        for vertex in self.graph:
            vertex.setColor('white')
        #self.start.setColor('black')
        for vertex in self.graph:
            if vertex.getColor()=="white":
                self.dfs_visit(vertex)

    def dfs_visit(self,vertex):
        vertex.setColor('gray')
        self.current_time+=1
        vertex.setDiscovery(self.current_time)
        for nbr in vertex.getConnections():
            if nbr.getColor()=="white":
                nbr.setPred(vertex)
                self.dfs_visit(nbr)
        vertex.setColor('black')
        vertex.setFinish(self.current_time)

    def traverse(self,y):
        '''
        following the predecessor links to print out the word ladder.
        :param y: Node in a graph
        :return: None
        '''

        x = y
        while (x.getPred()):
            print(x.getId(),x.getDiscovery(),x.getFinish())
            x = x.getPred()
        print(x.getId())


class DFSTest(unittest.TestCase):
    def setUp(self):
        self.tGraph=buildGraph('word.txt')
        '''
        for v in self.tGraph:
            for w in v.getConnections():
                print("(%s,%s)" % (v.getId(), w.getId()))
        '''

    def testDfs(self):
        #vertices=self.tGraph.getVertices()
        #print(vertices)
        '''
        testcase involves traversing the graph from 'sage' to 'fool'
        Expected output
        sage
        page
        pale
        pall
        poll
        pool
        fool

        :return:
        '''

        obj=self.tGraph.getVertex('fool')
        #obj.setPred(None)
        #print(obj)
        Dfs=DFS(self.tGraph,obj)

        #for v in self.tGraph:
        #    print("(%s,%d,%d)" % (v.getId(), v.getDiscovery(),v.getFinish()))
        Dfs.traverse(self.tGraph.getVertex('sage'))

"""
class BFSTest(unittest.TestCase):
    def setUp(self):
        self.tGraph=buildGraph('word.txt')
        '''
        for v in self.tGraph:
            for w in v.getConnections():
                print("(%s,%s)" % (v.getId(), w.getId()))
        '''

    def testBfs(self):
        #vertices=self.tGraph.getVertices()
        #print(vertices)
        '''
        testcase involves traversing the graph from 'sage' to 'fool'
        Expected output
        sage
        page
        pale
        pall
        poll
        pool
        fool

        :return:
        '''
        obj=self.tGraph.getVertex('fool')
        #print(obj)
        Bfs=BFS()
        Bfs.bfs(self.tGraph,obj)
        Bfs.traverse(self.tGraph.getVertex('sage'))
"""

if __name__=="__main__":
    unittest.main()

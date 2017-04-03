from graphs import Vertex;
from pythonds.basic import Queue;
from wordladder import buildGraph;
import unittest;

class BFS:
    def bfs(self,g,start):
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
        if not isinstance(start,Vertex):
           raise Exception("Start must be a vertex node of graph")
        start.setDistance(0)
        start.setPred(None)
        vertQueue=Queue()
        vertQueue.enqueue(start)
        while (vertQueue.size()>0):
            currentVert=vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if nbr.getColor()=='white':
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance()+1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
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

if __name__=="__main__":
    unittest.main()

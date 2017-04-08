'''
Given a directed graph, a source vertex ‘s’
and a destination vertex ‘d’, print all paths from given ‘s’ to ‘d’.
'''

from pythonds.graphs import Vertex,Graph;
import unittest;

class PrintPaths:
    def __init__(self,g,s,t):
        """
        :param g: Graph
        :param s: Start Vertex
        :param t: Target vertex
        :return: None
        """
        assert isinstance(g, Graph)
        assert isinstance(s,Vertex)
        assert isinstance(t,Vertex)
        self.graph=g
        self.start=s
        self.target=t
        self.start.setPred(None)
        self.paths=[]

    def print_all_paths(self):
        path=[]
        for vertex in self.graph:
            vertex.setColor('white')
        self.print_path_utils(self.start,path)
        #print(self.paths)
        self.print_path_keys()

    def print_path_keys(self):
        #print(self.paths)
        for path in self.paths:
            for vertex in path:
                #print(vertex)
                id=vertex.getId()
                print(id,end=' ')
            print()
        #print(len(self.paths))


    def print_path_utils(self,start,path):
        start.setColor('gray')
        path.append(start)

        if start.getId()==self.target.getId():

            self.paths.append(list(path))
        else:
            for nbr in start.getConnections():
                if nbr.getColor()=='white':
                    self.print_path_utils(nbr,path)
        path.pop()

        start.setColor('white')



class PrintAllPathsTest(unittest.TestCase):
    def setUp(self):
        g=Graph()
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(0, 3)
        g.addEdge(2, 0)
        g.addEdge(2, 1)
        g.addEdge(1, 3)
        self.graph=g
        self.start = g.getVertex(2)
        self.target = g.getVertex(3)


    def test_print_paths(self):
        #print ("Following are all different paths from %d to %d :" %(s, d))
        p=PrintPaths(self.graph,self.start,self.target)
        p.print_all_paths()

if __name__=="__main__":
    unittest.main()

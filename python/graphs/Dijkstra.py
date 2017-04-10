import unittest
from random import randint
from pythonds.graphs import PriorityQueue
from pythonds.graphs import Graph, Vertex;



def build_graph_with_word_file(word_file):
    """
    This
    :param word_file:
    :return: graph Object
    """
    d = {}
    g = Graph()
    wfile = open(word_file, 'r')
    # create buckets of words that
    # differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words
    # in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2, randint(0, 9))
                    # g.addEdge(word2, word1, randint(0, 9))
    # print(d)
    return g


def build_graph():
    g = Graph()
    # a->b->c->d->a, d->b
    g.addEdge('a', 'b', 4)
    g.addEdge('b', 'c', 5)
    g.addEdge('c', 'd', 3)
    g.addEdge('d', 'a', 2)
    g.addEdge('b', 'd', 1)
    return g

class Dijkstra:
    def shortest_path(self,aGraph, start):
        """
        uses vertex.dist to realize distance between nodes.
        The dist instance variable will contain the current total weight of the smallest
        weight path from the start to the vertex in question.
        Time Complexity: O((V+E)logV)
        :param aGraph: Graph Object
        :param start: vertex Object
        :return:aGraph: Graph Object
        """
        if not isinstance(start, Vertex):
            raise Exception("Value Error: second parameter must be a vertex node")
        pq = PriorityQueue()
        start.setDistance(0)  # we set the distance of source from itself as 0
        pq.buildHeap([(v.getDistance(), v) for v in aGraph])
        # we are building a priority queue of tuple of vertices and their distances from source
        # Initially all distances are set to infinity
        while not pq.isEmpty():
            currentVert = pq.delMin()  # extracts minimum and reconstructs the heap
            for nextVert in currentVert.getConnections():
                newDist = currentVert.getDistance() \
                          + currentVert.getWeight(nextVert)
                if newDist < nextVert.getDistance():
                    # Checking if d[v]<d[u]+w[u,v]
                    nextVert.setDistance(newDist)
                    nextVert.setPred(currentVert)
                    pq.decreaseKey(nextVert, newDist)
                    # decrease key value and reconstructs the heap
        return aGraph


class DijkstraTest(unittest.TestCase):
    def setUp(self):
        self.tGraph = build_graph()

    def test_graph(self):
        print("Edges and their weights")
        for v in self.tGraph:
            for w in v.getConnections():
                print("(%s->%s,%d)" % (v.getId(), w.getId(), v.getWeight(w)))

    def test_dijkstra(self):
        print("Running Dijkstra")
        start = self.tGraph.getVertex('a')
        sp=Dijkstra()
        self.tGraph = sp.shortest_path(self.tGraph, start)

        for v in self.tGraph:
            print("The distance from a to %s is %d" % (v.getId(), v.getDistance()))


if __name__ == "__main__":
    unittest.main()

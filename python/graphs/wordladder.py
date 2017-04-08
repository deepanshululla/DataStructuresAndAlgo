from graphs import Graph;
import unittest

def buildGraph(wordFile):
    d={}
    g=Graph()
    wfile=open(wordFile,'r')
    #create buckets of words that
    #differ by one letter
    for line in wfile:
        word=line[:-1]
        for i in range(len(word)):
            bucket=word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket]=[word]
    #add vertices and edges for words
    #in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1!=word2:
                    g.addEdge(word1,word2)
    print(d)
    return g

class BuildGraphTest(unittest.TestCase):
    def setUp(self):
        self.tGraph=buildGraph('word.txt')

    def testGraph(self):
        for v in self.tGraph:
            for w in v.getConnections():
                print("(%s,%s)" % (v.getId(), w.getId()))


if __name__=="__main__":
    unittest.main()

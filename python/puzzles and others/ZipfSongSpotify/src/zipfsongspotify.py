import sys
import heapq
class StoreInput:
    def __init__(self):
        songsHeap=[]
        firstLine=sys.stdin.readline()
        mS,nS=firstLine.split()
        self.albumLength=int(mS)
        self.selected=int(nS)
        for i in range(self.albumLength):
            currSong = sys.stdin.readline()
            fr=int(currSong.split()[0])
            name=currSong.split()[1]
            sg=Song(fr,name,i+1)
            heapq.heappush(songsHeap, (-sg.getQuality(), sg.index, sg))
        self.songsHeap=songsHeap    
    def getProcessedHeap(self):
        return self.songsHeap
    def getNumSelected(self):
        return self.selected
    
class Song:
    def __init__(self,frequency,name,index):
        self.name=name
        self.frequency=int(frequency)
        self.index=int(index)
        #self.quality=-1*index*frequency
    def getQuality(self):
        return self.index*self.frequency

def main(argv=None):
    inp=StoreInput()
    numSelections=inp.getNumSelected()
    songsList=inp.getProcessedHeap()
    
    i=0
    #print songsList
    while i<numSelections:
        song = heapq.heappop(songsList)[2]
        i+=1
        print(song.name)

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
import threading
import time


def timer(name, delay, repeat):
    print(name + 'started')
    for j in range(repeat):
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))
    print(name + 'completed')

def timerLocking(name, delay, repeat):

    tlock.acquire()
    print(name + 'started and acquired lock')
    for j in range(repeat):
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))

    print(name + 'completed and relaeased lock')
    tlock.release()


def printSomething(something):
    for i in range(20):
        print(something)

class AsynchronousWrite(threading.Thread):
    #basic threading program to write a file in background
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text=text
        self.out=out
    def run(self):
        f=open(self.out,'a')
        f.write(self.text+'\n')
        f.close()
        time.sleep(2)
        print("finished writing")


def main():
    '''
    t1 = threading.Thread(target=timer, args=('timer1',1,5,))
    t2 = threading.Thread(target=timer, args=('timer2',2,5,))
    t1.start()
    t2.start()
    '''
    message=input("Enter a string to store:")
    background=AsynchronousWrite(message,'out.txt')
    background.start()
    #starts running background function
    print ("the program continues to run")
    print(100+500)
    background.join()
    print("waited until thread was complete")
    t1 = threading.Thread(target=timerLocking, args=('timer1',1,5,))
    t2 = threading.Thread(target=timerLocking, args=('timer2',2,5,))
    t1.start()
    t2.start()


tlock=threading.Lock()

# print("hello")
main()
# print("done")

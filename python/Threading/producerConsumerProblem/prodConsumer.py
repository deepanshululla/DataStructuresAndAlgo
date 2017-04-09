import threading
import time
import random

queue=[]
lock=threading.Lock()
condition=threading.Condition()

class ProducerThread(threading.Thread):

    def run(self):
        nums=list(range(5))#creates list [0,1,2,3,4]
        global queue
        while True:
            condition.acquire()
            num=random.choice(nums) #chooses randomly one of
            queue.append(num)
            print("produced ",num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Queue is empty. So I will wait until notifed")
                condition.wait()
                print("Producer added something. Queue is no longer empty")
            num=queue.pop()
            print("Consumed",num)
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()

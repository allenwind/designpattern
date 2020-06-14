import random
import time
import threading
import queue

data = list(range(1, 11))
stop = None
_sentinel = object()

data.append(_sentinel)

def producer(queue_):
    while True:
        if stop:
            print("producer quit")
            break
        time.sleep(random.random())
        data_ = random.choice(data)
        try:
            queue_.put(data_, block=False)
        except queue.Full as e:
            pass

def consumer(queue_):
    while True:
        if stop:
            print("consumer quit")
            break
        time.sleep(random.random())
        data_ = queue_.get(timeout=0.5)
        if data_ is _sentinel:
            queue_.task_done()
            set_stop(0)

def watcher(queue_):
    while True:
        if stop:
            break
        time.sleep(1)
        print(queue_.qsize(), queue_.queue, sep=' --> ')

def set_stop(interval):
    time.sleep(interval)
    global stop
    if queue_.empty(): #not q.full()
        queue_.task_done()
    stop = True

if __name__ == '__main__':
    qsize = 10
    
    queue_ = queue.Queue(qsize)
    p = threading.Thread(target=producer, args=(queue_,))
    c = threading.Thread(target=consumer, args=(queue_,))
    w = threading.Thread(target=watcher, args=(queue_,))
    s = threading.Thread(target=set_stop, args=(50, ))

    p.start()
    c.start()
    w.start()
    s.start()
    queue_.join()

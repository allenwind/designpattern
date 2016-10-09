import time
import random
import queue

from queue import Queue
from threading import Thread, Event

class ActorExit(Exception):
    pass

class Actor:
    _qsize = 10
    
    def __init__(self):
        self._mailbox = Queue(self._qsize)
        self._result = []

    def send(self, msg, *args, **kwargs):
        time.sleep(random.random()) #sleep random
        self._mailbox.put((msg, args, kwargs))

    def recv(self):
        time.sleep(random.random())
        msg = self._mailbox.get(block=True)
        
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()

    def add_result(self, result):
        self._result.append(result)

    def show_result(self):
        for item in self._result:
            print(item)

    def submit(self, func, *args, **kwargs): #like concurrent.futures submit
        self.send(func, *args, **kwargs)
        
def countdown(n, interval=0.3): #for test
    while n > 0:
        time.sleep(interval)
        n -= 1
    return "countdown is end"

def counter(num1, num2):
    time.sleep(random.random())
    return num1 * num2

class ActorTask(Actor):
    def run(self):
        while True:
            task, args, kwargs = self.recv()
            if task.startswith('do_'):  #use inner task
                task = getattr(self, task)
            result = task(*args, **kwargs)
            self.add_result((task.__name__, result))

    def do_A(self, *args, **kwargs):
        pass

    def do_b(self, *args, **kwargs):
        pass
        

if __name__ == '__main__':
    p = ActorTask()
    p.start()
    p.send(countdown, 10, interval=0.2)
    p.send(counter, num1=123, num2=456)
    p.show_result()
    





















    

    

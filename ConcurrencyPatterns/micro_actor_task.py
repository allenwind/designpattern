from collections import deque

#使用生成器来实现一个不依赖线程的 actor
    

class MicroActor:
    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass

def printer():
    while True:
        msg = yield
        print('get', msg, sep='-->')

def counter(sched):
    while True:
        n = yield
        if n == 0:
            break

    sched.send('printer', n)

    sched.send('counter', n-1)

if __name__ == '__main__':
    sched = MicroActor()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))
    sched.send('counter', 1000)
    sched.run()





























    
            

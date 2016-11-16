from collections import defaultdict
from contextlib import contextmanager

#消息会被发送给一个交换机，然后交换机会将它们发送给被绑定的订阅者

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):  #use 'with' stynax
        self._subscribers.add(task)

    def detach(self, task):   
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    def distrubte(self, msg):
        pass

    @contextmanager
    def subscribe(self, *tasks):  #with subscribe stynax
        for task in tasks:
            self.attach(task)
        try:
            yield self
        finally:
            for task in tasks:
                self.detach(task)

_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]

class Task:
    def send(self, msg):
        print('recv', msg , sep='-->')

class Subscriber:
    def __init__(self, name):
        self._name = name
        self.count = 0
    def send(self, msg):
        self.count += 1
        print("{name} get {msg}".format_map({'name': self._name,
                                             'msg': msg}))

"""交换机可以实
现一整个消息通道集合或提供交换机名称的模式匹配规则。交换机还可以被扩展到分
布式计算程序中（比如，将消息路由到不同机器上面的任务中去）。
"""

if __name__ == '__main__':
    task_a = Task()
    task_b = Task()
    s = Subscriber('redis')

    exc = get_exchange('name')  #select channel
    
    exc.attach(task_a)
    exc.attach(task_b)
    exc.attach(s)

    exc.send('I am great')
    exc.send('Hello Python')
    

    


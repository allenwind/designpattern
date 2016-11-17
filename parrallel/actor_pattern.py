import queue
import time
import random
import threading
import multiprocessing
import unittest

#优先队列功能
#添加协程模式
#添加非阻塞模式
#put method may be not block

#single, thread, process

"""actor模式：
基础类接口
守护线程类
守护进程类
多线程类
多进程类

协程类

线程服务器类
进程服务器类
参考socketserver接口"""

__all__ =['ThreadingActor', 'ActorTask', 'ProcessingActor', 'ProprityThreadingActor', 'Actor']

class ActorExit(Exception):
    pass

class ExecuteError(Exception):
    pass

class Actor:
    _qsize = 100

    def __init__(self):
        self._init(self)

    def send(self, task, *args, **kwargs):
        self._mailbox.put((task, args, kwargs))

    def recv(self, block=True, timeout=None):
        try:
            task, args, kwargs = self._mailbox.get(block=True, timeout=timeout)
        except queue.Empty as err:
            task = ActorExit

        if task is ActorExit:
            raise ActorExit()
        return task, args, kwargs

    def start(self):
        raise NotImplementedError("must start by MixIn pattern!")

    def close(self):
        self.send(ActorExit)

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def _wrapper_task(self, task, *args, **kwargs):
        result = task(*args, **kwargs)
        self._results.put(result)
        return 
        
class TaskHandler:
    """Actor的执行句柄"""

    def __init__(self, *args, **kwargs):
        pass

    def setup(self):
        pass

    def handle(self):
        pass

    def finish(self):
        pass

class ActorTask:
    """扩展Actor的接口"""
    def get_results(self):
        return self._results.queue

    def clear_results(self):
        self._results.queue.clear()

    def set_qsize(self, time_=10):
        self._qsize = self._qsize * time_
        data = self._results.queue
        pass
        
class ThreadingMixIn:
    def __init__(self, taskhandler=None):
        self._mailbox = queue.Queue(self._qsize)
        self._results = queue.Queue(self._qsize)
        self._errors = queue.Queue()

    def start(self):
        self._terminated = threading.Event()
        thread = threading.Thread(target=self._bootstrap)
        thread.daemon = True
        thread.start()
        
    def run(self):
        while True:
            task, args, kwargs = self.recv()
            try:
                threading.Thread(target=self._wrapper_task, args=(task, *args),
                                 kwargs=kwargs).start()
            except Exception as err:
                self._errors.put((task, args, kwargs))
                raise ExecuteError from err

class ProcessingMixIn:
    def __init__(self, taskhandler=None):
        self._mailbox = multiprocessing.Queue(self._qsize)
        self._results = multiprocessing.Queue(self._qsize)
        self._errors = multiprocessing.Queue()

    def start(self):
        self._terminated = multiprocessing.Event()
        process = multiprocessing.Process(target=self._bootstrap)
        process.daemon = True
        process.start()

    def run(self):
        while True:
            task, args, kwargs = self.recv()
            try:
                multiprocessing.Process(target=self._wrapper_task, args=(task, *args),
                                        kwargs=kwargs).start()
            except Exception as err:
                self._errors.put((task, args, kwargs))
                raise ExecuteError from err

class PriorityThreadingMixIn(ThreadingMixIn):
    def __init__(self, taskhandler=None):
        self._mailbox = queue.PriorityQueue(self._qsize)
        self._results = queue.PriorityQueue(self._qsize)
        self._errors = queue.PriorityQueue()

    def send(self, proprity, task, *args, **kwargs):
        self._mailbox.put((proprity, task, args, kwargs))

    def recv(self, block=True, timeout=None):
        try:
            proprity, task, args, kwargs = self._mailbox.get(block=True)
        except Exception as err:
            task = ActorExit 

        if task is ActorExit:
            raise ActorExit()
        return proprity, task, args, kwargs

    def _wrapper_task(self, proprity, task, *args, **kwargs):
        result = task(*args, **kwargs)
        self._results.put((proprity, result))

    def run(self):
        while True:
            proprity, task, args, kwargs = self.recv()
            try:
                threading.Thread(target=self._wrapper_task, args=(task, *args),
                                 kwargs=kwargs).start()
            except Exception as err:
                self._errors.put((proprity, task, args, kwargs))
                raise ExecuteError from err

class ThreadingActor(ThreadingMixIn, Actor, ActorTask):
    pass

class ProcessingActor(ProcessingMixIn, Actor, ActorTask):
    pass

class PriorityThreadingActor(PriorityThreadingMixIn, Actor, ActorTask):
    pass

class ActorTest(unittest.TestCase):

    def test_actor_start(self):
        actor = Actor()
        with self.assertRaises(NotImplementedError):
            actor.start()

    def test_threading(self):
        pass

    def test_processing(self):
        pass

    def test_proprity(self):
        pass

if __name__ == '__main__':
    pass








    

"""系统会随着演化变得非常复杂，最终形成大量的（并且有时是令人迷惑的）类和交互，这种
情况并不少见。许多情况下，我们并不想把这种复杂性暴露给客户端。外观设计模式有助于隐藏
系统的内部复杂性，并通过一个简化的接口向客户端暴露必要的部分。本质上，外观（Facade）是在已有复杂系统之上实现的一个抽象层
"""

"""使用外观模式的最常见理由是为一个复杂系统提供单个简单的入口点。引入外观之后，客户
端代码通过简单地调用一个方法/函数就能使用一个系统。同时，内部系统并不会丢失任何功能，
外观只是封装了内部系统。

我们可以改变系统内部，但客户端代码不用关心这个改变，也不会受这个改变的影响"""

#用多服务进程方式实现一个操作系统
#多服务进程的操作系统有一个极小的内核，称为微内核（microkernel），它在特权模式下运行
#系统的所有其他服务都遵从一种服务架构（驱动程序服务器、进程服务器、文件服务器等）
#

import abc

from enum import Enum 

State = Enum('State', 'new running sleeping restart zombie')
#用枚举记录状态

class Server(metaclass=abc.ABCMeta):
    #作为已给类模板，强制定义接口
    @abc.abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def boot(self):
        pass

    @abc.abstractmethod
    def kill(self, restart=True):
        pass

class FileServer(Server):
    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print("trying to create the file '{}' for user '{}' with permisions {}".
            format(name, user, permissions))

class ProcessServer(Server):
    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        print("trying to create the process '{}' for user '{}'".format(name, user))


class OperatingSystem:
    #对上面定义的类从新包装，开放出简单的APIs
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permisions):
        return self.fs.create_file(user, name, permisions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('hello', 'world', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')

if __name__ == '__main__':
    main()

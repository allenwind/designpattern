"""责任链模式:

责任链（Chain of Responsibility）模式用于让多个对象来处理单个请求
时，或者用于预先不知道应该由哪个对象（来自某个对象链）来处理某个特定请求时。其原则
如下所示。
(1) 存在一个对象链（链表、树或任何其他便捷的数据结构）。
(2) 我们一开始将请求发送给链中的第一个对象。
(3) 对象决定其是否要处理该请求。
(4) 对象将请求转发给下一个对象。
(5) 重复该过程，直到到达链尾"""

"""例子：
Java的servlet过滤器是在一个HTTP请求到达目标处理程序之前执行的一些代码片段。 在使用
servlet过滤器时，有一个过滤器链，其中每个过滤器执行一个不同动作（用户身份验证、记日志、
数据压缩等），并且将请求转发给下一个过滤器直到链结束；如果发生错误（例如，连续三次身
份验证失败）则跳出处理流程"""

"""通过使用责任链模式，我们能让许多不同对象来处理一个特定请求。在我们预先不知道应该
由哪个对象来处理某个请求时，这是有用的。

另一个责任链可以派上用场的场景是，在我们知道可能会有多个对象都需要对同一个请求进
行处理之时。"""

"""这一模式的价值在于解耦。客户端与所有处理程序（一个处理程
序与所有其他处理程序之间也是如此）之间不再是多对多关系，客户端仅需要知道如何与链的起
始节点（标头）进行通信。"""

class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


#UML图中展示的parent聚合关系表明每个控件都有一个到父对象的引用
class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event): 
        #关联关系用于表明Widget类知道Event类
        #核心在这里,handle方法用于连接责任链上
        #的方法。这些方法依据设计分布在不同的子类中
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)

        elif self.parent:
            self.parent.handle(event)

        elif hasattr(self, 'handle_default'):
            self.handle_default(event)

class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))

class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))

class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('Sending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}_ to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
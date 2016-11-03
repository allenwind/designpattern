"""策略模式（Strategy pattern）鼓励使用多种算法来解决一个问题，其杀手级特性是能够在运
行时透明地切换算法（客户端代码对变化无感知）。因此，如果你有两种算法，并且知道其中一
种对少量输入效果更好，另一种对大量输入效果更好，则可以使用策略模式在运行时基于输入数
据决定使用哪种算法"""

"""我们已看到Python和Java如何使用策略模式来支持不同的排序算法。然而，策略模式并不限
于排序问题，也可用于创建各种不同的资源过滤器（身份验证、日志记录、数据压缩和加密等），
请参考网页

策略模式的另一个应用是创建不同的样式表现，为了实现可移植性（例如，不同平台之间断
行的不同）或动态地改变数据的表现。

另一个值得一提的应用是模拟；例如模拟机器人，一些机器人比另一些更有攻击性，一些机
器人速度更快，等等。机器人行为中的所有不同之处都可以使用不同的策略来建模"""

import pprint

from collections import namedtuple
from operator import attrgetter



if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('JavaScript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23))

    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print('\n')
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))


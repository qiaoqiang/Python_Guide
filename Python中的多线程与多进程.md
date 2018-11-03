# 多线程



# 多进程

`https://blog.csdn.net/jw690114549/article/details/69396267`

- Process
- multiprocess
- Pool
- Pipe







# 其他



## ctypes

看到ctypes库，有时间了解一下

```python
# -*- coding: utf-8 -*-

from pprint import pprint

# 共享内存
from multiprocessing import sharedctypes, Process, Lock
from ctypes import Structure, c_bool, c_double

pprint(sharedctypes.typecode_to_type)

lock = Lock()


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]  # _fields_


def modify(n, b, s, arr, A):
    n.value **= 2
    b.value = True
    s.value = s.value.upper()
    arr[0] = 10
    for a in A:
        a.x **= 2
        a.y **= 2

if __name__ == '__main__':

    n = sharedctypes.Value('i', 7)
    b = sharedctypes.Value(c_bool, False, lock=False)
    s = sharedctypes.Array('c', b'hello world', lock=lock)  # bytes
    arr = sharedctypes.Array('i', range(5), lock=True)
    A = sharedctypes.Array(Point, [(1.875, -6.25), (-5.75, 2.0)], lock=lock)
    p = Process(target=modify, args=(n, b, s, arr, A))
    p.start()
    p.join()
    print(n.value)
    print(b.value)
    print(s.value)
    print(arr[:])
    print([(a.x, a.y) for a in A])
--------------------- 
作者：蒋狗 
来源：CSDN 
原文：https://blog.csdn.net/jw690114549/article/details/69396267 
版权声明：本文为博主原创文章，转载请附上博文链接！
```




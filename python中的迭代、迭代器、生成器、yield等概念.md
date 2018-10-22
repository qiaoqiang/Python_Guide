# python中的迭代、迭代器、生成器、yield等概念

enumerate 枚举

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

## python的列表表达式（列表生成式）



## python的迭代

可迭代
一个对象，物理或者虚拟存储的序列。list，tuple，strins，dicttionary，set以及生成器对象都是可迭代的，整型数是不可迭代的。如果你不确定哪个可迭代哪个不可以，你需要用python内建的iter()来帮忙。



>>> iter([1,2,3])
>>> <listiterator object at 0x026C8970>>>> iter({1:2, 2:4})
>>> <dictionary-keyiterator object at 0x026CC1B0>>>> iter(1234)
>>> Traceback (most recent call last):
>>>   File "<pyshell#145>", line 1, in <module>
    iter(1234)TypeError: 'int' object is not iterable
iter()为list返回了listiterator对象，为dictionary返回了dictionary-keyiterator对象。类似对其他可迭代类型也会返回迭代器对象。

iter()用在自定义的类型会怎样呢？我们先自己定义一个String类：

class String(object):
  def __init__(self, val):
    self.val = val  def __str__(self):
    return self.val
st = String('sample string')
那么，st是可迭代的吗？

>>> iter(st)TypeError: 'String' object is not iterable
>>> 你可能会有几个问题要问：

怎么让自定义的类型可迭代？

iter()究竟做了些什么？

让我们补充String类来找找答案

class String(object):
    def __init__(self, val):
        self.val = val    def __str__(self):
        return self.val    def __iter__(self):
        print "This is __iter__ method of String class"
        return iter(self.val)  #self.val is python string so iter() will return it's iterator
>>> st = String('Sample String')>>> iter(st)
>>> This is __iter__ method of String class<iterator object at 0x026C8150>
>>> 在String类中需要一个’__iter__’方法把String类型变成可迭代的，这就是说’iter’内部调用了’iterable.__iter__()’

别急，不是只有增加’__iter()’方法这一种途径

class String(object):
    def __init__(self, val):
        self.val = val    def __str__(self):
        return self.val    def __getitem__(self, index):
        return self.val[index]
>>> st = String('Sample String')>>> iter(st)
>>> <iterator object at 0x0273AC10>
>>> ‘itr’也会调用’iterable.__getitem__()’，所以我们用’__getitem__’方法让String类型可迭代。

如果在String类中同时使用’__iter__()’和’__getitem__()’,就只有’__iter__’会起作用。

自动迭代
for循环会自动迭代

for x in iterable:    print x
我们可以不用for循环来实现吗？

def iterate_while(iterable):
    index = 0
    while(i< len(iterable)):        print iterable[i]
        i +=1
这样做对list和string是管用的，但对dictionary不会奏效，所以这绝对不是python式的迭代，也肯定不能模拟for循环的功能。我们先看迭代器，等下回再过头来。

迭代器
关于迭代器先说几条………..

1. 迭代器对象在迭代过程中会会产生可迭代的值，`next()`或者`__next()__`是迭代器用来产生下一个值的方法。

2. 它会在迭代结束后发出StopIteration异常。

3. `iter()`函数返回迭代器对象

4. 如果`iter()`函数被用在迭代器对象，它会返回对象本身

我们试一试模仿for循环

def simulate_for_loop(iterable):
    it = iter(iterable)    while(True):	try:	    print next(it)	except StopIteration:	    break
>>> simulate_for_loop([23,12,34,56])23123456
>>> 前面我们看过了iterable类，我们知道iter会返回迭代器对象。

现在我们试着理解迭代器类的设计。

class Iterator:
    def __init__(self, iterable)
        self.iterable = iterable
    .
    .    def __iter__(self):  #iter should return self if called on iterator
        return self
    def next(self):  #Use __next__() in python 3.x
        if condition: #it should raise StopIteration exception if no next element is left to return
            raise StopIteration
我们学了够多的迭代和迭代器，在python程序中不会用到比这更深的了。

但是为了学习的目的我们就到这儿。。。。

列表迭代器
你可能会在面试中写这个，所以打起精神来注意了

class list_iter(object):
    def __init__(self, list_data):
        self.list_data = list_data
        self.index = 0
    def __iter__(self):
        return self    def next(self):   #Use __next__ in python 3.x
        if self.index < len(self.list_data):
            val = self.list_data[self.index]
            self.index += 1 
            return val        else:            raise StopIteration()
我们来用`list_iter`自己定义一个列表迭代器

class List(object):
    def __init__(self, val):
        self.val = val    def __iter__(self):
        return list_iter(self.val)
>>> ls = List([1,2,34])>>> it = iter(ls)>>> next(it)1>>> next(it)2>>> next(it)34>>> next(it)

Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    next(it)
  File "<pyshell#228>", line 13, in next
    raise StopIteration()
StopIteration
xrange
从一个问题开始——xrange是迭代还是迭代器？

我们来看看

>>> x = xrange(10)>>> type(x)
>>> <type 'xrange'>
>>> 几个关键点：

1. `iter(xrange(num))`应该被支持

2. 如果`iter(xrange(num))`返回同样的对象（xrange类型）那xrange就是迭代器

3. 如果`iter(xrange(num))`返回一个迭代器对象那xrange就是迭代

>>> iter(xrange(10))
>>> <rangeiterator object at 0x0264EFE0>
>>> 它返回了rangeiterator，所以我们完全可以叫它迭代器。

让我们用最少的xrange函数实现自己的xrange

xrange_iterator
class xrange_iter(object):
    def __init__(self, num):
        self.num = num
        self.start = 0
    def __iter__(self):
        return self    def next(self):
        if self.start < self.num:
            val = self.start
            self.start += 1
            return val        else:            raise StopIteration()
my xrange
class my_xrange(object):
    def __init__(self, num):
        self.num = num    def __iter__(self):
        return xrange_iter(self.num)
>>> for x in my_xrange(10):	print x,0 1 2 3 4 5 6 7 8 9
>>> 我喜欢在这里总结这篇文章，欢迎发表评论和疑问。


作者：喵喔喔
链接：https://www.imooc.com/article/34306
来源：慕课网

## python的迭代器



## python的生成器

```python 
(i for i in range(1,10))
```





## python中的yield关键字

return 返回

yield 产出



3. (译)Python关键字yield的解释(stackoverflow)
   译者:hit9
   原文:http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained
   译者注:这是stackoverflow上一个很热的帖子，这里是投票最高的一个答案
   Contents

(译)Python关键字yield的解释(stackoverflow)
提问者的问题
回答部分
可迭代对象
生成器
yield关键字
回到你的代码
控制生成器的穷尽
Itertools,你最好的朋友
了解迭代器的内部机理
3.1. 提问者的问题
Python关键字yield的作用是什么？用来干什么的？

比如，我正在试图理解下面的代码:

def node._get_child_candidates(self, distance, min_dist, max_dist):
    if self._leftchild and distance - max_dist < self._median:
        yield self._leftchild
    if self._rightchild and distance + max_dist >= self._median:
        yield self._rightchild
下面的是调用:

result, candidates = list(), [self]
while candidates:
    node = candidates.pop()
    distance = node._get_dist(obj)
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
return result
当调用 _get_child_candidates 的时候发生了什么？返回了一个列表？返回了一个元素？被重复调用了么？ 什么时候这个调用结束呢？

3.2. 回答部分
为了理解什么是 yield,你必须理解什么是生成器。在理解生成器之前，让我们先走近迭代。

3.3. 可迭代对象
当你建立了一个列表，你可以逐项地读取这个列表，这叫做一个可迭代对象:

>>> mylist = [1, 2, 3]
>>> for i in mylist :
>>> ...    print(i)
>>> 1
>>> 2
>>> 3
>>> mylist 是一个可迭代的对象。当你使用一个列表生成式来建立一个列表的时候，就建立了一个可迭代的对象:

>>> mylist = [x*x for x in range(3)]
>>> for i in mylist :
>>> ...    print(i)
>>> 0
>>> 1
>>> 4
>>> 所有你可以使用 for .. in .. 语法的叫做一个迭代器：列表，字符串，文件……你经常使用它们是因为你可以如你所愿的读取其中的元素，但是你把所有的值都存储到了内存中，如果你有大量数据的话这个方式并不是你想要的。

3.4. 生成器
生成器是可以迭代的，但是你 只可以读取它一次 ，因为它并不把所有的值放在内存中，它是实时地生成数据:

>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator :
>>> ...    print(i)
>>> 0
>>> 1
>>> 4
>>> 看起来除了把 [] 换成 () 外没什么不同。但是，你不可以再次使用 for i in mygenerator , 因为生成器只能被迭代一次：先计算出0，然后继续计算1，然后计算4，一个跟一个的…

3.5. yield关键字
yield 是一个类似 return 的关键字，只是这个函数返回的是个生成器。

>>> def createGenerator() :
>>> ...    mylist = range(3)
>>> ...    for i in mylist :
>>> ...        yield i*i
>>> ...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
>>> <generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
>>> ...     print(i)
>>> 0
>>> 1
>>> 4
>>> 这个例子没什么用途，但是它让你知道，这个函数会返回一大批你只需要读一次的值.

为了精通 yield ,你必须要理解：当你调用这个函数的时候，函数内部的代码并不立马执行 ，这个函数只是返回一个生成器对象，这有点蹊跷不是吗。

那么，函数内的代码什么时候执行呢？当你使用for进行迭代的时候.

现在到了关键点了！

第一次迭代中你的函数会执行，从开始到达 yield 关键字，然后返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。

如果生成器内部没有定义 yield 关键字，那么这个生成器被认为成空的。这种情况可能因为是循环进行没了，或者是没有满足 if/else 条件。

3.6. 回到你的代码
(译者注:这是回答者对问题的具体解释)

生成器:

Here you create the method of the node object that will return the generator

def node._get_child_candidates(self, distance, min_dist, max_dist):

Here is the code that will be called each time you use the generator object :

If there is still a child of the node object on its left

AND if distance is ok, return the next child

  if self._leftchild and distance - max_dist < self._median:
            yield self._leftchild
If there is still a child of the node object on its right

AND if distance is ok, return the next child

  if self._rightchild and distance + max_dist >= self._median:
                yield self._rightchild
If the function arrives here, the generator will be considered empty

there is no more than two values : the left and the right children

调用者:

Create an empty list and a list with the current object reference

result, candidates = list(), [self]

Loop on candidates (they contain only one element at the beginning)

while candidates:

    # Get the last candidate and remove it from the list
    node = candidates.pop()
    
    # Get the distance between obj and the candidate
    distance = node._get_dist(obj)
    
    # If distance is ok, then you can fill the result
    if distance <= max_dist and distance >= min_dist:
        result.extend(node._values)
    
    # Add the children of the candidate in the candidates list
    # so the loop will keep running until it will have looked
    # at all the children of the children of the children, etc. of the candidate
    candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))

return result
这个代码包含了几个小部分：

我们对一个列表进行迭代，但是迭代中列表还在不断的扩展。它是一个迭代这些嵌套的数据的简洁方式，即使这样有点危险，因为可能导致无限迭代。 candidates.extend(node._get_child_candidates(distance, min_dist, max_dist)) 穷尽了生成器的所有值，但 while 不断地在产生新的生成器，它们会产生和上一次不一样的值，既然没有作用到同一个节点上.
extend() 是一个迭代器方法，作用于迭代器，并把参数追加到迭代器的后面。
通常我们传给它一个列表参数:

>>> a = [1, 2]
>>> b = [3, 4]
>>> a.extend(b)
>>> print(a)
>>> [1, 2, 3, 4]
>>> 但是在你的代码中的是一个生成器，这是不错的，因为：

你不必读两次所有的值
你可以有很多子对象，但不必叫他们都存储在内存里面。
并且这很奏效，因为Python不关心一个方法的参数是不是个列表。Python只希望它是个可以迭代的，所以这个参数可以是列表，元组，字符串，生成器... 这叫做 duck typing,这也是为何Python如此棒的原因之一，但这已经是另外一个问题了...

你可以在这里停下，来看看生成器的一些高级用法:

3.7. 控制生成器的穷尽
```python
>>> class Bank(): # let's create a bank, building ATMs
...    crisis = False
...    def create_atm(self) :
...        while not self.crisis :
...            yield "$100"
>>> hsbc = Bank() # when everything's ok the ATM gives you as much as you want
>>> corner_street_atm = hsbc.create_atm()
>>> print(corner_street_atm.next())
$100
>>> print(corner_street_atm.next())
$100
>>> print([corner_street_atm.next() for cash in range(5)])
['$100', '$100', '$100', '$100', '$100']
>>> hsbc.crisis = True # crisis is coming, no more money!
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> wall_street_atm = hsbc.create_atm() # it's even true for new ATMs
>>> print(wall_street_atm.next())
<type 'exceptions.StopIteration'>
>>> hsbc.crisis = False # trouble is, even post-crisis the ATM remains empty
>>> print(corner_street_atm.next())
<type 'exceptions.StopIteration'>
>>> brand_new_atm = hsbc.create_atm() # build a new one to get back in business
>>> for cash in brand_new_atm :
...    print cash
$100
$100
$100
$100
$100
$100
$100
$100
$100
...
```
对于控制一些资源的访问来说这很有用。


3.8. Itertools,你最好的朋友
itertools包含了很多特殊的迭代方法。是不是曾想过复制一个迭代器?串联两个迭代器？把嵌套的列表分组？不用创造一个新的列表的 zip/map?

只要 import itertools

需要个例子？让我们看看比赛中4匹马可能到达终点的先后顺序的可能情况:


```python
>>> horses = [1, 2, 3, 4]
>>> races = itertools.permutations(horses)
>>> print(races)
<itertools.permutations object at 0xb754f1dc>
>>> print(list(itertools.permutations(horses)))
[(1, 2, 3, 4),
 (1, 2, 4, 3),
 (1, 3, 2, 4),
 (1, 3, 4, 2),
 (1, 4, 2, 3),
 (1, 4, 3, 2),
 (2, 1, 3, 4),
 (2, 1, 4, 3),
 (2, 3, 1, 4),
 (2, 3, 4, 1),
 (2, 4, 1, 3),
 (2, 4, 3, 1),
 (3, 1, 2, 4),
 (3, 1, 4, 2),
 (3, 2, 1, 4),
 (3, 2, 4, 1),
 (3, 4, 1, 2),
 (3, 4, 2, 1),
 (4, 1, 2, 3),
 (4, 1, 3, 2),
 (4, 2, 1, 3),
 (4, 2, 3, 1),
 (4, 3, 1, 2),
 (4, 3, 2, 1)]
```


3.9. 了解迭代器的内部机理
迭代是一个实现可迭代对象(实现的是 __iter__() 方法)和迭代器(实现的是 __next__() 方法)的过程。可迭代对象是你可以从其获取到一个迭代器的任一对象。迭代器是那些允许你迭代可迭代对象的对象。

更多见这个文章 http://effbot.org/zone/python-for-statement.htm




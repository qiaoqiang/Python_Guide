# python中的operator.itemgetter函数

operator.itemgetter函数
operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号。看下面的例子

a = [1,2,3] 
>>> b=operator.itemgetter(1)      //定义函数b，获取对象的第1个域的值
>>> b(a) 

2

>>> b=operator.itemgetter(1,0)  //定义函数b，获取对象的第1个域和第0个的值
>>> b(a) 
>>> (2, 1)

要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

sorted函数用来排序，sorted(iterable[, cmp[, key[, reverse]]])

其中key的参数为一个函数或者lambda函数。所以itemgetter可以用来当key的参数

a = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

根据第二个域和第三个域进行排序

sorted(students, key=operator.itemgetter(1,2))
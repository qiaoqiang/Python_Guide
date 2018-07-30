 class A(object):  
        def kkk(self,x):    #实例方法，类和实例都能访问  
            print(self,x)  
        @classmethod    #加上这句后 classKkk就成为了类方法，类和实例都可以访问，  
        def classKkk(cls,x):  
            print(cls,x)  
        @staticmethod   #加上这句就成为了静态方法，类和实例都可以访问。  
        def staticKkk(x):  
            print(x)  
        def mmm(x):     # 这是无敌普通函数  
            print(x)  
    A.classKkk(2)  
    #   <class '__main__.A'> 2 这里类A可以直接访问类方法classKkk，但是不能访问实例方法kkk（会报错的）。  
    A.kkk(A,1)  #<class '__main__.A'> 1 类要访问实例方法需要加入参数,至于这个参数可以是A也可以是A()  
    A.staticKkk(3)  #   3 这里类A也可以访问静态方法staticKkk，  
    A.mmm(3) #  3 对象可以访问无敌普通函数  
    a = A()  
    a.kkk(5)    # <__main__.A object at 0x0000028A64394CC0> 5 实例访问实例方法，没毛病  
    a.classKkk(6)   #   <class '__main__.A'> 6 实例访问类方法，没毛病  
    a.staticKkk(7)  #   7  
    a.mmm(7)    # 报错，实例不能访问普通函数  
      
 
    # 总结：实例方法和类方法一定要传入参数，a.kkk(x)相当于kkk(a,x)，第一个参数必须是实例本身。
    # 类方法也是如此，但是静态方法不用传入参数，此外普通函数只有类能访问，对象不能访问

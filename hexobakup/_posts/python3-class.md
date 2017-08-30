---
title: python3 class
date: 2017-01-15 20:06:40
tags:
- python
categories:
- Tech
- Note
- Code
---
在折腾django，发现wtf我真的学过python?赶紧复习一波python的class。
<!-- more -->
```python
class Person:
    """A simple class"""
    age = 18
    def name(self):
        return 'sally'

sally = Person()
```
构造简单类Person,创建**对象**sally

```python
class Complex:
    numtype = "complex" # class attr shared by all instances
    # sharing class variables like list[] will cause mutiple pointers
    def __init__(self, realpart ,imagpart): # similar to constructor in cpp
        self.r = realpart # instance attr
        self.i = imagpart # instance attr

x = Complex(3.0,-4.5)
print(x.r,x.i,x.numtype)
# 3.0 -4.5 complex
y = Complex(5,9)
print(y.r,y.i,y.numtype)
# 5 9 complex

```
private and public variables 
from **segmentfault**

```python
class A(object):
        def __init__(self):
            self.__private()
            self.public()
        
        def __private(self):
            print('A.__private()')
        
        def public(self):
            print('A.public()')

class B(A):
        def __private(self):
            print('B.__private()')
       
        def public(self):
            print('B.public()')

b=B() # 创建一个B的实例
```
result:
`A.__private()` 调用的时候是在class A中 所以打印出的是A.__private() 
`B.public()`

类的多重继承**"depth-first, left-to-right"**

```python
class A:  
    def test(self):  
        print("in A...")  
  
          
class B(A):  
    def test(self):  
        print('in B...')  
  
          
class C(A):  
    def test(self):  
        print('in C...')  
  
          
class D(B,C):  
    def test(self):  
        print('in D...')  
  
          
d = D()  
d.test() #如果子类拥有该方法，那直接调用该方法  
# in D...  
class D(B,C): #重定义类D  
    pass  
  
d = D()  
d.test() #B先继承，在B中首先找到该方法，调用B的方法  
# in B...  
class D(C,B): #再次重定义，改变了继承顺序  
    pass  
  
d = D()  
d.test() #这次调用了C的方法  
# in C...  
```

湿兴大发
```python
class Person(object):
    species = "human"
    immortal = False
    needfood = True
    needwater = True

    def show_species(self):
        print(self.species)

class Woman(Person):
    has_beauty = True
    need_care = True
        
class Sally(Woman):
    def __init__(self): # 当已经子类已经有初始化方法，将不会再自动调用父类的方法！若没有init才递归调用父类的init!
        self.name = "Sally"
        self.__age = 18 # cannot be directly modified
        self.__world_best_girl = True # cannot be directly modified
        self.__lover = "Jeff" # cannot be directly modified
        self.life()
    
    def get_name(self):
        print("Sally")
    
    def life(self):
        while (True): # after initialize, loop forever
            print("Jeff loves Sally")
            print("Jeff loves Sally")
            print("Jeff won't be late any more")

sally = Sally()

print(sally.name)
print(sally._Sally__lover) # lover is private so cannot call directly
print(sally.species) # inherit from Person class
sally.show_species()
print(sally.has_beauty) # inherit from Woman class
print(sally._Sally__world_best_girl) # special instance attribute!

```
Python Notes
======

References
> https://www.toptal.com/python/interview-questions

---- 

[1. 基础](#1)

　[1.1 二级目录](#1.1)


<h2 id='1'> 1. 基础 </h2>



<h3 id='1'> 1.1 What will be the output of the code below? Explain your answer. </h3>
    
    def extendList(val, list=[]):
        list.append(val)
        return list
    
    list1 = extendList(10)
    list2 = extendList(123,[])
    list3 = extendList('a')
    
    print "list1 = %s" % list1
    print "list2 = %s" % list2
    print "list3 = %s" % list3



**Answer:**

The output of the above code will be:

    list1 = [10, 'a']
    list2 = [123]
    list3 = [10, 'a']

Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

<u>However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. </u><strong>This is because expressions in default arguments are calculated when the function is defined, not when it’s called.</strong>

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

    def extendList(val, list=None):
      if list is None:
        list = []
      list.append(val)
      return list
With this revised implementation, the output would be:

    list1 = [10]
    list2 = [123]
    list3 = ['a']

 


__________________


<h3 id='1'> 1.2 What will be the output of the code below? Explain your answer. </h3>
    
    def multipliers():
      return [lambda x : i * x for i in range(4)]

    print [m(2) for m in multipliers()]

**Answer:**

The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6]).

The reason for this is that Python’s closures are This is an [late binding](https://en.wikipedia.org/wiki/Late_binding). This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by 3, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

(Incidentally, as pointed out in The Hitchhiker’s Guide to Python, there is a somewhat widespread misconception that this has something to do with lambdas, which is not the case. Functions created with a lambda expression are in no way special and the same behavior is exhibited by functions created using an ordinary def.)

Below are a few examples of ways to circumvent this issue.

One solution would be use a Python generator as follows:

    def multipliers():
      for i in range(4): yield lambda x : i * x 
Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:

    def multipliers():
      return [lambda x, i=i : i * x for i in range(4)]
Or alternatively, you can use the functools.partial function:

    from functools import partial
    from operator import mul

    def multipliers():
      return [partial(mul, i) for i in range(4)]


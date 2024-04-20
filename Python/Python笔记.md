# Python 笔记

## 目录

- [输入输出](#输入输出)
- [数据类型和变量](#数据类型和变量)
- [选择循环](#选择循环)
- [序列](#序列)
    - [list tuple](#listtuple)
    - [dict set](#dict字典)
    - [字符串](#字符串)
- [其他结构](#其他结构)
- [函数](#函数)
- [高级特性](#高级特性)
- [模块](#模块)
- [类与对象](#类与对象)
- [继承和多态](#继承和多态)
- [异常](#异常)
- [File](#File)

## 输入输出

- Python遇到未闭合的小括号，自动将多行字符串拼接为一行
- `exit()=quit()`
- `python --version`
- `>>> ...`（等待，两次回车结束） 
- `help(obj)`
- `print(seq = ' ', end = '\n')`
- `name = input("提示字符串")` 
- `\`续行，包括字符串或一般语句
- `#`行注释，三引号块注释
- 选用`;`分隔语句
- `# -*- coding: UTF-8 -*-`  
    `# coding:UTF-8`
```py
if __name__ == "__main__":
    main()
```

## 数据类型和变量

- False:0、None、空字符串、空list等
- 短路逻辑运算规则：
    - 表达式从左往右运算，如果or的左侧逻辑值为 true，则短路or后面的所有表达式（无论后面是and还是or等），直接输出or左侧表达式；如果or左侧的表达式逻辑值为false，则输出or后面的表达式，且不论后面表达式的真与假。
    - 表达式从左往右运算，如果and左侧逻辑值为false，则短路and后面所有表达式，直到有or出现，输出and左侧表达式到or的左侧，参与接下来的逻辑运算。
    - 如果or的左侧为false，或者and的左侧为true，则不能使用短路逻辑。
- 长数字`_`分隔
- `float("inf")`
- `type(var)` ,print为`<class 'type'>`  
- `del var` 删除（垃圾回收）  
- 赋值：都是引用（地址）传递
- 运算符：
    - tuple赋值`var1, var2 = a, b`
    - `/`结果一定是浮点数，`//`、`%`、`**`、`+=`
    - `1<var<2`
    - `id(var)` 返回内存地址
    - `var1 is/is not var2` 判断是否指向同一地址（浅相等）
        - `==`值是否相等（深相等）

## 选择、循环
```python
[(1,3),(2,4)]=list(zip([1,2],[3,4]))
[res1,...]=list(map(func,[arg_a1,...],[arg_b1,...]))
dict=vars(obj) # 调用__dict__()返回 属性-值
x, y = zip(*sorted(zip(x, y))) # (x,y)排序

if bool:
elif bool:
else:

assert bool,"..."

while bool:

for var in iterable:
break continue

range(init=0,final,step=1) # 不包括final
```

## 序列

- 运算：+连接，*重复N次，==判断顺序和项目是否都相等
- `item in/not in infos` 成员判断返回bool
- slice切片：
    - 用于str,list,dict
    - 下标0~len-1，负索引-1开始，越界就IndexError异常
    - start_index < end_index包括负索引  
        end_index对应元素不被取出，包括负索引（最后元素负索引-1）
    - `infos[start_index:end_index:step]`  
        步长默认1，不取出end_index  
        `infos[start_index:end_index]` 省略下标表示到末尾，见Matlab
    - 可作为左值被赋值，长度可变，删除为`del`
    - 左闭右开，方便spilt直接写划分的数目（1k/5k，则0:1000,1000:end）

序列统计函数：

        len() max() min() sum()  
        any(item) all()确认元素多少为True，返回bool  

### list,tuple

list列表：

- 可变长度，元素类型可不同，可以是list（多维数组）
- 空列表[]
- 方法：

            append(item) insert(index,item)
            pop([index]) remove(item)
            extend(list)
            index(item) count(item)
            copy()地址不同，浅拷贝
            sort()方法针对list，直接修改原list sorted()函数针对iterable，新建list reverse()

tuple元组

- 内容不许修改，否则TypeError异常，但创建时可用+、*运算 `infos=(...,...)`
- tuple的每个元素指向不变。若指向list则list元素可变
- 1个元素的tuple：infos = (1,)

相互转换：list() tuple()

### dict字典

- 无序Hash表
- key可以是数字、字符串、元组、None
- key重复表示覆盖
- example
    ```python
    infos = {'a': 95, 'b': "cm" ,None:"123"}  
    infos['a']=95
    infos['d']=3 # 可以直接append
    infos = dict(key1=val1,...) # key自动转为字符串
    infos = dict([[key1,value1],[key2,value2],...])
    ```
- list转换：`info = dict(zip(list_a,list_b))`
- iteration迭代：
    ```py
    for key in infos
    for key,value in infos.items()
    ```
- 方法：

        items() keys() values()
        item=get(key[,defaultvalue])
        clear() update({k=v,...})动态扩充替换
        pop(key) popitem()弹出最后一项
        setdefault(key, default=None) 返回key对应value，否则创建key并设置为default

### set集合

- 无序，value不重复否则覆盖
- 创建空集合：set()
- 和dict一样可以用enumerate迭代，但是无序
- example
    ```py
    infos = {value1,value2,...}
    infos = set(seq) # seq为某序列
    ```
- 方法：

        add() pop() clear() remove()
        差集- 交集& 并集| 对称差集（并集减交集）^ 子集<=

### 字符串

- 内容不可修改。
- 单双引号等价，二者互相可括就不用转义。`r'...'`不转义
- 转义：`\0yy`为八进制yy-ASCII，`\xyy`为十六进制yy-ASCII，`\uyyyy`为十六进制
- 三引号：是单引号双引号都行，保留换行空格等原始信息
- 格式化字符串：
    - 传统：`"%d...%c"%(val1,val2)` 一个参数括号可省  
    - format:
        - `"{} {}".format("hello", "world")`
        - `"{:.2f}".format(1.125)`
    - `f"Hello, my name is {name:5s}"`
- 编码
    ```py
    b'ABC' = 'ABC'.encode('ascii') # bytes-UTF
    'ABC' = b'ABC'.decode('ascii') # str-Unicode
    int=ord() str=chr()
    hex() oct() bin() # 返回str类型
    ```

方法：

        center(len)居中 ljust(len) rjust(len)对齐 strip()删除左右空格
        idx=find(item)找不到索引为-1 count(item)
        ','.join('abc')='a,b,c'  ''.join(['a','b'])='ab'
        split(item[,limit])拆分为列表
        lower() upper() capitalize()
        replace(old,new[,limit]) new=''表示删除
        endswith('.wav')结尾字符串

## 其他结构

- deque双端队列
    - 前端为first后端为last
    ```py
    from collections inport deque
    var = deque(seq) # 创建
    # 方法：
    append()后端 appendleft()前端 clear() count() pop()前端 popleft()后端 remove() reverse()
    ```
- heapq堆
    ```py
    import heapq
    heapq.heapify(iterable) # 创建，iterable就是heap对象了
    # 方法：
    heapq.heappush(heap,element)保存  
    heappop(heap)弹出最小值  
    heappushpop(heap) heapreplace(heap)  
    nlargest(n,heap)前n个最大值 nsmallest(n,heap)
    ```
- enum枚举
    ```py
    import enum
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    ```
- OrderedDict有序字典
    ```py
    from collections import OrderedDict
    new_dict = OrderedDict()
    ```

## 函数

- pass语句
- 函数名：type为function区别于method和builtin函数方法，可赋给其他变量`var=func`，`var()`调用
- return
    - 遇到return立即结束  
    - `return None`等同`return`等同没有return
    - **建议写return返回，不要改参数的值作为返回**
- 函数参数
    - 默认参数：参数后加`=default`如`=None`  
        必须指向不变对象（定义函数时地址确定，函数不同时间调用返回结果不同）
    - 命名关键字参数：`*`后参数调用时必须指明名称`(...,*,a,...)`
    - 可变参数：`*`修饰的参数，数量可变，函数体视为tuple序列。相当于把list参数拆开成一个个。  
        传参时要拆分list为可变参数，在list前加*即可。
    - 关键字参数：`**`修饰的参数，key=value方式传入任意个参数，函数体视为dict用items方法。相当于把dict参数拆开成一个个。  
        传参时要拆分dict加`**`即可。
    - 顺序：必选，默认，可变，命名关键字，关键字  
        命名关键字参数在可变参数后面就不用再*
- 说明注释`__doc__`
    ```py
    '''
    description
    :param var_a: ...
    :return: ...
    '''
    ```
- 变量作用域
    - 函数体定义的为局部变量，声明global var使用全局变量
    - `globals() locals()` 用dict返回环境全局变量、局部变量
- closure闭包：
    - 外函数嵌套定义内函数，外函数返回内函数名引用，此时外函数环境（参数）被保存
    - nonlocal在内函数修饰外函数参数
- 匿名函数：`sum = lambda x,y : x + y;`  
    可以用作自己写的函数的部分返回值的函数提取
- 内置函数：

    callable(obj) compile()提前编译
    eval(str[,var])解析表达式并返回值，var为dict表示的变量(namespace)
    exec(str) 解析多语句返回None，str通过"...:"\"    ..."换行

- 参数检查：
    ```py
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    ```

## 高级特性

1. decorator装饰器：在函数前快速增加内容，不改变函数定义和调用名
    - 无参装饰器：
        ```py
        def log(func):
            def wrapper(*args, **kw):
                print('call %s():' % func.__name__)
                return func(*args, **kw)
            return wrapper
        # 调用处：
        @log
        def now():...
        相当于now = log(now)
        ```
    - 有参装饰器
        ```py
        def log(text):
            def decorator(func):
                def wrapper(*args, **kw):
                    print('%s %s():' % (text, func.__name__))
                    return func(*args, **kw)
                return wrapper
            return decorator
        # 调用处
        @log('execute')
        相当于now = log('execute')(now)
        ```
    - 基于类：在__call__()方法中定义，修饰函数
    - 函数.`__name__ , __doc__`等属性被内嵌套函数信息覆盖：wraps
        ```py
        from functools import wraps
        在wrapper函数定义前加@wraps(func)，其他一致
        ```
    - wrapt模块：无参
        ```py
        import wrapt
        @wrapt.decorator
        def logging(wrapped,instance,args,kwargs):
            print...wrapped.__name__
            return wrapped(*args,**kwargs)
        ```
2. 内置装饰器
    - 静态方法：调用类方法不用创建实例，无法访问类和对象的数据
        ```py
        @staticmethod
        def get_info():...注意没有self
        调用：Class.get_info()
        ```
    - 类方法：必须有一个接受当前类的参数，可调用类属性，或创建实例调用method。
        ```py
        @classmethod
        def get_info(cls):
            cls().hello()
        调用：Class.get_info()
        ```
    - property属性访问：不用设计setattr()、getattr()方法访问属性，把方法包装成属性，让方法可以以属性的形式被访问和调用
        ```py
        class Student:
            def get_age(self):
            def set_age(self, age):
                self._age = age
            def del_age(self):
            age = property(fget=get_age, fset=set_age, fdel=del_age, doc='学生年龄') # property函数
        student = Student()
        print(student.age.__doc__)

        class Student:
            @property
            def age(self): # 访问
            @age.setter
            def age(self,age): # 设置
            @age.deleter
            def age(self): # 删除
        ```
- list comprehensions列表生成式
    ```py
    [x * x for x in range(1, 11)]
    [x*x for x in range(1, 11) if x % 2 == 0]
    [x if x % 2 == 0 else -x for x in range(1, 11)]
    # 双变量
    [m+n for m in 'ABC' for n in 'XYZ']
    [print(i) for y in y_list for i in y]
    # dict comprehension
    {x: x ** 2 for x in nums if x % 2 == 0}
    # set comprehension
    {int(sqrt(x)) for x in range(30)}
    ```
- iterator迭代器：取出来的数据就不存在了
    ```py
    it = iter([1,2,3]) # __iter__(): return iterable or return self(using __next__())
    next(it) # __next__(): raise StopIteration
    from collections.abc import Iterable
    isinstance('abc', Iterable)
    ```
- generator生成器:返回iterator
    ```py
    # define 1
    g = (x * x for x in range(10))
    # define 2: Fibonacci
    def fib(max):
        n, a, b = 0, 0, 1
        while n < max:
            recv = yield b
            a, b = b, a + b
            n = n + 1
        return 'done'
    g = fib(10)
    ```
    - 调用`next(g)`执行到yield返回并保存。函数结束（return或代码段末尾）就StopIteration。
    - `generator.send(...)`先给上一次输出的yield的recv发送消息并找到下一个yield返回
    - `yield from iterable = for item in iterable: yield item`可迭代对象显式变为生成器

- contextlib模块：
    1. 和with连用：

            from contextlib import contextmanager
            @contextmanager修饰generator函数

        在函数内（不是类）yield作为__enter()和__exit__()分界线
    2. x

            from contextlib import closing
            with closing(Class()) as ...:...自动调用close()方法

    3. with supress(异常类):...压制异常
    - 调用：

            o = odd()创建一个generator对象
            next(o)
            而next(odd())生成多个generator对象，只返回第一个值

    - 得到return返回值：捕获StopIteration异常，在obj.value

## 模块

- module模块：.py程序文件  
- package包：名称空间，本质是文件目录，包括若干.py文件。父级关系加`.`
- usage
    ```py
    import package.module[as alias],...
    from package import module
    from package.module import obj[as alias],...
    # 在程序中调用的是import后面的称呼
    print(module)输出模块路径
    dir(module)查看模块的obj，返回list
    ```
- `__import__('module')`动态导入
- 模糊导入：obj为通配符*引入所有结构（但不自动导入_变量，而import引入模块不行）
- 模块中函数外的代码也会被执行
- 特殊变量（public直接访问）：

        __init__.py：空文件：标识包还是目录；内容：去别名；__all__=['module']控制模糊导入*的模块
        __name__为模块名，但运行的程序改为__main__
        __doc__：模块第一个字符串为文档注释。

- `_x,__x`:private非公开访问，前者告知程序员后者由解释器重命名
- 自定义模块名和系统模块名重合会覆盖
- 系统模块
    ```py
    # functools.partial偏函数重新封装
    b=functools.partial(a,arg1,arg2)则调用函数b()=>a(arg1,arg2) # 有时也可以考虑用匿名函数
    # random
    random()0~1 uniform(x,y)x~y randint(x,y)整数
    choice(seq)随机抽一个数 randrange() shuffle() sample()
    ```
        
## 类与对象

1. class,instance：
    - 特性：封装性（属性行为为整体、隐蔽-隐藏细节、权限保护）、继承性、多态性
    - `dir(obj/Class)`查找类所有属性方法
2. 声明：
    - 类名首字母大写
    - `__var`私有属性（本质上改名`bart._Student__var`）
    - 析构方法`__del__`在del和抛弃时调用
    - 类属性
        - 所有实例中共享，可通过实例或类调用
        - 在方法里`Student.info`而不是`self.info`
        - 和实例属性重名则用实例属性覆盖，直到被删除
4. 匿名对象：`Student().fun` 使用一次就释放
5. `__slot__`限制实例属性范围：类属性`__slots__ = ('var1','var2')`否则发生AttributeError异常
6. 内部类：
    - 可在外部类内外使用，但是调用时都要说明父级关系`Message.Connect()`
    - 封装保护：用`__`定义 class `__Connect:...`
    - 内部类不能直接使用外部类成员，还需传递外部类实例参数
    - 还可以再外部类的方法中定义，访问方法局部变量、参数
8. 特殊方法（继承object类得到的）：调用方法监听
    - 对象

            __str__()用于print(obj)
            __gt__() __eq__() __add__()运算符
            __call__()用于obj()
            __getitem__用于obj[idx]

    - 属性控制

            __getattribute__(self, attr: str)属性拦截操作
            __set/get/delattr__()属性
            vars()调用__dict__()返回实例属性dict
            __init_subclass__()父类了解子类创建实例时调用

    - 序列操作（序列内容是类）

            iteration:__iter__() __next__()
            reversed():__reversed__()
            dict:__set/get/delitem__() __len__() __contains__

9. 属性控制函数：`getattr(object,name: str[,default])、setattr()、hasattr()`

## 继承和多态

1. 继承：
    - 一个子类可有多个父类
    - 构造方法：子类没有时按顺序调用父类无参构造方法；  
        子类有时不调用父类但可以手动调用`super().__init__()`
    - 多继承：method resolution order判断调用构造方法顺序，广度优先  
        检查MRO:类名.mro() 返回list
    - 继承信息：
        - obj.__class__实例对应类 issubclass(Sub,Base) 
        - `Class.__subclasses__() Class.__bases__` 返回list/ tuple
        - isinstance(obj,Class) 包括父类判断(比type好)。Class可以为tuple表示
2. 多态：接口，要求子类按照父类标准覆写方法，"开闭"原则
    - 方法覆写：方法名、返回值类型、参数类型和个数完全相同
    - 调用覆写前父类方法：super().fun()
    - object类为所有类的父类，默认继承
    - 设计模式：工厂函数返回实例对象（主函数只关心父类提供标准，子类对象封装隐藏）、代理（辅助且完成核心工作）
3. 动态语言的方法参数时任意类："鸭子类型"，配合isinstance()使用

## 异常

- 错误码：返回-1，层级上报
- 异常处理
    - ```python
        try:
            r = 10 / 0
        except ZeroDivisionError as obj:
            print(obj)
        except:...
        else:
            ...
        finally:
            ...
        ```
    - 解释器遇到异常会实例化异常类对象，与except比对。执行完finally判断异常是否处理了
    - 跨层捕获（调用栈）
- 异常类继承
    - `objectBaseException`（Python全部异常父类）`Exception`（程序中处理的异常父类）`ValueError`, `ArithmeticError`
    - 父类可以捕获子类异常
    - traceback模块：详细异常情况
    - 自定义异常类：继承`Exception`类,`__init__()`在raise调用，`__str__`print输出
- raise
    - `raise ExceptionClass()`抛出异常，可用于父类不提供方法实现，要求子类覆写
    - 异常类可以自定义。可以是已有的：
        - 放在except里raise，try的异常被放到except里raise异常的__cause__属性里
        - 不附加__cause__：except的raise后加from None

- with：`with ... as var: ...`
    - 对with后语句求值（如Class()）调用`__enter__(self)`方法且把返回值给var，之后执行with块语句。遇到异常或执行完，调用`__exit__()`方法结束
    - `__exit__(self,type,value,trace)`后三参数提供异常信息

- 记录错误
```py
import logging
logging.exception(obj)
```

## File

```py
filename = "runoob.txt"
fo = open(filename, "w")
str = fo.read() fo.readline() fo.readlines() # 都返回str（包括\n），但readlines转换成list每个元素为一行str
fo.name # 文件名
fo.write(str)
fo.close()

with open("file_path","r") as f:
    str = f.read()
    for line in f: # line include '\n', so using .strip()
        feature, label = line.strip().split(',')
```

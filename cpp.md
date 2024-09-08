# cpp

## TOC



## command
- `$ g++ -v` 检查gcc版本
- `g++ main.cpp -o <exe_name>` 指定可执行文件名
- `g++ main.cpp a2.cpp -o <exe_name>` 多文件
- -g调试信息 -Wall生成所有警告 -std=c++11新标准
- `system("pause");` 防止闪屏

## common
- `typedef type newname;`
- `enum color { red, green=5, blue } c;`
- 结构体
    - `struct Books{char title[50];} book;`
    - `Books book1;`
    - `void printBook( struct Books book );` 多一个struct
- 声明
    - `extern int a, b;` 变量声明，声明多次定义一次，多文件声明
    - static在函数中为堆，文件中仅文件使用
- `const type variable = value;`
    - `int* const demo = &var` 指针变量不变
    - `const int *demo = &var` 指针指向变量值不变
- 字符串
    - ""中间用\分行
    - string类: `string str1 = "runoob"; str1.size(); str1+str2;`
- 数组
    - `double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};`
    - `p = balance; *(p+1)` 指向下一个元素
    - `void myFunction(int param[])` 函数参数
- vector 动态增长，连续存储
    - `#include<vector>`
    - `std::vector<int> myVector(5,10);`5个int，初始值为10
    - `std::vector<int> myVector={1,2,3};`
    - `.push_back(element) .at(index) .size() .erase(myVector.begin() + 2) .clean()`
    ```cpp
    // iterator
    for (auto it = myVector.begin(); it != myVector.end(); ++it) {
        std::cout << *it << " ";
    }
    // range
    for (int element : myVector) {
        std::cout << element << " ";
    }
    ```
- 指针
    - NULL 空指针为0
    - `if(ptr)` 判断是否为空
    - 指针减法：之间的元素个数
    - 统一数组内可比较大小，判断前后顺序
- 动态分配
    - `int* myArray = new int[3];` 三元素数组
    - `delete[] myArray;`
- 引用：创建时初始化，不会改变
    - `int&  r = i;`
    - 用作函数返回值时，作为左值赋值

## function
- `void swap(int &x, int &y)` 引用调用，调用时和函数内当普通变量
- `int sum(int a, int b=20)` 指定默认值
- `[](int x, int y) -> int { int z = x + y; return z + x; }` Lambda表达式

## class
```cpp
class Box
{
    public:
        double length,breadth,height;
        double get(void); // 函数声明，也可以直接在这里定义
        Box(double len); // 构造函数
        ~Box(); // 析构函数
    protected: // 在派生类可以访问
    private: // 不声明默认private。只有本类和友元函数可以访问私有成员
};

double Box::get(void)
{
    return length * breadth * height;
}

Box:Box(double len,double hei): length(len),height(hei) // 初始化列表，替代函数内的初始化赋值
{
    cout << "Hello" << endl;
    length = len;
}
Box:~Box(void)
{
    ...
}

Box box1(10.0);
box1.length // 访问public成员

class SmallBox:Box // SmallBox 是派生类
{
   public:
      void setSmallWidth( double wid );
      double getSmallWidth( void );
};
class B : public A{...} // public继承
```
- 

## package
- cmath: sin,abs,pow
- ctime: `(unsigned)time(NULL)` 系统时间，单位为秒
- cstdlib
    - rand: `srand((unsigned)time(NULL)); j=rand();`
- cstring: strcpy,strlen,strcat

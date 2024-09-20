# c++

## TOC
- [command](#command)
- [common](#common)
- [function](#function)
- [class](#class)
- [inheritance](#inheritance)
- [IO](#IO)
- [exception](#exception)
- [package](#package)


## command
- `$ g++ -v` 检查gcc版本
- `g++ main.cpp -o <exe_name>` 指定可执行文件名
- `g++ main.cpp a2.cpp -o <exe_name>` 多文件
- -g调试信息 -Wall生成所有警告 -std=c++11新标准
- `system("pause");` 防止闪屏
- `exit(1)` 提前退出

## common
- `typedef type newname;`
- `enum color { red, green=5, blue } c;`
- cout格式化
    - `cout << setw(2) << endl` 设置空格宽度
    - `cout << fixed << setprecision(3) << float_num` 固定浮点数小数位
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
- 动态内存
    - `int* myArray = new int[3];` 三元素数组
    - `delete[] myArray;`
- 引用：创建时初始化，不会改变
    - `int&  r = i;`
    - 用作函数返回值时，作为左值赋值
- 名称空间
    - `namespace <name> { // 代码声明 }` 可以嵌套定义。不连续定义时跨文件仍然需要前缀声明。
    - `using namespace <name>`
    - `using std::cout` 使用cout不用std修饰
    - `::a` 表示局部同名变量存在时的全局变量

## function
- `void swap(int &x, int &y)` 引用调用，调用时和函数内当普通变量
- `int sum(int a, int b=20)` 指定默认值
- `[](int x, int y) -> int { int z = x + y; return z + x; }` Lambda表达式

## class
```cpp
class Box
{
    public:
        double length,breadth,height,width;
        static int objectCount; // 静态成员，类的所有对象共用，不能在类定义中初始化
        double get(void); // 函数声明，也可以直接在这里定义
        // 类中定义函数为inline内联函数
        Box(double len); // 构造函数
        Box(const Box &obj); // 拷贝构造函数，有指针变量或动态内存分配
        ~Box(); // 析构函数
        static int getCount() // 静态成员函数，没有this指针，没有对象就能调用，可访问其他静态成员
        {
            return objectCount;
        }
        friend void printWidth( Box box ); // 友元函数，不是成员函数但可以访问protected和private，没有this指针
        friend class ClassTwo; // 声明类 ClassTwo 的所有成员函数作为友元
    protected: // 在派生类可以访问
    private: // 不声明默认private。只有本类和友元函数可以访问私有成员
        int *ptr;
};
// 成员函数
double Box::get(void)
{
    return length * breadth * height;
    return this->length;
}
// 友元函数
void Box::printWidth(Box box)
{
    cout << width << endl;
}
// 构造函数
Box:Box(double len,double hei): length(len),height(hei) // 初始化列表，替代函数内的初始化赋值
{
    cout << "Hello" << endl;
    length = len;
    ptr = new int;
    *ptr = len;
}
Box:~Box(void)
{
    delete ptr;
}
Box::Box(const Box &obj) // obj用于初始化另一个对象
{
    ptr = new int;
    *ptr = *obj.ptr;
}

int Box::objectCount=0;
cout << Box::getCount();
Box box1(10.0);
box1.length // 访问public成员
```

## inheritance
```cpp
// 继承：is-a
class SmallBox: public Box, public Box2// SmallBox 是派生类，多继承
{
   public:
      SmallBox(int a=0, int b=0):Box(a,b) {} // 继承的构造函数
      void setSmallWidth( double wid );
      double getSmallWidth( void );
};
// 函数重载：根据函数参数类型和顺序，上下文决定使用哪个同名函数
// 运算符重载
Box operator+(const Box&); // 成员函数时
Box operator+(const Box&, const Box&); // 非成员函数需要两个参数
// 多态：在基类加virtual为虚函数，在派生类多态此函数，实现动态链接
virtual int area() = 0; // 纯虚函数，没有函数主体
```

## IO
```cpp
#include<iostream>
#include<fstream>
// 写
ofstream outfile("abc.txt"); // 直接构造
ofstream outfile;
outfile.open("file.dat", ios::out | ios::trunc ); // 第二个参数可省略: trunc清除再写 ios::app追加
// 读
ifstream infile;
infile.open("file.dat", ios::in );
// 关闭
infile.close()
// 读写
outfile << data << endl;
infile >> data;
```

## exception
```cpp
try
{
   // 保护代码
   throw "Division by zero!";
}catch(const char* msg)
{
    cerr << msg << endl;
}catch( ExceptionName e2 )
{
   // catch 块
}catch( ... ) // 任意异常
{
   // catch 块
}
```

## package
- cmath: sin,abs,pow
- ctime: `(unsigned)time(NULL)` 系统时间，单位为秒
- cstdlib
    - rand: `srand((unsigned)time(NULL)); j=rand();`
- cstring: strcpy,strlen,strcat

# MATLAB

## TOC
- [basis](#basis)
- [plot](#plot)
- [string](#string)
- [符号计算](#符号计算)
- [线性代数数据拟合](#线性代数数据拟合)
- [数值微分积分](#数值微分积分)
- [优化工具箱](#优化工具箱)
- [随机变量模拟](#随机变量模拟)

## basis
- basis
    ```matlab
    % F5执行程序
    clear  clear a b   clc
    who   whos a b 显示size  class(var)
    save("results.mat", "var_G", "var_C");
    help funname
    pause(seconds)
    tic ... toc % elapsed time
    % 长语句末尾...后换行
    ```
- control structure
    ```matlab
    if 逻辑表达式1  语句块1 elseif else end
    switch switch_expr(一般为标量或字符串)
        case case_expr,  语句块1
        case {case_expr1, case_expr2, case_expr3,...},  语句块2
        otherwise,  语句块3
    end
    for x=[1,3,5,4] 语句块 end
    while 逻辑表达式  循环语句块  end
    ```
- useful functions
    ```matlab
    zeros(m,n)   ones(m,n)   eye(m,n)   rand(m,n)
    x=a:step:b % 包含ab,step省略默认1.不会有超过b的数
    linspace(a,b,n)  包含ab,分为n个数
    a=fix(10*rand(m,n))
    factorial(n)  power() pow2()
    conj()   real() imag()

    % string
    input('please input','s') % 返回char
    disp(var) % 显示变量内容而不显示变量名,自动换行.
    fprintf(formatSpec,A1,A2…);

    % statistics
    sum/mean(A,1) % 列求和
    sum/mean(A,2) % 行求和
    [value,index]=max(x) 
    diag(A) % 取对角为向量/构造对角阵
    length(x)  各维度长度最大值   size(x)  各维度长度
    [sorted, index]=sort(a,'descend') % index=sorted在a中对应数的下标
    idx=find(A) % 查找非零元素,返回线性索引
    ```
- index
    ```matlab
    a = [1,2,3;4,5,6]   a = [1 2 3; 4 5 6]
    % >=1,end表示最后
    x(x>1)==x(find(x>1)) % 逻辑下标:logic数组作为下标,提取下标为非0的元素:
    A(r,:)  A(:,c)
    A([3,4,6],[1,3,2])
    A([1,3,2]) A(:) % 线性索引:单下标列主序
    ```
- operators
    ```matlab
    A.'transpose  A'矩阵共轭转置
    A\B(A^{-1}B)  A/B   A^n   inv(A)   det(A)   rank(A)   norm(A,p)   [V,D]=eig(A)
    % element-wise加.
    % 关系运算符:~=不等与   True=1, False=0   数组比较的是每个元素,结果为一个同维logical数组.
    % 逻辑运算符:& | ~   True=1, False=0
    ```
- data structure
    - `a = 'abc'   a = "abc"` character array / string
    - `a = 2+3i` i = imaginary unit
    - Cell 元素可以是不同类型 a=cell(m,n) 存取数组元素a{i,j} 
    - Struct 直接F.first=…
- others
    ```matlab
    mod(a,b)求余结果向-inf舍去   rem(a,b)向0舍去
    floor(x)向-inf   fix(x)向0   ceil(x)向+inf   round(x)四舍五入
    3.5e7   3.5*10^7 指数
    format long/short/loge e/short e 单精度/双精度位数显示   Format 恢复默认
    +eps  加在除数防止除0
    % 函数句柄:作为参数传递给其他函数,在函数前加@
    ```
- functions
    ```matlab
    % 脚本文件执行完后仍然保留在工作空间中
    addpath('E:\mywork')
    function [r1, r2, r3]＝funname(a1, a2, a3, a4)
    nargin,nargout % 输入参数个数,输出参数个数
    % 调用函数以文件名为准
    % 一个主函数,其他为子函数
    f(1:2,5:7) == f(1,5), f(2,7)
    f=@(x,y)(x+y) % 匿名函数
    [~,~,ext] = fun(...) % 忽略返回值
    ```

## plot
```matlab
hold on / hold off
grid on / grid off
subplot(1,2,1)
plot(x,y1,x,y,'-—r',x,-y,'-—r') % 画3条线,间断点会连接起来
fplot(@(x) sin(x))
legend('sin(x)','cos(x)')
title('Figure: Legend Example', 'interpreter', 'latex')
xlabel('str') ylabel('str')
colormap([1,0,0])
figure   figure(3) % 指定
plot3(x1,y1,z1,'S1',x2,y2,z2,'S2') % 画曲线
[X,Y]=meshgrid(x,y)  % 生成平面网格点,x横向y列向复制
mesh(X,Y,f(X,Y))  % 绘制曲面(连线染色)
surf(X,Y,f(X,Y))  % 网格染色
meshc(X,Y,f(X,Y))  meshz(X,Y,z)  % 绘制等值线投影、边界垂帘的网格图
contour(X,Y,z,n)  contour3(X,Y,z,n)  % 绘制2维、3维等高线n条
```

## string
- character array
    - s1 = 'happy'
    - s1(3) = 'p'
    - [s1,s2] = 'happyboy'
- string
    - "happy" + "."
    - string array [s1,s3]
    - strlength(s1)

## 符号计算
- 定义变量
- syms arg1 arg2 real/positive(后面的类型可选)不用加分号
- 相当于把arg的变量赋给名为arg的变量
- 这种命令方式相当于把后面的参数当做字符型传入后面的函数.
- =syms('arg1','arg2','real');
- x1=sym('x1');	a1=sym(sqrt(200));	v=sym([100,200]);
- x1=sym('x1','real');
- 如果是字符串,则产生一个符号数或变量；
- 如果是数值标量或数值矩阵,则其转为符号类型.
- 和字符数组
- 定义符号变量并存储到变量中,组成的表达式也在变量中,和字符数组没有关系！
- Subs
- subs(s, old, new)  替换表达式s中old符号变量为new(变量或数字)
- 可以是向量:subs(f,[x,y],[1,2])  x,y为符号变量.
- simplify
- simplify(expr)  化简表达式
- 求值
- digits  digits(n)  显示、设置vpa计算结果的有效数字的位数
- vpa(s)  vpa(s,n)  (采用n位有效数字计算精度)求s的数值结果(返回sym)↓
- double(s)  char(s)  转换表达式s
- compose
- compose(f, g)返回复合函数f(g(y)),其中f=f(x),g=g(y). x和y分别为f、g中找到的符号变量
- compose(f, g, z)返回复合函数f(g(z)),变量z代替上面变量y
- compose(f, g, x, y, z)返回复合函数f(g(z)). 指定自变量x,y
- limit
- limit(f,x,a)计算f(x)在x趋于a的极限,返回符号型
- limit(f,x,a,'left')	limit(f,x,a,'right')左右极限
- diff
- diff(f,x)对f(x)的x求1阶偏导
- diff(f,x,n)求n阶导
- int
- int(expr,var)对var求不定积分
- int(expr,var,a,b)从a到b的定积分,返回符号型.
- taylor
- taylor(f)计算f的5阶麦克劳林多项式
- taylor(f,v,a)计算f对变量v在点a展开的麦克劳林多项式
- taylor(f,v,a,Name,Value)指定属性:Name(字符串),Value值
- taylor(expr,v,'expansionpoint',0,'order',8)8阶0点展开
- solve
- solve(a*x+b*y==10,a*x-b*y==20,x,y)解方程(组),表达式等式要有2个等号,后面指定求解变量并返回结构体变量,成员名即解的变量名.
- dsolve
- syms y(x)注意定义方式！
- s=dsolve(diff(y,x,1)==y,y(0)==4,x)解微分方程,第二个为初始条件.
 
## 线性代数,数据拟合
- tri-u/p
- triu(A) tril(A) 获得上三角、下三角阵(triangle upper/lower)
- 解线性方程组
- Ax=b:x=A\b
- eig
- eig(A) 获取特征值组成列向量
- [P,]=eig(A) 为特征向量组成的对角矩阵,P的列向量是对应的特征向量组
- A*P=P*；应用于矩阵求幂:A^n=P*.^n*inv(P)
- P为正交矩阵时inv(P)=P'.
- polyfit
- p=polyfit(x,y,n) n次多项式线性拟合x,y数据点
- p为幂次从高到低的多项式系数向量(n+1个元素的行向量,包括0次幂)
- polyval
- y=polyval(p,x) x在给定系数p的多项式的值
- roots()求多项式的根

 
## 数值微分,积分
- 模型
- 一阶常系数微分方程dy/dt=f(t,y)
- y=y(t)未知函数
- f(t,y)给定的二元函数
- 初始条件y(t_0 )=y_0
- Ode23(低阶)/ode45(高阶)
- [T, Y] = ode23(@fun,Tspan,y0)
- @fun为函数f(t,y)句柄(匿名函数不用@,函数文件的函数要加@)
- 方程组时返回列向量,每一行一个变量f(t,y_n),所以运算符用数组运算
- 方程组不同的y_n用y(1),y(2)…表示
- 表示法:
- R=[…;…]
- r(1,:)=…	r(2,:)=…
- Tspan为求解区域,一般为[T0,Tn]表示两个端点.也可以用行向量具体指定.
- y0初始条件,列向量表示方程组每个y0的数值
- T为列向量,Tspan得到的自变量t的离散数据点
- Y为数值解y的离散点,每一列对应于列向量T中的数值解,不同列对应方程组不同变量.
- 高阶:方程组y(1)=y;y(2)=dy/dt
- Euler法:(不讨论方程组即y(t_k )=y_k)
- 泰勒公式y(t)=y(t_0 )+(t-t_0 ) y^' (t_0 )+(t-t_0 )^2/2 y^'' (t_0 )+⋯
- 近似y(t)=y(t_0 )+(t-t_0 )f(t_0,y_0)
- 迭代:y_(k+1)=y_k+hf(t_k,y_k),其中h=∆t为定值
- Quad:Simpson 积分法
- quad(fun,a,b,tol) fun函数句柄,ab下限-上线,tol精度(可选)
- dblquad矩形区域二重积分
- dblquad(fun,a,b,c,d,tol) ab内限cd外限
- quad2d:tiled 方法
- quad2d(fun,a,b,c,d) ab外限cd内限,可为函数句柄
- trapz:无具体表达式
- trapz(x,y)x,y为向量数值
- integral,integral2积分
 
## 优化工具箱
- 函数优化
- fminunc( ) 多变量无约束
- ga( )遗传算法
- 求最大值
- 函数*(-1)求最小值找到最小值点对应原函数最大值点
- 求导(梯度下降法)
- X_min/max=solve(diff(f,x))
- fminbnd()单变量边界约束
- [xmin,fmin]=fminbnd(fun,a,b)求最小值
- a,b为区间,fun函数句柄
- fminsearch()多变量无约束
- x = fminsearch(fun,x0) 句柄函数x(1),x(2)
- fmincon()多变量有约束
- x = fmincon(fun,x0,A,b,Aeq,beq,lb,ub,nonlcon)
- nonlcon:非线性约束句柄
- [c,ceq]=nonlcon(x) c(x)<=0;ceq(x)=0;没有约束用[]
- linprog() 线性规划
- [x,fval]=linprog(C,A,b,Aeq,Beq,Lb,Ub)求最小值
- min┬ ⁡〖C^T X〗       s.t.  AX≤b,    A_eq X=b_eq,Lb≤X≤Ub
- X,b,Lb,Ub为列向量
- 求最大值:C-C带入函数；Aeq,Beq无约束:[]
- fzero:求解非线性方程根
- fzero(fun,x0)—x0为起始点
- fsolve()解非线性方程(组)
- x = fsolve(fun,x0)
- 句柄函数function F=fun(x) F(1)=...x(1)...x(2)...
- lsqcurvefit()非线性函数拟合
- x = lsqcurvefit(fun,x0,xdata,ydata)
- fun的参数为@(x,xdata)x(1)...x(2)...中x(1),x(2)为待求参数
- xdata,ydata为数据集,x0为待求参数起始点,返回值x为带求参数向量即调用f(x,xdata)其中x为[x(1),x(2),...]
 
## 随机变量模拟
- rand():(0,1)区间上均匀分布
- randn()标准正态分布
- exprand()指数分布
- normrnd()正态分布
- r = normrnd(mu,sigma,m,n)
- (a,b)区间均匀分布:
- a+(b-a)*rand(m, n)
- unifrnd(a, b, m, n)

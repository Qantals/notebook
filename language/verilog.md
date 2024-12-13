# verilog

## TOC
- [基础](#基础)
- [数据](#数据)
- [模块](#模块)
- [结构](#结构)
- [语句](#语句)
- [组合逻辑](#组合逻辑)
- [时序逻辑](#时序逻辑)
- [状态机](#状态机)
- [竞争和冒险](#竞争和冒险)
- [testbench](#testbench)

## 基础
- 标识符
    - 数字字母下划线和$（用于命名系统函数或任务）
    - 大小写敏感
    - c++风格注释
- 数值
    - 0,1,x未知,z高阻
    - 基数：`[bitwidth]'[d/h/b/o][digit]`
        - digit可用下划线分
        - 不指明位宽：32位，`'`可选
        - 负数的符号在位宽的前面
    - 小数：`3.5`,`3e5`
- 数组
    - 多维数组 `reg [7:0] name[2:0][1:0]`
    - 必须指定下标读写
- 向量[a:b]
    - 表达式`[32-1:0]`
    - 可以 $a<b$ (MSB为a)
    - 固定位宽 `[31-:8]=[31:24]; [0+:8]=[0:7]`
- 表达式位宽
    - 手动调整 `{1’b0,a}  sum[8:1]`
    - 赋值：
        1. 由等号左右侧确定最大位宽
        2. 扩展右侧到最大位宽
        3. 赋值，截掉高位信号
- 编译指令(`开头)
    ```verilog
    `define name xxx 在整个编译过程中有效，包括此文件外
    `undef name
    `ifdef `ifndef `elsif `else `endif
    `include "./head.v"
    `timescale unit/precision 后面模块继承，直至遇到另一个`timescale
    ```

## 数据类型、运算符
- 数据类型
    - wire
        - `wire [2:0] a,b,c;`
        - net型，只能赋值一次，只能assign持续赋值
        - 缺省为z
    - reg
        - variable型触发器,只能always块赋值
        - 缺省为x
        - 可以使正值或负值。作为操作数视为无符号数
    - memory：reg数组
    - reg [n-1:0] name [m-1:0]  n位宽字，m个大小
    - 读写必须指定地址  name[0]<=……
    - integer：用于过程赋值语句，用于for循环
    - real：默认0值，赋给整数截取整数部分
    - localparam：常数，在模块内，建议常量名大写
    - 字符串：reg数组，每个字符1字节8bit，不能有回车符，即不能换行写。如果寄存器变量的宽度大于字符串的大小，则使用0来填充左边的空余位；小于则会截去字符串左边多余的数据
    - time：保存仿真时间，64位，调用系统函数$time赋值给它

### 操作符
- 除条件操作符从右往左关联，其余操作符都是自左向右关联
- 优先级：
        单目运算	+ - ! ~
        乘、除、取模	* / %
        加减	+ -
        移位	<<  >>
        关系	<  <=  >  >=
        等价	==  !=  ===  !===
        归约	& ~&
            ^ ~^
            | ~|
        逻辑	&&
            ||
        条件	?:多路复用器
- X/Z
- 算术：某一位为 X，结果全部 X
- 相等/不等：有一位为 x 或 z，结果为x
- 全等：可以比x、z（x与z不同）
- 不确定的操作数：多位的操作数不全为0认为1；4’bxx00认为不确定，4’bxx11一定是1↓
- 关系、逻辑：操作数为 x 或 z，结果为 x
- 算术运算：溢出就截掉高位
- 求模：全部当成正数计算，结果取第一个操作数的符号
- 乘法除法：截掉小数
- 关系运算、逻辑运算结果为一位数值0,1
- 按位运算
- 与、或、非、异或、同或
- 如果 2 个操作数位宽不相等，则无符号扩展短的
- 移位：>>逻辑移 >>>算术移
- 缩减：与（非）、或（非）、异或（同或）
- 位拼接{a,b} 
- 必须指定位宽
- 赋值等号两侧都可以拼接{cout,sum}=a+b;
- N{……}表示复制N次，可以嵌套



## 模块

### 模块
- Module name #(parameter) (port);……endmodule  端口声明也可以写在括号里
- 可以是一个元件或元件组合
- 包括变量声明，数据流语句，底层模块实例，行为语句，任务函数。  顺序任意，可选。
- 模块内不能声明模块（声明类似architecture，定义类似实例调用）

### 端口声明
- 没有端口不用声明
- input不可写 output不可读 inout都可以
- inout:可用于仿真下加三态缓冲选择输入输出，高阻态可以被上拉或下拉。如果其他输入和三态拉冲突则表现为X
    ```verilog
    inout PAD;
    assign PAD = OEN ? 'bz : DIN;
    assign DOUT = OEN ? PAD : ‘bz;
    --testbench:
    assign PAD = OEN ? PAD_REG : 'bz;
    ```
- 默认wire型,即wire型可不声明数据类型
- 模块内
- input,inout:wire  不能reg（输入反应外部变化）  output:wire/reg
- 模块外
- input:wire/reg  output,inout:wire（输出反应模块变化）

### 模块参数
- Parameter name=init,……;
- 在端口声明或实体内。要给初始值！可以在调用时被覆盖
- defparam：层次调用直接修改，可以写在例化前面。不建议  defparam u_ram_4x4.MASK = 7 ;
- 利用 defparam 可以改写模块在端口声明时声明的参数，利用带参数例化也可以改写模块实体中声明的参数
- 混合使用：前提是所有参数都是模块在端口声明时声明的参数或参数都是模块实体中声明的参数，否则只能用带参数模块例化的方法去改写参数不能用defparam

### 模块（带参数）例化
- Module_name #(.para(num),……)inst_name(.port(signal),…);  或位置连接(signal,…)
- 允许端口内外位宽不同，右对齐高位截断或左端补z
- 允许输出端口悬空（写空括号）或删除（不写）；输入端口可悬空不可删除
- 顺序连接或名字连接，不能混用
- 层次访问：层层访问到变量等  top.u_m2.u_n3.c ;
- 重复例化
    ```verilog
    genvar i;
    generate
        for(i=1;i<=3;i=i+1) begin
        name_ins name_module(...);
        end
    endgenerate
    ```
 


## 结构
### 结构建模
- Gate（门级）例化语句
- UDP (用户定义原语)例化语句
- module (模块) 例化语句
### 过程结构：行为级建模
- Initial和always语句之间并行，内部顺序。不可嵌套
- 顺序语句：非阻塞赋值是并行，顺序无关
- Initial begin end
- 从 0 时刻开始执行，只执行一次
- 不可综合，用于初始化，信号检测
- Always
- 无敏感量的always begin end：从0时刻开始执行，反复。  常用于产生时钟信号（或initial forever也一样）
- 可选事件控制@
### 过程赋值
- 赋值对象为reg，integer，real等，直到再赋值前不变
- 阻塞赋值=，下一句前赋值完毕
- 非阻塞赋值<=，并行执行（使用旧值），块结束才赋值（即时序逻辑的下一次触发）
- 不要在一个过程结构混用，always块组合逻辑阻塞赋值，时序逻辑非阻塞赋值，initial块阻塞赋值
- 竞争冒险
- 阻塞赋值：always块并行，无法判断顺序，导致编译出a、b值相等（等于谁看编译器）
    ```verilog
    always @(posedge clk) a=b;
    always @(posedge clk) b=a;
    ```
- 使用非阻塞赋值对上例可以实现ab交换
### 连续赋值assign（数据流建模）
- 允许声明时赋值
### 过程连续赋值
- assign deassign只能用于reg变量，作用时连续赋值reg变量直到deassign。并保存assign的值，直到过程语句的赋值。
- force release：可用于reg变量和wire变量。Reg变量同上，wire变量在release后立刻变成其他连续赋值的值。
### 事件控制：继续执行语句要有条件
- 一般事件控制
- 组合逻辑电平触发，时序逻辑边沿触发（posedge,negedge）  不能混用
- q = @(posedge clk) d ; //在clk上升沿时刻d赋值给q，不推荐这种写法。在顺序语句块中要等到触发才继续向下。
- 命名事件控制
- 声明event变量，触发（->）该变量来识别该事件
    ```verilog
    event start_receiving;
    always @( posedge clk_samp) begin
            -> start_receiving ; 
    end
    always @(start_receiving)
    ```
- 敏感列表：or或,连接；@*或@(*)表示该语句块的所有输入都是
- 电平敏感事件控制
- wait (start_enable) ;等到为真才继续执行
### 时延：不可综合
	惯性时延
	普通时延assign #10    Z = A & B ;
	隐式时延wire #10      Z = A & B;
	声明时延：该变量的所有赋值都被推迟  wire #10 Z ;  assign Z =A & B
	时延控制
	常规时延：不顾表达式，等待后再赋值。不会滤窄脉冲  #10 value_general=value_test ;  相当于#10 ;value_general=value_test ;
	内嵌时延：先存表达式，等待后再赋值。延时后才执行下面语句。  value_embed = #10 value_test ;
### 语句块
	块内可以声明参数、reg、integer、real、time、event
	顺序块：initial，always
	并行块：fork ... join放在initial里面。即使是阻塞赋值。效果等同非阻塞赋值。
	嵌套块：initial里除了fork还有其他顺序赋值，则把fork当成整体顺序执行（即需要等待fork内时延全部通过），fork内并行。
initial begin
    ai_sequen2= 4'd5; //at 0ns
    fork
        #10 ai_paral2= 4'd5 ;    //at 10ns
        #15 bi_paral2= 4'd8 ;    //at 15ns
    join
    #20 bi_sequen2= 4'd8 ;    //at 35ns
	命名块：begin:block_name...块中可设局部变量，外部调用：module_name.block_name.variable_name
	disable block_name退出语句块，包括任意位置的语句块。一般用在循环的语句块，如果是always或forever的语句块只能退出当前次，下一次仍继续执行。
 
语句
1.	If-else
	If(expr)begin……end
else begin……end
顺序语句
	If()……else if……else……
	表达式为1认为真，0或z为假
	设计时不要在一个块写并行if语句，用好else
	设计时比如写异步复位，就不要先写不复位的情况：
if(rstn)...正常...else...复位...
2.	Case
	Case(sel) item:begin……end
default:begin……end
endcase
顺序语句
	多匹配则只匹配前面的，没匹配保持当前值
	多选项同一语句逗号隔开
2'bx0, 2'bx1: ...
	x/z
	?表示z
	case的选项可以有x/z/?（不定/高阻），不可综合
	casex（sel和item视x,z/?为不在乎）,casez（sel和item视z/?为不在乎）按顺序比较，不可综合 
	Full case全匹配，组合逻辑必须
parallel case没交叠
3.	循环
	For(exp1;exp2;exp3)begin……end
	Repeat(expr)begin……end
expr指定循环次数，为常量，变量或信号，如果是后两者则循环次数定住不变
	While(expr)begin……end
	Forever begin……end
可用disable中断，常用于产生时钟信号
4.	函数
	任务或函数：将重复性的行为级设计进行提取，并在多个地方调用
	函数只能在模块中定义，位置任意。并在模块的任何地方引用，作用范围也局限于此模块。
	特点
	不含有任何延迟、时序或时序控制逻辑（就是组合逻辑），不含有非阻塞赋值语句
	至少有一个输入变量，不能为inout型，只有一个返回值且没有输出
	函数可以调用其他函数，但是不能调用任务
	声明
	function datatype [range-1:0] function_id ;
input_declaration ;
 other_declaration ;
procedural_statement ;
endfunction
也可以在函数名和分号之间加一个括号将 input 声明包起来
	会隐式的声明一个宽度为range名字为 function_id 的寄存器变量，传递返回值。默认位宽为 1。
	调用
	function_id(input1, input2, …);
	参数可以用defparam改写，取决于编译器
5.	其他函数
	常数函数
	function integer logb2;
input integer depth ;//外面是parameter调用
	在编译期间就计算出结果为常数的函数，代替常量
	常数函数不允许访问全局变量或者调用系统函数，但是可以调用另一个常数函数
	automatic函数
	一般函数的局部变量是静态的，两个函数调用行为同时对同一块地址进行操作，会导致不确定的函数结果
	此类函数在调用时是可以自动分配新的内存空间的，也可以理解为是可递归的
	局部变量不能通过层次命名进行访问
	function automatic integer factorial ;
factorial=(data>=2)?data*factorial(data-1):1;
6.	任务
	在模块内任意位置定义，模块内任意位置被调用。包括组合逻辑和时序逻辑
	看做是过程性赋值，output 端信号返回时间是在任务中所有语句执行完毕之后。
	使用全局变量：变量声明在模块之内、任务之外
	比较
比较点	函数	任务
输入	函数至少有一个输入，端口声明不能包含 inout 型	任务可以没有或者有多个输入，且端口声明可以为 inout 型
输出	函数没有输出	任务可以没有或者有多个输出
返回值	函数至少有一个返回值	任务没有返回值
仿真时刻	函数总在零时刻就开始执行	任务可以在非零时刻执行
时序逻辑	函数不能包含任何时序控制逻辑	任务不能出现 always 语句，但可以包含其他时序控制，如延时语句
调用	函数只能调用函数，不能调用任务	任务可以调用函数和任务
书写规范	函数不能单独作为一条语句出现，只能放在赋值语言的右端	任务可以作为一条单独的语句出现语句块中
	声明
	task task_id ;
    port_declaration ;
    procedural_statement ;
endtask
也可以在任务名和分号之间加一个括号将端口声明包起来
	端口声明：input端口变量看做wire型；output端口变量看做reg型，不需要用reg再次说明，建议用阻塞赋值方便控制时序（不用always块就用#延时）。
	调用：在initial或always块
	task_id(input1,input2,…,outpu1,output2,…);
	端口必须按顺序对应
	输入端可以是wire、reg型，输出端一定是reg型
	automatic：和函数一样
 
组合逻辑
1.	优先编码器：casex或if语句
2.	多路复用器：if或三目语句
assign data_out = sel[1]?(sel[0]?data_in[3]:data_in[2])
:(sel[0]?data_in[1]:data_in[0]);
3.	注意
	不能多驱动源（变量不要在多个always赋值）
	敏感量列表完整（用*）
	完整分支输出赋值
	Always块变量没赋值就保持原来的值，综合出意外锁存器
	方法：
if写完else分支；
always起始部分赋初值
full case满足
	要用阻塞赋值
	使用assign语句可避免 always 语句描述组合逻辑时容易出现的毛刺等问题
 
时序逻辑
1.	敏感量要边沿型（包括reset），用非阻塞赋值<=（消除竞争冒险）
	在同一个 always 块中建立时序和组合逻辑模型时，用非阻塞赋值。
	敏感量保证对应信号在边沿，且指定电平；内部的if保证是这些敏感量的哪一个引起语句激活并确定优先级。
2.	异步复位
	Always@(posedge clk,posedge rst)
if(reset)……else……
	Rstn就negedge rstn,if(!rstn)
3.	异步复位同步使能
	……if(reset)……else if(en)……
	最后没else分支表示锁存，即else q<=q;
4.	锁存器
	Always@(clk,d)
if(clk)q<=d;
	通过无else实现锁存（q<=q）（时序逻辑）
5.	异步复位锁存器
	Assign q=(reset)?0:(clk?d:q);
6.	二进制计数器
	Always@(posedge clk)
if(rst)regN<=0;
else regN<=regN+1;
	Assign cout=(regN==N)? 1’b1 : 1’b0 ;
	确定regN位宽就不用轮回
7.	模m计数器
	……if(reset) regN<=0;
else if(regN<(M-1)) regN<=regN+1;
else regN<=0;
	else if(regN>=(M-1)) regN<=0;
else regN<=regN+1;
	要轮回
8.	秒表（BCD计数器）
	时序逻辑更新寄存器
reg<=reg_next
update_cnt++
assign update=update_cnt==MAX?1:0
	用组合逻辑生成reg_next（先加1再轮回）
if update
  if(i不进位) i++
  else begin
    i=0;
    if(j不进位) j++......
	时分秒进位（先轮回）
if(secL==9)
  secL<=0;
  if(secH==5)
    secH<=0;
    if(minL==9)......
    else minL<=minL+1;
  else secH<=secH+1;
else secL<=secL+1;
	或者24小时清零（先轮回）
if(i==9) begin
  i<=0; j<=j+1;
end else if(i==3 && j==2) begin
  i<=0; j<=0;
end else
  i<=i+1;
	或者60分钟/秒清零（先轮回）
if(i==9) begin
  i<=0; 
  if(j==5)
    j<=0;
  else
    j<=j+1;
end else
  i<=i+1;
	递减计数（先轮回）
if(i==0)
  if(j==0)
    锁存
  else begin
    j<=j-1;
    i<=9;
  end
else i<=i-1;
 
状态机
1.	状态编码，状态寄存器
	Localparam [1:0] s0=2’b00,s1=2’b01,……;
	Reg [1:0] state_reg,state_next;
2.	时序逻辑
	Always@(posedge clk, posedge rst)
if(rst) state_reg<=0;
else state_reg<= state_next;
3.	次态逻辑
	Case(state_reg)
s0:if(input) state_next=sx;
4.	输出
	Moore：assign y=(state_reg==s0)||……;
	Mealy：assign y=(state_reg==s0)&a&b;
5.	有时候直接把状态寄存器当成输出，用于控制
 
竞争与冒险
1.	原因
	竞争：在组合逻辑电路中，不同路径的输入信号变化传输到同一点门级电路时，在时间上有先有后
	冒险：由于竞争的存在，过渡时间内可能产生瞬间的错误输出，例如尖峰脉冲
	竞争不一定有冒险，但冒险一定会有竞争。
2.	同步电路
	在时钟边沿驱动下，利用触发器对一个组合逻辑信号进行延迟打拍,包括输入和输出
	最好延迟3 拍，输入多打2拍
3.	格雷码计数器
	如101110因为延时变为101111110出现毛刺
	改为格雷码计数器或用同步计数器
 
Testbench
1.	技巧
	系统函数：$time,$finish,$stop
$display("xxx");
	行为级（类似C语言）检验输出结果
没有复杂反馈和控制的逻辑设计的简单TestBench，否则UVM
initial begin
  for(i=0;i<=7;i=i+1) begin
    in=i;
    check=behave(i); //行为级计算
    #1;
    if(check!=out) begin
    $display(“wrong!”); $stop;
    end
    //#9; 可选
  end
  $display(“accept”);
  $stop;
end
	计数器
reg [4:0] cnt;
wire [4:0] cnt_nxt = (cnt == end_addr) ? start_addr : cnt + 1'b1;
always @ (posedge clk_i or negedge rst_n) begin
  if (~rst_n) cnt <= start_addr;
  else cnt <= cnt_nxt;
end
	触发条件1
buy_oper  = 10'b00_0101_0101 ;
repeat(5) begin
    @(negedge clk) ;
    coin      = buy_oper[1:0] ;
    buy_oper  = buy_oper >> 2 ;
end
	触发条件2
@(negedge clk) ;
buy_oper  = 10'b00_0101_0101 ;
	时钟1
always begin
    clk = 0 ; #(CYCLE_200MHz/2) ;
    clk = 1 ; #(CYCLE_200MHz/2) ;
end
	时钟2
initial begin
    rstn = 1'b0 ;
    clk = 1'b0 ;
    #5 rstn = 1'b1 ;
    forever begin
        #5 clk = ~clk ;
    end
end
	地址译码器+使能assign三目
assign BRAM_WRITE = wr_en_reg ? size_reg : 4'h0;
assign P0_HSEL = (HADDR[31:16] == 16'h0000) ? Port0_en : 1'b0;
	always #20 begin ... end
	脉冲发生器
if(time_start)
  if(cnt==CNT_MAX) begin
    output<=0;
    cnt<=cnt;
  end else begin
    output<=1;
    cnt<=cnt+1;
end else if(input)
  time_start<=1;
充分用行为级的if写法，eda自己综合去
	把if条件写简单：用if嵌套层层分解，内部可以留有复位的条件，直接执行复位的语句就行（比如使sig在0~10内偶数时执行A，则sig[0]==1时执行复位，==0时执行A）







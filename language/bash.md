## shell脚本
- `shellcheck example.sh`

代理
```sh
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
unset http_proxy
```

error code
```bash
&& # 短路,前命令成功再执行后面
|| # 短路，前命令失败再执行后面
true # code=0
false # code=1
; # concatenate many commands in one line
```

变量
- `read name`终端读入变量
- `your_name="runoob"`定义变量，=不留空格，字符串单引号双引号无引号均可
- `declare/typeset -i my_integer=42`整数变量，否则默认字符串
- `my_array=(1 2 3 4 5) | my_array[0]=1 | declare -A my_array`数组
- `my_array[@]`读取所有元素

特殊变量
- `$`或`${}` 引用变量
- `$0脚本名 $1参数1 $#参数数量 $?上个命令退出状态 $_上个命令最后一个参数 $$程序PID $@所有的参数，用于for迭代 !!上次命令，包括参数`特殊变量
- `sudo !!`再执行上一次命令
- `${n1}${n2} 'a''b'` 直接拼接
- 变量名大写
- `foo=$(pwd)` 保存pwd命令输出结果为foo变量
- `cat <(ls)` 将命令的输出临时保存为文件并替代此位置  
    - `diff <(ls dir1) <(ls dir2)`

转义
- `\`连接换行
- 双引号转义多个字符; 单引号不转义不能有变量; 反引号返回执行后结果
- <code>val=`expr 2 + 2`</code>获得表达式，反引号可换为<code>$()</code>
- `awk '{print $0}' 122.txt`打印所有内容，$n表示第n个字段（列），n=0表示整行
- `[ $a == $b ]`**表达式和运算符之间要有空格，条件表达式要放在方括号之间，并且要有空格**
- 乘号(*)前边必须加反斜杠(\)才能实现乘法运算
- `${#string}`得到字符串长度
- `${string:1:4}`切片，索引0开始，包括1和4
- `${1:-"default"}`使用${1}输入第一参数，如果为空则使用默认值"default"

条件判断  
```bash
[[ $a -eq $b ]] # 比较建议用双括号
# 数字比较 -ne -gt -lt -ge -le
# 布尔：!:not -o:or -a:and
# 逻辑： && ||
# 字符串比较：== != -z长度为0 -n长度不为0
[ -d $file ] # 文件测试 -d目录存在 -f普通文件存在 -e文件或目录存在
if [ "$a" -eq "$b" ]
if ((1==1)) # like C language
then
    echo "true"
elif [ "$a" -nq "$b" ]
    ...
else
    echo "false"
fi
if [ "$a" -eq "$b" ]; then # then在同一行就要有分号

case ${VAILE} in
    "1")
        echo "我是1"
    ;;
    *)
        echo "我不是1，也不是2"
    ;;
esac
```

循环  
```bash
# globbing
convert snow.{jpg,png} = convert snow.jpg snow.png # shortcut
touch foo{,1,2} = touch foo foo1 foo2
touch proj{1,2}/src/test{1,2,3}.py # Cartesian product
touch {a..j}

for n in 1 3 5
for idx in {00...40}
do
    echo "${n}"
done
for ((n=0;n<3;n++)) # like C language

while [...] # 或until ((a==b))
do
    ...
done
```

函数  
function can change enviroment variables, while scripts can't.
Scripts can only affect their processes. They need to use "export".  
```bash
function fun(){
    mkdir -p "$1"
    macro_path=$(pwd)
    cd ${macro_path}
}
# 调用
source a.sh # only need to load once
fun arg1 arg2
```
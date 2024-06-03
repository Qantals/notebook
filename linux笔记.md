# Linux 笔记
## Content
- [命令帮助](#命令帮助)
- [目录](#目录)
- [文件](#文件)
- [系统](#系统)
- [vim](#vim)
- [shell脚本](#shell脚本)

## 命令帮助

- 光标：方块左侧为backspace，方块为replace  
    Ctrl+Z 或 命令末尾加& 后台执行  
    Ctrl+U 清除行  
    Ctrl+L 清屏 或$clear  
    Ctrl+S 挂起  
    Ctrl+Q 解冻
- `man cmd`查看帮助文档  
    `info cmd`详细说明
- `tldr cmd` show examples better than 'man'
- `which` 命令在PATH变量的路径  
    `whereis` 命令的源文件、可执行文件、帮助文件搜索路径
- `less` TUI查看文本  
    `more` CLI查看文本
    - `b/f(space) u/d j/k` 翻页
    - `/`向下搜索 `?`向上搜索 `n`下一个关键词 `N`上一个
- `#!/bin/sh` shebang  
    - `#!/usr/bin/env bash(python)` is better
- `cat /etc/shells` 查看所有shell  
    `$SHELL` 查看默认sehll  
    `chsh -s /bin/zsh` 修改默认sehll
- `xdg-open [doc]` open with default app
- `find <dir> -name/iname 'name' -type f` 查找文件
- `grep <pattern> <file>` 筛选所在行

参数用white space分隔
```bash
echo hello
echo "hello world"
echo hello\ world
/usr/bin/echo world
```

PATH
```bash
echo $PATH # separated by :
which echo # find path in PATH
PATH=$PATH:/... # 追加
export PATH # 变为全局变量多用户使用
```

ls  
number of hard links | owner | group | size | date of modified  
Read permission of directory: ls.  
Execute permission of directory: cd to this. And cd
need execute permission of all parent directories.

重定向和管道
```bash
cmd < doc_in > doc_out # 清除覆写模式
cmd >> doc # 追加模式
1> 2> # 标准和错误的重定向，追加模式也一样
cmd > log 2>&1 # 2错误重定向到1
cmd &> doc # 1标准 和 2错误 都写入

cmd1 > tmpfile && cmd2 < tmpfile # cmd1 | cmd2
cmd1 | tee abc.log | cmd2 # tee 既输出又记录
ls -l | tail -n1 # output end of 1 line
sudo echo 50 > /sys/class/backlight/amdgpu_b10/brightness # permission denied: Shell but not sudo use pipeline.
echo 50 | sudo tee brightness # This is OK.
```

root
```bash
# 省略用户名默认root用户
sudo su
su test # 切换到test用户，路径/root
su - test # 路径/home/test
```

script
```bash
chmod +x a.sh | chmod 777 a.sh
source a.sh | . a.sh # 当前shell执行
bash a.sh # 子shell执行
./a.sh # 子shell执行，需要chmod +x权限
```

homework:`curl --head --silent https://missing.csail.mit.edu | grep last-modified | cut --delimiter=' ' -f1 --complement > ~/last-modified.txt`

## shell脚本
- `shellcheck example.sh` 检查shell脚本

代理
```sh
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
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
- `$0脚本名 $1参数1 $#参数数量 $?上个命令退出状态 $_上个命令最后一个参数 $$程序PID $@所有的参数，用于for迭代`特殊变量
- `sudo !!`再执行上一次命令
- `${n1}${n2} 'a''b'` 直接拼接
- 变量名大写
- `foo=$(pwd)` 保存pwd命令输出结果为foo变量
- `cat <(ls)` 将命令的输出临时保存为文件  
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
```bash
function fun(){
    mkdir -p "$1"
}
# 调用
source a.sh
fun arg1 arg2
```

## 文件

`wget -O name -P path -c(断点继续) URL`  
`sh -c "$(curl -fsSL URL)"`静默模式安装
`mount -o loop [source] [dir]`挂载  
`umount [dir]`解挂  
`zip abc.zip file` 压缩zip  
`unzip file -d <dir>` 解压zip
    - `-v` 查看但不解压

`tar -zcvf abc.tar doc1 doc2 ...` 归档（打包）且压缩
    - `-c` 打包文件 `-x` 解开档案
    - `-v` 列出详细过程
    - `-f <name>` 指定档案文件名称，用.tar/.tar.gz结尾
    - `-z`.gz  `j`.bz2 `J`.xz
    - `-C <dir>` 解压到指定目录

`ln [-s] f1 f2` f2硬（软）链接到f1

## 系统

```bash
free -h # 查看内存信息
cat /proc/version # 显示正在运行的内核版本  
lsb_release -a
cat /etc/issue # 显示发行版本信息 
df -h # 查看分区使用情况
du -sh file # folder usage
cat /proc/cpuinfo # 查看cpu相关信息，包括型号、主频、内核信息等
```

`ps -ef` 查看所有进程  
`kill pid` 杀进程

```bash
apt install cmatrix # 用apt安装软件
apt-get update # 更新软件列表
apt-get upgrade # 更新版本
apt-get list | grep [name] # 查看软件目录
apt-get [purge] remove <package> # 删除软件及其配置文件
apt-get autoremove # 删除没用的依赖包
apt-get clean

dpkg -i [name] # 安装deb文件包
dpkg -l # 查看安装的软件
dpkg -r [name] # 卸载软件
```



## vim
- `$vim doc`打开编辑
### 模式
- `esc`其他模式返回正常模式
- `i`当前位置插入 `a`追加插入 `I / A` 行首/行末插入
- `R`替换模式 `:`命令模式
- `v`可视模式 `V`可视行模式 `Ctrl+V `可视块模式
### 命令
- 保存：`:q`退出 `:w` 保存 `:saveas doc` 或 `:w doc` 另存为  
    `ZZ` 或 `:x` 保存并退出 `:qa!` 退出所有正在编辑的文件
- 切换：`:e doc`打开文件 `:e!` 放弃所有更改 `:ls`显示打开的缓存  
    `:bn/:bp/:b<num>` 切换文件，可加`！`  
    `:f/<C-g>` 显示文件名 `:f doc` 改名
- option：`:set number` 显示行号  
    `:set shiftwidth?` 显示缩进数 `:set shiftwidth=10` 设置 `:set shiftwidth&` 默认值  
    `:help <cmd>`显示帮助文档(like CTRL-A, i_CTRL-A(insert mode), index, 'number')
### 重复
- `.` 重复上次命令
- `N<cmd>`重复命令
- `N.` 重复N次
### 移动
- 基本移动: `hjkl` 左下上右
    `-` 上一行非空格 `+`下一行非空格
- 词： `w` 下一个词， `b` 词初， `e` 词尾 （词：小写：类似变量，字母数字下划线；大写：空格分隔英文）
- 行： `0` 行初 `$` 行尾 `^` 第一个非blank字符 `g_` 最后一个非blank字符
- 段： `{/}` 找到下一个空行
- 屏幕： `H` 屏幕首行， `M` 屏幕中间， `L` 屏幕底部
- 翻页： `Ctrl-u` 上翻 `Ctrl-d` 下翻
- 文件： `gg` 文件头， `G` 文件尾
- 行数： `:{行数}<CR>` 或 `{行数}G` `{0-100}%` 模糊位置
- 列数： `{列数}|`
- 跳转后`<C-o>`返回跳前位置 `<C-i>` 反向跳转
- 查找： `%` 找到配对 `*` / `#` 匹配光标对应单词下/上一个
    `f` / `t` / `F` / `T{字符}` 查找在本行字符，光标：`f`对应，`t`在前（不处理目标），`,/;`向前向后选择， **方向：小写向后，大写向前**
- 搜索: `/`或`?{字符串}` `<enter>`  
    `/` 向下 `?` 向上；`n`下一个 `N`上一个
### 编辑
**`{start移动命令}{编辑命令}{end移动命令}` 选择区域操作，start可选（start=光标位置）**
- `r{字符}` 替换光标字符
- `>> / <<`  缩进
- `o` / `O` 在下/上插入行，进入插入模式
- `d{移动命令}` 删除（剪切），如`dw` 删除词, `D=d$` 删除到行尾, `dd` 删除行并保存到剪切板
- `c{移动命令}` 改变，相当于`d{移动命令}` 再 `i` 如`cw` 改变词，`cc`替换行
- `x`=`dl` / `X=dh` 删除字符 大写删除游标前的字符
- `s` 替换字符（等同于 `xi`）
- `u/U` 撤销(大写表示整行), `<C-r>` 重做
- `y` 复制（其他一些命令比如 `d` 也会复制）
- `yy` 拷贝当前行，`p`/`P`粘贴下/上一行，类似于`ddp`交换2行位置
- `yaw` 复制当前单词(yank all word)
- `caw ciw` 改变当前单词(i不会多删除前面的空格)
- `p`/`P` 当前位置（方块光标）后/前粘贴
- `~` 改变字符的大小写 `g~~` 整行反转大小写 `guu/gUU` 整行大小写 可以用`guaw/gUiw`修饰语
- `J` 下一行连接到本行
### 修饰语
- `{action}N{a / i}{object}` 选择操作
    action=y / d / v / c
    N可认为嵌套数 a包含obj，i不含obj
    object=w 变量单词 W空格单词 s句子 p 段落；也可以时引号、括号等匹配

- `ci(` 改变当前括号内的内容
- `da'` 删除一个单引号字符串， 包括周围的单引号
### 自动补齐
`Ctrl+P` / `Ctrl+N`
### 宏
- `qa` 开始记录到寄存器a
- `q` 结束录制
- `@a` 回放宏a
- `@@` 回放最新的宏，和次数连用：`N@@`
- `<C-a>` 递增选择的数字
### 块操作（`<C-V>`可视模式）
`<` / `>` 左右缩进 `=` 自动缩进
在所有行的前面或后面添加同样的内容：使用`A`/`I`和`$`/`0`
### 分屏
- 启动：`vim -On file1 file2 ...` | `-o`垂直 `-O`水平
- 关闭窗口：`<C-w>c`
- 分屏：`<C-W>s/v` 垂直/水平分割当前文件 `:sp/vsp doc` 新文件
- `:new` 打开窗口
- 移动光标：`<C-w>hjkl/w` w下一个
- 移动分屏：`<C-w>HJKL`
- 交换窗口：`<C-w>r`
- 屏幕尺寸：`<C-w>=/+/-` `<C-w>_` 最大化窗口
### vscodevim
- `gd` / `gh` 跳转定义/提示
- `gt/gT` 跳标签页 `<M-num>` 直接选标签页
- `<C-0/1>`or`<C-shift-e>` 选择文件目录(Group0)或Group1
- `<space>/o|<Enter>/l` (预览模式)打开文件
- `gb` 多光标选中(可以多按几次)
### 其他
- `:s/old/new/g` 行内替换(最后的flag中g指行内所有匹配项，gc表示一一确认) `:#,#s/...` 行号范围内替换 `:%s/...` 整个文件替换
- `:!cmd` 执行外部命令
- `:r doc` 从doc中插入内容 `:r !ls` 相当于重定向
- `:set ic/noic/invic` (搜索时)忽略大小写ignorecase 类似的：incsearch=is hlsearch=hls
- `:h 'ruler'` option开关的帮助
- `<C-D>` 在`:!ls`等命令需要Tab时提示，与Tab连用
- 用||包围的为超链接，用`<C-]>`跳转
- `m[register]` 设置位置标记，`` `/' `` 返回跳转位置, `:marks` 显示所有标记 `'' '" '[ '] '.` 特殊标记位 `a-z` 文本内部 `A-Z` 跨文件 `0-9` 保存iminfo `:delm[arks] [reg]` 删除标记
- `colorscheme blue` 配色方案
- `:w|!sh %` 保存当前文件，并接着运行此shell脚本
- `z<Enter>` 当前行放到屏幕顶部
- `<C-f>/<C-b>/<C-y>/<C-e>` 翻页


# Linux


## basic

- cursor: block left: backspace or insert, block: replace  
    Ctrl+Z | cmd&: backend
    Ctrl+U: clear line  
    Ctrl+L | clear: clear screen  
    Ctrl+R 反向搜索模式，找到过去使用的命令
    Ctrl+B/F/P/N move crusor
    Ctrl+A/B
- `man | info cmd`
- `tldr cmd`
- `which | whereis` PATH / search path
- `less | more`
    - `b/f u/d j/k` 翻页
    - `/`向下搜索 `?`向上搜索 `n`下一个关键词 `N`上一个
- `#!/bin/sh` shebang
    - `#!/usr/bin/env bash(python)` is better
- `cat /etc/shells` 查看所有shell  
    `$SHELL` 查看默认sehll  
    `chsh -s /bin/zsh` 修改默认sehll
- `xdg-open [doc]` open with default app
- `find <dir> -path <path> -name/iname 'name' -type f -exec rm {} \;` 查找文件
    - `find . -type f \( -name "._*" -o -name ".DS_Store" \) -print -delete`
- `grep -R <pattern> <file>` 筛选所在行
    - `rg "pattern" -t py -C 5 <path>` 更好的展示

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
which cmd # find path in PATH
PATH=$PATH:/... # 追加
export PATH # 变为全局变量多用户使用
/etc/profile.d/texlive2023.sh
/etc/environment
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


## 文件

`curl -x http://127.0.0.1:7890 [-I] URL -o filename.iso [--silent]` -I 只请求http响应头，检查连通性
`ping -w 10 -c 5 www.google.com` 10s超时 5个icmp包
    `ping 127.0.0.1` `ping localhost`检查与本机的连接
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
`gzip`
    - `gzip -d` 解压，`-k`保留原文件
    - `gzip -c abc.txt > abc.txt.gz` 压缩并保留原文件
    - `gunzip -c abc.txt.gz > abc.txt` 解压并保留原文件
`ln [-s] f1 f2` f1源文件，f2目标文件

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


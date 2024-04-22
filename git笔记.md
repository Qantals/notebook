# git 命令

## 目录
- [配置](#配置)
- [本地仓库搭建](#本地仓库搭建)
- [文件状态](#文件状态)
- [远程仓库](#远程仓库)
- [分支命令](#分支命令)
- [标签](#标签)
- [忽略文件](#忽略文件)

## 配置
```bash
git config -l # 查看配置
git config --global --list # 查看当前用户（global）配置  
git config --global user.name "xiaolan" # 配置用户名  
git config --global user.email "2717110178@qq.com" # 配置邮箱
```

## 本地仓库搭建
```bash
git init
git clone # 克隆一个项目和它的整个代码历史
```

## 文件状态
```bash
Untracked, Staged, Unmodify, Modified # 后两个已commit

git add <文件名> # 把untracked或modified改为Staged
git add .
git commit [-m] [-a] # -a 连带未暂存文件一起提交

git reset HEAD <文件名> # 取消暂存（仍然tracked）  
git reset --hard <commit_id> # 工作区恢复到某个版本，<commit_id>可为 HEAD^^
git rm <文件名> # 不跟踪unmodify文件并删除（commit和working space）  
git rm --cache <文件名> # 不跟踪unmodify文件不删除（保留working space）
git checkout -- <文件名> # 把modified丢弃修改为unmodify（来自于storage或commit）

git diff <文件名> # 查看文件具体修改
git diff HEAD -- <file> # 查看文件在工作区和最新提交的修改

git status [<文件名>] # 查看[指定]文件状态 
# 红色：已修改/未暂存； 绿色：已暂存； 提交后则不显示

git log [--all] [--graph] [--pretty=online] [--abbrev-commit] # 查看日志，显示commit id
git reflog # 记录HEAD指针变化
```

## 远程仓库
```bash
git remote add <origin> <URL> # 添加仓库，一般远程仓库名origin  
git remote set-url <origin> <URL> # 重置URL  
# <https://github.com/user/repo.git> / <git@github.com:user/repo.git> (SSH) 

git remote [-v] # 查看远程仓库名[信息]
git remote rm <仓库名origin> # 解除与远程库绑定

git push [-u] <origin> <master> # 第一次用[-u]
git pull

git checkout -b <new分支名> origin/<new分支名> 在本地创建和远程分支对应的分支  
git branch --set-upstream-to=origin/<new分支名> <new分支名> 建立本地分支和远程分支的关联  
git push origin --delete <分支名> 删除远程分支

ssh-keygen -t rsa -C <email> # 建立ssh秘钥 or ~/.ssh/id_rsa.pub
```

## 分支命令
```bash
# 版本指针：`HEAD`为当前版本，`HEAD^^`为上2版本，`HEAD~5`为上5个`^版本
git branch [--list] # 列出本地所有分支（返回带*表示当前分支）  
git branch -r # 列出所有远程分支
git branch -M <old_branch> master # 重命名
git config --global init.defaultBranch master

git branch <分支名> # 新建分支但不切换
git checkout <分支名> | git switch <分支名> #切换分支
git checkout -b <分支名> | git switch -c <分支名> #新建分支并切换

git branch -d <分支名> #删除分支  
git merge <分支名> #合并指定分支到当前分支  
git merge --no-ff -m <message> <分支名> # 禁用fast mode来合并分支，可看出合并过程  
```

## 标签
```bash
git tag # 查看标签  
git tag -a <tagname> -m <message> [<commit_id>] # 在当前或指定commit打标签 
git show <tagname> # 查看标签信息  
git tag -d <tagname> # 删除标签

git push origin <tagname> # 推送标签
git push origin --tags # 推送全部本地标签
git push origin :refs/tags/<tagname> # 删除远程标签
```

## 忽略文件

在主目录下建立`.gitignore`文件，此文件有如下规则：

1. `#`为行注释 
2. 可以使用Linux通配符。例如∶星号`*`代表任意多个字符，问号`?`代表一个字符，方括号`[abc]`代表可选字符范围，大括号`{string1,string2……}`代表可选的字符串等。
3. 如果名称的最前面有一个感叹号`!`，表示例外规则，将不被忽略。
4. 如果名称的最前面是一个路径分隔符`/`，表示要忽略的文件在此目录下，而子目录中的文件不忽略。
5. 如果名称的最后面是一个路径分隔符`/`，表示要忽略的是此目录下该名称的子目录，而非文件（默认文件或目录都忽略）。

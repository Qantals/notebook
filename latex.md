## normal
```latex
\LaTeX \TeX
\␣ 插入间距
\TeX{} 花括号阻止其忽略空格
星号看作一种特殊的可选参数

环境：
\begin{⟨environment name⟩}[⟨optional arguments⟩]{⟨mandatory arguments⟩}
…
\end{⟨environment name⟩}

分组{}限制作用域

\documentclass[10pt,twoside,a4paper]{ctexart、ctexrep、ctexbook}
\usepackage{tabularx, makecell, multirow}
\include{chapters/file} % 相对路径，读入之前会另起一页
\input{⟨filename⟩} % 不会另起一页

\includeonly{⟨filename1⟩,⟨filename2⟩,…} % 不在其列表范围的 \include 命令不会起效

一行开头的空格忽略不计。
行末的换行符视为一个空格(分隔单词)
行末使用 \par 命令分段

转义
\^{} \~{} 避免重音
\textbackslash
\\手动换行
\\[⟨length⟩]
\\*[⟨length⟩] % 禁止分页
\newline % 只用于文本段落中

断页
\newpage
\clearpage

手动断词
\-

\verb|\\| % 原样输出

dif{}f{}icult % 连字

单引号 ‘ 和 ’ 分别用 ` 和 ' 输入；双引号 “ 和 ” 分别用 `` 和 '' 输入(" 可以输入后双引号)

连字号（hyphen）、短破折号（en-dash）和长破折号（em-dash）

\dots = \ldots 命令表示省略号

\P{} \S{} \dag{} \ddag{} % 章节

~ 输入一个不会断行的空格


```

## 文章结构
```latex
一般三级
\chapter{⟨title⟩}
\section[⟨short title⟩]{⟨title⟩} % 目录页眉页脚
\section*{⟨title⟩} % 无编号无页眉页脚
\subsection{⟨title⟩}
\subsubsection{⟨title⟩}
\paragraph{⟨title⟩}
\subparagraph{⟨title⟩}

\tableofcontents 生成目录

\appendix 命令将正文和附录分开

% 标题页
\title{⟨title⟩}
\author{\thanks{} \and } % \thanks表示脚注
\date{\today}
\maketitle

\bibliography{books} % 利用 BibTeX 工具从数据库文件 books.bib 生成参考文献

% 超链接引用
\label{⟨label-name⟩} % label=sec:this
\ref{⟨label-name⟩}
\pageref{⟨label-name⟩}

% 脚注
\footnote{⟨footnote⟩}
% 特殊环境下
\footnotemark
\footnotetext{表格里的名句出自《千字文》。}
\marginpar[⟨left-margin⟩]{\footnotesize right-margin} % 边注

% 列表
\renewcommand{\labelitemi}{\ddag}
\renewcommand{\labelitemii}{\dag} % 直到iv，定义无序列表符号
\begin{enumerate}
\begin{itemize} % 无序列表
    \item …
    \item[*] A starred item.
\end{enumerate}
\begin{description}
    \item[Enumerate] Numbered list.

% 对齐
\begin{center} … \end{center} % 这些环境和其他段产生间距
\begin{flushleft} … \end{flushleft}
\begin{flushright} … \end{flushright}
\centering % 这些命令不会产生特殊间距
\raggedright
\raggedleft % 命令单独一行，紧接着下一行作用

% 代码
\begin{verbatim}
\begin{verbatim*} % 特殊显示空格
\end{verbatim}
\verb⟨delim⟩⟨code⟩⟨delim⟩ % 简短模式，也可用\verb*显示空格

% 表格
\caption % 加标题
\begin{tabular}[⟨align⟩:t/b]{⟨column-spec⟩:|l/c/r|} % @{text} 插入任意内容 @{} 可直接用来消除单元格前后的间距
⟨item1⟩ & ⟨item2⟩ & … \\
\hline
\end{tabular}
重复的写法 *{⟨n⟩}{⟨column-spec⟩}
array 宏包提供了辅助格式 > 和 <，用于给列格式前后加上修饰命令
% 控制行距a
\renewcommand\arraystretch{1.8}
\\[6pt] % 在这一行下面加额外的间距
从第二行开始，表格的首个单元格不能直接使用中括号 []，应当放在花括号 {} 里面

% 重复
\newcommand\txt{a b c d e f g h i}

% 图片
建议使用 xelatex 命令
\usepackage{graphicx}
\includegraphics[⟨options⟩:key=value]{⟨filename⟩} % 图片文件的扩展名一般可不写
% 文件名不要有空格/点号
options=width, height, scale, angle(逆时针)
\graphicspath{{figures/}{logo/}} % 省写路径

% 浮动体，上下文隔离
\begin{table}[⟨placement⟩=htbp]
\begin{figure}[⟨placement⟩]
…
\end{table}
\caption{…} % 紧跟 \label 命令标记交叉引用
\caption*
caption包：修改 \figurename 和 \tablename
\listoftables
\listoffigures % 生成专门的目录
% 并排
\begin{figure}[htbp]
    \centering
    \includegraphics[width=...]{...}
    \qquad
    \includegraphics[width=...]{...} \\[...pt]
    \includegraphics[width=...]{...}
    \caption{...}
\end{figure}
```

## 公式
```latex
amsmath
% 行间公式：
\begin{equation}
a 2 + b2 = c 2
a^2 + b^2 = c^2 \label{pythagorean} | \tag{修改编号}
(4.1)
\end{equation}
引用：\eqref{pythagorean}有圆括号 \ref{pythagorean}
\[ 和 \] 包裹 | equation* 环境 | \notag % 没有编号

% 数学模式
\quad 和 \qquad \␣ \, \: \; \!(负间距) % 空格
\text{} \textbf{} \mathrm{} % 正体文本
\dots=\ldots(在下面) \cdots(居中)
f''^{2}(x) f'(x) % 导数
\dfrac(放大) 和 \tfrac(缩小) % 分式
\sqrt[3]{2}
自定义二元关系符的命令 \stackrel{*}{\approx}
\cdot % 点乘
\DeclareMathOperator{\argh}{argh} % 自定义算符
\DeclareMathOperator*{\nut}{Nut} % 带上下限
\sum\limits_{i=1}^n： \limits(上下) \nolimits(右上右下) % 巨算符上下标位置
\substack % 能够在下限位置书写多行表达式

一般应当对某个符号而不是“符号加下标”使用重音
\{ \} \langle \rangle \left( \right) 控制括号大小可变 % 不允许断行
有left就有right，所以单个界定符用点\left. \right|单个竖线
\big( \big)\bigg \bigl \biggl % 允许断行

% 公式对齐
\begin{align} % 不用eqnarray
a & = b + c \\
& = d + e
\end{align}
\notag 去掉某行的编号
align环境公式间可用&间隔
gather环境：不对齐多公式
aligned、gathered 等环境，与 equation 环境套用：多个公式组在一起公用一个编号
array，cases，matrix，bmatrix，vmatrix环境：数组和矩阵，分类

% 数学字体
\boldsymbol{M}
package{bm}: \bm{M}

```

## 字体
```latex
{\bfseries ⟨some text⟩} % 分组生效
\textbf{} % 参数生效
\fontsize{⟨size⟩}{⟨base line-skip⟩} % 需要 \selectfont 命令才能立即生效
OT1字体编码：大于号和小于号可用命令 \textgreater 和 \textless 输入
\usepackage[T1]{fontenc} % 切换编码 (from OT1)
如果使用 xelatex 编译方式，并使用 fontspec 宏包调用 ttf 或 otf 格式字体，就不要再使用 fontenc 宏包
xelatex, lualatex使用发行版ttf字体（linux的opentype-otf需要配置）
xelatex 和 lualatex 命令下支持用户调用字体的宏包是 fontspec
\setmainfont{⟨font name⟩}[⟨font features⟩]
\setsansfont{⟨font name⟩}[⟨font features⟩]
\setmonofont{⟨font name⟩}[⟨font features⟩]
font name = 字体的文件名（带扩展名）或者字体的英文名称
\setsansfont{Arial}[BoldFont={Arial Bold}, ItalicFont={Arial Italic}]

fontspec 宏包会覆盖数学字体设置，否则应当在调用 fontspec 宏包时指定 no-math 选项，
自动被ctex等调用时 \documentclass 命令里指定 no-math 选项

% 中文字体
\setCJKmainfont{⟨font name⟩}[⟨font features⟩]
\setCJKsansfont{⟨font name⟩}[⟨font features⟩]
\setCJKmonofont{⟨font name⟩}[⟨font features⟩]
\setCJKmainfont{SimSun}[BoldFont=SimHei, ItalicFont=KaiTi] % 匹配缺失格式
% unicode 数学字体
\usepackage{unicode-math}
\setmathfont{⟨font name⟩}[⟨font features⟩]

% 修饰
\underline{underlined}
ulem宏包\uline{} 可换行下划线
\emph % 强调
\emph里\emph换成直立体

% 行距
\newlength{\⟨length command⟩} % 定义
\setlength{\⟨length command⟩}{⟨length⟩} % 赋值
\addtolength{\⟨length command⟩}{⟨length⟩}
\linespread{⟨factor⟩} % 导言区，行距，分段\par生效
缺省的基础行距是 1.2 倍字号大小（参考 \font-size 命令
% 缩进
\setlength{\leftskip}{⟨length⟩}
\setlength{\rightskip}{⟨length⟩}
\setlength{\parindent}{⟨length⟩}
\setlength{\parskip}{<length>} % 段落垂直间距
段落开头使用，使用多个 \indent 命令可以累加缩进量
\indent
\noindent
默认在 \chapter、\section 等章节标题命令之后的第一段不缩进。（ctex不是！）
如果不习惯这种设定，可以调用 indentfirst 宏包
\hspace{1.5cm} % 水平间距
\hspace* % 不会因断行消失

% 页面参数
\usepackage{geometry}
\geometry{⟨geometry-settings⟩}
或 \usepackage[⟨geometry-settings⟩]{geometry}
\geometry{a4paper,left=1.25in,right=1.25in,top=1in,bottom=1in}
% 文档类\documentclass{}设置的是输出区域，\geometry{}是PDF纸张
\raggedbottom % 垂直方向顶部对齐
\flushbottom % 垂直方向分散对齐

% 分栏
\onecolumn
\twocolumn[⟨one-column top material⟩]
在双栏模式下使用 \newpage 会换栏而不是换页；\clearpage 则能够换页。
\begin{multicols}{3} % multicol方案
...
\end{multicols}

% 页眉页脚
\pagestyle{⟨page-style⟩}
\thispagestyle{⟨page-style⟩=headings/myheadings}
\markright{⟨right-mark⟩}
\markboth{⟨left-mark⟩}{⟨right-mark⟩}

twoside/oneside
\pagenumbering{⟨style⟩} % 页码样式
fancyhdr宏包
```

## 特色
```latex





```


## 宏包
```latex
xeCJK
syntonly % 只检查错误不生成pdf
fontspec % 选用字体
titlesec % 章节定制格式
makeidx % 用来处理索引
enumitem % 定制列表
array % 生成列表
tabularx % 列表对齐
booktabs % 三线列表
graphicx % 图片
float % 浮动体
multicol % 分栏
caption
subcaption
fontspec % 字体
ulem % 下划线
layout % 页边距
geometry % 页面参数
fancyhdr % 页眉页脚


```

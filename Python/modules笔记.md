# modules 笔记

## TOC

- [argparse](#argparse)
- [文件操作](#文件操作)
    - [os](#os)
    - [glob_shutil_pathlib](#glob_shutil_pathlib)
    - [sys](#sys)
- [输出显示](#输出显示)
    - [tqdm](#tqdm)
    - [time_datetime](#time_datetime)
    - [termcolor](#termcolor)
    - [logging](#logging)
- [数据处理](#数据处理)
    - [json](#json)
    - [csv](#csv)
    - [pandas](#pandas)
- [re](#re)
- [multi_process](#multi_process)
- [others](#others)

## argparse
```py
import argparse
parser = argparse.ArgumentParser(description='命令行中传入一个数字') # '-h'/'--help' 提示
parser.add_argument('integers', nargs=1, help='传入的数字') # 位置参数
# nargs= '+'1个或多个 '*'0个或多个
parser.add_argument('-f','--family', type=str, required=False, default='张') # required可选参数
parser.add_argument('--cpu', action='store_true'/'store_false') # 不指定参数,返回的bool值为False/True
# 传list
parser.add_argument('--list', nargs='+', required=True) # --list 1 2 3
parser.add_argument('--ll', action='append', required=True) # --ll 1 --ll 2 --ll 3
args = parser.parse_args()
args.f | args.cpu
print(args.integers)
print(vars(args))
# subparser
def add(args): args.x args.y ...
parser = argparse.ArgumentParser(description)
subparsers = parser.add_subparsers(dest='mode',help='sub-command help') # dest=属性名称即第一参数，help info
parser_a = subparsers.add_parser('add') # use like: python test.py add -x 1 -y 2 
parser_a.add_argument('-x', type=int, help='x value')
parser_a.set_defaults(func=add)
args = parser.parse_args()
# 直接用参数执行函数
args.func(args) # 1
if args.mode == 'add': add(args) # 2
```


## 文件操作

### os
```py
# python中脚本内的路径以终端的工作目录为基础！
# 如save到'./'下，不保存到脚本所在路径，而是工作目录下！
os.getcwd() # 当前终端路径--工作目录
script_dir = os.path.dirname(os.path.abspath(__file__)) # __file__=脚本文件路径=终端路径+运行解释器输入的路径
# sys.path[0] 运行py文件所在目录，不建议
os.chdir(path) # 修改路径
list=os.listdir(path) # 目录内容，包括文件夹
os.path.exists(path)
os.path.isdir(path)
os.path.join(str1,str2) # 连接路径
os.mkdir() os.makedirs(path, mode=0o777, exist_ok=True) # 后者递归创建 mkdir -p

list=os.path.splitext(str) # 返回root（除.ext的所有部分）和扩展名.ext
os.path.dirname(str) # 返回路径头部
os.path.basename(str) # 返回文件名或文件夹名（路径尾部）
os.path.split(str) = (basename, dirname)
filelist = os.walk(path) # 遍历所有子文件夹，返回生成器返回(root, dir, doc)后二者为list，root为当前路径。遍历下一个则选择为子文件夹
os.path.abspath() # 得到绝对路径（根据当前os.getcwd()）
os.mknod("test.txt") # 创建空文件

int=os.getpid()
os.system(str)

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
```

### glob_shutil_pathlib
```py
import glob
list=glob.glob(r"/home/qiaoyunhao/*/*.png") # 搜索所有匹配项
f = glob.iglob(r'../*.py') # 返回generator

import shutil
shutil.copy("file_path", "dir_path") shutil.copytree()
shutil.move() os.rename("oldname", "newname")
shutil.rmtree() os.remove("file")
shutil.make_archive(base_name, 'gztar', root_dir, [base_dir]) # base_name目标文件名, root_dir打包路径
shutil.unpack_archive(filename[, extract_dir[, 'gztar']])

from pathlib import Path
file = Path.cwd() # file为对象，使用str(file)转换
Path(__file__) Path('subdir/demo_02.py')
# 路径
file.resolve() # 转化成绝对路径
file.stat().st_size # 文件属性
file.name .stem .suffix .parent # 文件名 无扩展名 扩展名 父目录
file.resolve().parents[4] # 多级父目录
# 文件查找
file.iterdir() # 目录下所有文件（夹）
file.is_dir() is_file() .exists
    # [f.suffix for f in path.iterdir() if f.is_file()]
list(cwd.glob('*.txt')) # glob返回生成器
list(cwd.rglob('*.txt')) # 递归查找
bool = file.match('*.txt') # 规则匹配
# 路径拼接
Path.home() / 'dir' / 'file.txt'
Path.home().joinpath('dir', 'file.txt')
# 文件操作
Path('hello.txt').touch(exist_ok=True) # exist_ok文件存在，则不报错
path.mkdir(parents=True)
path.rmdir()
with open(file) as f: with file.open() as f:
```

### sys
```py
sys.argv # 命令行参数 ['script_name',arg1,...]
list=sys.path # python搜索库的目录，第一个为运行目录
sys.path.append(dir) # 对list调用方法
```


## 输出显示

### tqdm
```py
# tqdm(iterator)
import time
from tqdm import tqdm, trange
for i in trange(100):
for i in tqdm(range(100), desc='Processing'):
    time.sleep(0.05)
pbar = tqdm(['1','2','3'])
for i in pbar:
    pbar.set_description('Processing '+i)
    time.sleep(0.2)
# manually update
with tqdm(total=200) as pbar:
    pbar.set_description('Processing')
    for i in range(20):
        time.sleep(0.1)
        pbar.update(10)
tqdm(leave=False, unit='it', unit_scale=False)
```

### time_datetime
```py
import time
time.sleep(sec)
timestamp = time.time() # 浮点数的秒表示

from datetime import datetime
str = datetime.now().strftime('%Y/%m/%d_%H:%M:%S')
datetime.datetime.fromtimestamp(timestamp)
str(timedelta(seconds=timestamp1-timestamp2)) # 时间换算

from timeit import Timer
t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "milliseconds")
```

### termcolor
```py
from termcolor import colored, cprint
text = colored(text, color, on_color, attrs) # 可以用list of str表示组合
print(text)
# 文本颜色：'grey', 'red', 'green', 'yellow', blue, magenta, cyan, white
# 背景颜色：on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white
# 文本属性：bold, dark, underline, blink, reverse, concealed
cprint(text, color, on_color, attrs, **kwargs) # 直接打印
```


### logging
```py
import logging
# functional
logging.basicConfig(level=logging.NOTSET,format='%(asctime)s - %(levelname)s - %(name)s - %(message)s') # 低于该级别的日志将不输出 name为logger名
dict = logging._nameToLevel ._levelToName
# {'CRITICAL': 50, 'FATAL': 50, 'ERROR': 40, 'WARN': 30, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}
# CRITICAL=FATAL, WARNING=WARN 用前面的更好
logging.debug("This is a %s message.",logging.getLevelName(logging.DEBUG))
logging.info(logging.BASIC_FORMAT)
logging.log(level=logging.INFO, msg="This ia a message from logging.log().")

# logger记录器
logger = logging.getLogger(__name__) # module名
logger.setLevel(level = logging.INFO)
logger.info("Start print log")
    # using file/stream
handler = logging.FileHandler("log.txt") | StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'[,
    datefmt = "%Y/%m/%d %H:%M:%S"]
)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Start print log")

# exception
logging.exception(obj)
```


## 数据处理

### configparser
INI file-like

```py
import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['forge.example'] = {}
config['forge.example']['User'] = 'hg'
with open('example.ini', 'w') as configfile:
  config.write(configfile)

config.read('example.ini')
config.sections() # see parsed args
# use like dict
# manually converts datatype

```

### json
```py
import json
dict/list = json.load(file)
str = json.loads(file)
json.dump(dict,file,indent=4)
str=json.dumps(dict)
```

### yaml
```py
import yaml
with open('./yamlData.yml', 'r', encoding='utf-8') as f:
    result = yaml.load(f.read(), Loader=yaml.FullLoader) # 结果和json相似
    result = yaml.load_all(f.read(), Loader=yaml.FullLoader) # yaml的多组数据，返回generator
with open('./writeYamlData.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, stream=f, allow_unicode=True)
    yaml.dump_all(documents=[apiData1, apiData2], stream=f, allow_unicode=True)
```

### csv
```py
import csv
with open('test1.csv','rt') as f:
    cr = csv.reader(f)
    cr = csv.DictReader(f)
    cr.fieldnames # 表头
    for row in cr: # 返回row为list/dict
with open('1.csv','wt') as f2:
    # list
    cw = csv.writer(f2,delimiter=',',)
    cw.writerows(list) # 将嵌套列表内容写入
    for item in list:
        cw.writerow(item) # 写到csv文件的一行
    # dict
    cw = csv.DictWriter(f2,fieldnames=list)
    cw.writeheader() # 将fieldnames写入标题行
    cw.writerows(list_of_dict)
```

### pandas
```py
import pandas as pd
# series
s = pd.Series([1, 3, 5, np.nan, 6, 8]) # like list, different type
# DataFrame
df = pd.DataFrame(ndarray, index, columns=['a','b']) # 行,列索引
df = pd.DataFrame(dict)
df2.dtypes # 不同列的类型
# View
df.head() | df.tail(3) # 返回前/后几行
df.index | df.columns # 行/列索引
df.to_numpy()
df.describe() # show summary
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by="B")
# selection
df["A"] | df[0:3] | df["20130102":"20130104"] # index
df.loc[ : ,["A","B"]] # 标签索引
df.at[dates[0], "A"] = df.loc[dates[0],"A"] # 定位标量
df.iloc[ : ,2] # index索引
df.iat[1,2] = df.iloc[1,2]
list = df.values # 也可能是嵌套列表
df[df["A"] > 0] # bool indexing
df2[df2["E"].isin(["two", "four"])] # isin
s.value_counts() # counting
# csv
df.to_csv("foo.csv")
df = pd.read_csv("girl.csv", sep=',') # 返回DataFrame
df.to_excel(path, sheet_name="data")
```

## re
```py
import re
line_words = re.split('=|#|\s', line)  # split the line into words with splitor '=', '#', and whitespaces(won't leave spliters)
line_words = list(filter(None, line_words))  # filt out the whitespaces
```

## multi_process
```py
# psutil硬件信息
import psutil
psutil.cpu_count(logical=bool) # CPU逻辑数/物理核心数
psutil.cpu_percent(interval=0.5, percpu=True) # CPU使用率
# multiprocessing
import multiprocessing as mul
    # normal
p1 = mul.Process(target=function,args=tuple)
p1.start()
p1.pid
p1.join() # wait till finish
p1.is_alive()
    # pool
pool = mul.Pool(processes = mul.cpu_count()) # 线程数=12
res = pool.map(target = function_name, args = function_parameter) # 主线程阻塞等待，否则map_async()
pool.close() # 不接受新进程
pool.join()
```


## others
```py
# copy
import copy
copy.deepcopy()
# inspect
import inspect # 获取函数参数信息
list=inspect.getfullargspec(function).args # 函数参数的名称
# uuid
import uuid
str=uuid.uuid4() # generate from random
# skimage(图像处理)
from skimage.metrics import normalized_root_mse # NRMSE
nrmse_value = normalized_root_mse(img1.flatten(), img2.flatten(),normalization='min-max')
# scipy
from scipy.stats import wasserstein_distance # 概率分布距离
from scipy.interpolate import make_interp_spline # b-spline插值
import scipy.io as spio
A = spio.loadmat('a.mat')['A'] # 加载matlab的.mat文件
# mmcv(openMMlab机器视觉)
from mmcv import scandir
# scikit-learn(机器学习)
from sklearn.metrics import accuracy_score, roc_curve, confusion_matrix
# collections
from collections import Counter
Counter([1,1,1,0,1,0,0,...]) = Counter({1: 3226, 0: 3162})
# platform
import platform
platform.system().lower() == 'windows'
# typing
from typing import List, Tuple, Dict
def fun1(a0: int, s0: str, f0: float, b0: bool) -> Tuple[List, Tuple, Dict, bool]:
def func(a: int,b: str) -> List[int or str]:
# soundfile
import soundfile as sf
samples, sample_rate = soundfile.read(file, dtype='float32')
# int类型看取值范围，float归一化
# sample.shape=(length, channel) 可以直接plot
```



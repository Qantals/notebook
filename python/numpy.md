# numpy


## content
- [others](#others)
- [array](#array)
- [index](#index)
- [calculation](#calculation)
- [statistics](#statistics)
- [iteration](#iteration)


## others
```py
# 小数
np.spacing(1) # eps
np.pi
np.around(a,decimals) # 舍入到指定位

# 随机数
np.random.choice(a, size=None, replace=True, p=None) # need 1-D array
np.random.randn(shape) # 标准正态分布随机数
np.random.rand(shape)=np.random.random(shape) # 均匀分布
np.random.randint(low, high, size) # 整数

# 文件
np.save(file, arr) # file为.npy文件
b = np.load('outfile.npy')
np.loadtxt(FILENAME, dtype=int, delimiter=' ')
np.savetxt(FILENAME, a, fmt="%d", delimiter=",")
```


## array
```py
# ndarray
a = np.array([1,2,3],dtype=float,ndmin=2)
a.astype(np.float32)

# property
a.ndim # 维度数
a.shape # (a,b,c)-->深度，行数，列数，在前面加，对应最前面的是axis=0
a.size # 元素个数

# dimension
a = a.reshape((1,5)) # 可能返回引用 dimension=-1:自动推断
np.squeeze() # 去除长度为1的维度
a.flatten(order='C') # 展开的拷贝
a.ravel(order='C') # 展开的引用

# 创建数组
zeros(shape) ones(shape) eye(num)

numpy.arange(start, stop, step, dtype)
np.r_[start:stop:step] # equals to arange(), because slice is different from list/array
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
np.meshgrid(array1,array2)

# concatenate
numpy.concatenate((a1, a2, ...), axis)
np.vstack(a,b) np.r_[a,b]
np.hstack(a,b) np.c_[a,b]
numpy.tile(A , reps) # 扩展成reps个，可用tuple表示

# split
numpy.split(ary, indices_or_sections, axis) # arg2: integer or array
np.hsplit(harr, 3)
np.vsplit(a,2)
```


## index
- 返回引用：slice切片
- 返回新对象：2-D用`a[1]`
- 整数索引和slice混合：降维
- bool类型可被mean()视为0和1计算
```py
a[1] # 2-D取行向量，构造新的对象
a[1,2]=a[1][2] # 2-D取元素，former is faster
a[:,1:3] # 2-D取子阵
# 降维(删axis)
a[:,1] # 2-D降维
a[:,[1]] # 2-D不降维
# 数组索引
a[[1,1,3]]=[a[1],a[1],a[3]] # 1-D数组索引
a[[[1,1],[2,3]]]=[[a[1],a[1]],
                    [a[2],a[3]]] # 1-D数组索引，同形状
a[[1,3],[2,5]]=[a[1,2],a[3,5]] # 2-D数组索引，一一对应
ix_(a,b) # 笛卡尔积a列扩展，b行扩展 得到meshgrid
# bool
y[y>20]=y[np.nonzero(y>20)]
```
`a=a[None,...]`加一个轴
`a[-1:]`用slice取最后一个元素


## calculation
```py
a.dot(b) np.dot(a,b) a @ b # 一维向量点积/矩阵乘法

numpy.vdot(a,b) a * b # 矩阵对应元素相乘求和
numpy.linalg.det() # determinant
numpy.linalg.inv() # 逆矩阵
np.linalg.solve(A,b) # solve Ax=b
a.T  a.transpose(1,2,0) # (1,2,0)->(0',1',2') 输入参数为原轴，'表示新轴表示映射位置，则把原来的第0轴放最后

logical_and(a,b) # compare elementwise
a & b np.bitwise_and() np.bitwise_or()# compare bitwise
np.invert() ~ # bin()前面的符号表示符号位扩展省略
np.left_shift() np.right_shift()
```


## statistics
```py
np.nonzero(a>5) # 返回2个array表示各维度坐标
np.flatnonzero() # 线性索引

# elementwise
np.square() sqrt() abs() maximum()
# universal functions
np.mean() sum() max()

np.sort(a,axis) a.sort()
# arguments
numpy.argmax(a,axis) # get index
numpy.argmin(a,axis)
np.argsort()
```


## iteration
- 默认存储顺序读(a和a.T一样)
```py
a.copy(order) # 改变存储顺序
for x in np.nditer(a,order='C'): # 不同遍历顺序
for x in np.nditer(a,flags=['external_loop']): # 返回整列而不是一个元素
for row in a: # a为2维数组就迭代行数组
for element in a.flat: # 迭代元素，默认C-order
```

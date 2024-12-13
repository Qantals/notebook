# Matplotlib


## content
- [subplot](#subplot)


## helper function
```py
def plot_xx(x,y,ax=None):
    if not ax:
        ax=plt.subplot()
    ax.plot(x,y)
    return ax
```


## subplot
```py
fig = plt.figure(num, figsize=(width, height))
    # num starts from 1
fig, axs = plt.subplots(nrows, ncols, sharex, sharey) # ax = fig.subplots()
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # axs is group of axes
ax = fig.add_subplot(nrows, ncols, index) # optional: index=(first, last) compose unequal subfig
    # plt.subplot(nrows, ncols, index)
figL, figR = fig.subfigures(1, 2)
```


## properities
```py
ax.set(xlim, title, ylabel, xlabel)
myfont = mpl.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.rcParams['font.family'] = ['Heiti SC']
mpl.rcParams.update({'font.family':'Times New Roman','mathtext.fontset':'stix'})
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams.get('figure.figsize')
```


## plot
```py
l.set_linestyle(':') # OOP
```


## image
```py
img = mpl.image.imread('lena.png')
ax.imshow(array, cmap='gray', interpolation='bilinear', aspect='auto') # MxNx3
plt.imsave('lena.png', img, vmin, vmax, cmap)
```


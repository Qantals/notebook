# Matplotlib


## content
- [subplot](#subplot)


## subplot
```py
fig = plt.figure(num, figsize=(width, height)) # activate a figure
    # num starts from 1
    # figure size unit is "inch"
fig, axs = plt.subplots(nrows, ncols, sharex, sharey) # fig.subplots()
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) # axs is group of axes
ax = fig.add_subplot(nrows, ncols, index) # optional: index=(first, last) compose unequal subfig
    # plt.subplot(nrows, ncols, index)
    # starts from 1
fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained') # 复杂子图构型
    # axd['upleft'].set_title('upleft') # axd is dict of axs
figL, figR = fig.subfigures(1, 2)
fig = plt.gcf()
ax = plt.gca()
```


## properities
```py
ax.set(xlim, title, ylabel, xlabel)
myfont = mpl.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf')
plt.rcParams['figure.figsize'] = (10.0, 8.0)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
```


## plot
```py
l, = ax.plot(x,y,label='line1', color='blue', linewidth=3, linestyle='--', marker='o', markersize=12)
    # linewidth is pt unit
    # x,y: np.ndarray is preferred
ax.plot('x', 'y', data=dict|DataFrame)
l.set_linestyle(':') # another styling artists
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
n, bins, patches = ax.hist(arr, bins=10, normed=0, facecolor='black', edgecolor='black', histtype='bar')
ax.legend()
ax.legend(['l1', 'l2'])
```


## color plot (3D)
```py
pc = ax.pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=ax, extend='both')
co = ax.contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
pc = ax.imshow(Z**2 * 100, cmap='plasma', norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
pc = axs.scatter(data1, data2, c=data3, cmap='RdBu_r')
```


## annotation
```py
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
```


## text
```py
fig.suptitle('Figure') # don't use this for one axes
ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium') # plt.title()
ax.set_xlabel('x-label', loc) # plt.xlabel()
t = ax.text(x, y, r'$\mu=115,\ \sigma=15$')
ax.grid(True)
```


## axis
```py
ax.axis([xmin, xmax, ymin, ymax])
ax.axis(False)
ax.set_xlim(-2, 2) # plt.xlim
ax.set_xticks(np.arange(3), ['l1', 'l2', 'l3'])
ax.set_xticks([x1, x2, x3])
ax.set_xticks([]) # remove
ax.twinx() # secondary axis
ax.set_yscale('log')
```


## save
```py
fig.savefig('./name.png', dpi=300, bbox_inches='tight')
plt.show()
plt.close(fig)
```


## image
```py
img = mpl.image.imread('lena.png')
ax.imshow(array, cmap='gray', interpolation='bilinear', aspect='auto') # MxNx3
plt.imsave('lena.png', img, vmin, vmax, cmap)
```


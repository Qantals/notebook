from matplotlib import pyplot as plt

import pandas as pd
import os

def tensorboard_smoothing(x,smooth=0.60):
    x = x.copy()
    weight = smooth
    for i in range(1,len(x)):
        x[i] = (x[i-1] * weight + x[i]) / (weight + 1)
        weight = (weight + 1) * smooth
    return x

def draw(filename, smooth, fontsize):
    len_mean = pd.read_csv(filename)

    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Times New Roman'
    plt.rcParams.update({'font.size': fontsize})

    fig, axs = plt.subplots()

    axs.spines['top'].set_visible(False)
    axs.spines['right'].set_visible(False) 

    axs.set_title("Cosine Annealing", fontsize=fontsize)
    axs.set_xlabel("iters", fontsize=fontsize)
    axs.set_ylabel("learning rate", fontsize=fontsize)
    # axs.plot(len_mean['Step'], tensorboard_smoothing(len_mean['Value'], smooth=smooth), color="red",label='all_data')
    axs.plot(len_mean['Step'], tensorboard_smoothing(len_mean['Value'], smooth=smooth), color="red")
    # plt.legend(loc = 'lower right')
    fig.savefig(filename.replace(os.path.splitext(filename)[1], '.eps'), bbox_inches='tight', format='eps')


if __name__ == '__main__':
    draw(filename="run-log-tag-Train_lr.csv", smooth=0.60, fontsize=14)

 
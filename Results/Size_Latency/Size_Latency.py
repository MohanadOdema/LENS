import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

index = ['input', 'Conv1', 'Pool1', 'Conv2', 'Pool2', 'Conv3', 'Conv4', 'Conv5', 'Pool5', 'FC6', 'FC7', 'FC8', 'prob']

Latency = [0.03, 10.15, 2.256, 12.256, 1.784, 7.757, 6.936, 5.313, 1.163, 30.594, 15.764, 5.239, .761]
Size = [1, 7.536, 1.816, 4.843, 1.123, 1.684, 1.684, 1.123, 0.239, .106, .106, .026, .026]

#Random, Unnormalized,Normalized

plt.rc('xtick', labelsize=11)
plt.rc('ytick', labelsize=10)


fig, ax1 = plt.subplots()

width = 0.1
pos = np.array([0, .3, .6, .9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 3.6])

#ax1.grid(linestyle='dotted', zorder = 0)

color1 = '#B6BBD3'
color2 = '#223071'
#ax1.set_facecolor('whitesmoke')

ax1.set_xticks(pos+width/2)
ax1.set_xticklabels(index, minor=False, fontsize = 10, rotation = 60)

#ax1.set_xlabel(r'Confidence threshold $\sigma$', fontsize = 13)
ax1.set_ylabel('Size Change', color= '#8E92A4', fontsize = 10)
x1 = ax1.plot(pos, Size, width, color = color1, label = 'Size Change')
xbar1 = ax1.bar(pos, Size, width, color = 'whitesmoke', label = 'Size', hatch = '\\\\', edgecolor = color1)
ax1.tick_params(axis='y', labelcolor = '#8E92A4')

ax2 = ax1.twinx()
ax2.set_ylabel('Total Latency (%)', color=color2, fontsize = 10)
xbar2 = ax2.bar(pos+width, Latency, width, color=color2, label = 'Total Latency (%)', hatch = '.....', edgecolor = 'white')
ax2.tick_params(axis='y', labelcolor=color2)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

#x = x1 + x2
#labs = [l.get_label() for l in x]
#ax1.legend(x, labs, fontsize=9, framealpha=1)

plt.show()
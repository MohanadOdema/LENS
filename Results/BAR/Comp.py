import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

index = ['Err<25', 'Err<20', 'Ergy<250', 'Ergy<200', 'Err<30 &\nErgy<250', 'Err<25 &\nErgy<300', 'Err<25 &\nErgy<250']

trad= [79, 6, 79, 10, 27, 9, 1]
Lens = [67, 7, 156, 40, 53, 6, 1]

#Random, Unnormalized,Normalized

plt.rc('xtick', labelsize=11)
plt.rc('ytick', labelsize=10)
plt.rcParams["font.family"] = "Times New Roman"

order = [0, 5, 6, 1, 3, 4, 2]

index = [index[i] for i in order]
trad = [trad[i] for i in order]
Lens = [Lens[i] for i in order]

fig, ax1 = plt.subplots()

width = 0.075
pos = np.array([0, .25, .5, .75, 1, 1.25, 1.5])

ax1.grid(linestyle='dotted', axis='both', zorder = 0)

color1 = '#2F53E2'
color2 = '#97989C'
#ax1.set_facecolor('whitesmoke')

ax1.set_xticks(pos+width/2)
ax1.set_xticklabels(index, minor=False, fontsize = 10, rotation = 15)

#ax1.set_xlabel(r'Confidence threshold $\sigma$', fontsize = 13)
ax1.set_ylabel('#Architectures', color= 'black', fontsize = 12)
#x1 = ax1.plot(pos, trad, width, color = color1, label = 'Traditional')
xbar1 = ax1.bar(pos+width, Lens, width, color = 'whitesmoke', label = 'Partition within Optimization', hatch = '/////////', edgecolor = color1)
xbar2 = ax1.bar(pos, trad, width, color=color2, label = 'Partition after Optimization', hatch = '.....', edgecolor = 'black')
ax1.tick_params(axis='y', labelcolor = 'black')

plt.ylim(0, 180)
'''
ax2 = ax1.twinx()
ax2.set_ylabel('Total Latency (%)', color=color2, fontsize = 10)
xbar2 = ax2.bar(pos+width, Latency, width, color=color2, label = 'Total Latency (%)', hatch = '.....', edgecolor = 'white')
ax2.tick_params(axis='y', labelcolor=color2)
'''
fig.tight_layout()  # otherwise the right y-label is slightly clipped

ax1.legend(loc="upper center", fontsize='11', framealpha=1)

plt.show()
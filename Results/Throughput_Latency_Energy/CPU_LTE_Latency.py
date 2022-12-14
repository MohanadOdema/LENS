import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

index = ['1', '5', '15', '30']

allCloud = [1.233,.247,.082,.041]
allEdge = [.244,.244,.244,.244]
Pool = [.405,.169,.130,.120]
FC = [.315,.210,.193,.189]

#Random, Unnormalized,Normalized

fig = plt.figure()
ax = fig.add_subplot(111)

pos = np.array([0.2, .7, 1.2, 1.7])
    
width = 0.1 # the width of the bars 
#ind = np.arange(len(index))  # the x locations for the groups

ax.bar(pos, allCloud, width, color='white', label='All-Cloud', hatch = 'oooooo', edgecolor = '#96BED3', zorder = 3)
ax.bar(pos+width, Pool, width, color='#8ABCD6', label='Pool5', hatch = '......', edgecolor = 'black', zorder = 3)
ax.bar(pos+2*width, FC, width, color='#4FA8D5', label='FC6', hatch = 'oooo', edgecolor = 'black', zorder = 3)
ax.bar(pos+3*width, allEdge, width, color='#1093D5', label='All-Edge', hatch = 'oooooo', edgecolor = 'black', zorder = 3)

ax.grid(axis='y', zorder = 0)

ax.set_xticks(pos+3*width/2)
ax.set_xticklabels(index, minor=False, fontsize = 10)
#ax.set_yticklabels([0, 25, 50, 75, 100, 125, 150, 175, 200], minor=False, fontsize = 11)
#plt.rc('ytick', labelsize=12)
#ax.set(xlim=[2*width - 1, len(index)], ylim=[0,200])
ax.set(xlim=[0, 2.2])


#ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#          ncol=4, frameon = False)

plt.xlabel('Throughput (Mbps)', fontsize = 11)
plt.ylabel('Latency (s)', fontsize = 11)  

plt.show()
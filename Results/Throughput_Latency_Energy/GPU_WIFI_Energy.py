import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

index = ['1', '5', '15', '30']

allCloud = [.513,.382,.360,.355]
allEdge = [.194,.194,.194,.194]
Pool = [.215,.184,.179,.177]
FC = [.203,.189,.187,.186]

#Random, Unnormalized,Normalized

fig = plt.figure()
ax = fig.add_subplot(111)

pos = np.array([0.2, .7, 1.2, 1.7])
    
width = 0.1 # the width of the bars 
#ind = np.arange(len(index))  # the x locations for the groups

ax.bar(pos, allCloud, width, color='white', label='All-Cloud', hatch = 'oooooo', edgecolor = '#D6B3A1', zorder = 3)
ax.bar(pos+width, Pool, width, color='#D69472', label='Pool5', hatch = '......', edgecolor = 'black', zorder = 3)
ax.bar(pos+2*width, FC, width, color='#D6703B', label='FC6', hatch = 'oooo', edgecolor = 'black', zorder = 3)
ax.bar(pos+3*width, allEdge, width, color='#D35310', label='All-Edge', hatch = 'oooooo', edgecolor = 'black', zorder = 3)

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
plt.ylabel('Energy (J)', fontsize = 11)  

plt.show()
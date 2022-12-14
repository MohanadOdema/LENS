import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

from scipy.interpolate import make_interp_spline, BSpline


th_energy = 6.773
th_latency = 22.779

df1 = pd.read_excel(r'throughput.xlsx')

tu = []
tu = df1['tu_energy'].to_list()[:40]



A_energy = []
A_energy_edge = []
A_energy_split = []

A_acc_energy = []
A_acc_energy_split = []
A_acc_energy_edge = []


'''x_new = np.linspace(0, 500 ,50)
spl = make_interp_spline(np.asarray(p_frontX_lens), np.asarray(p_frontY_lens), k=3)
energy_lens_smooth = spl(x_new)'''

for throughput in tu:

	energy_edge = 279.534/1000
	energy_split = ((483.39*throughput + 1288.04)*((18816*8)/(throughput*1000000)) + 178.04)/1000
	A_energy_edge.append(energy_edge)
	A_energy_split.append(energy_split)
	if throughput > th_energy:
		A_energy.append(energy_split)
	else:
		A_energy.append(energy_edge)	


i = 0
while(i<len(A_energy)):
	A_acc_energy.append(sum(A_energy[:i+1]))
	A_acc_energy_split.append(sum(A_energy_split[:i+1]))
	A_acc_energy_edge.append(sum(A_energy_edge[:i+1]))

	i = i+1


	
plt.rcParams["font.family"] = "Times New Roman"
fig, ax1 = plt.subplots()

ax1.grid(linestyle='dotted', axis='both', zorder = 0)
ax1.set_facecolor('#F7F7F7')
ax1.set_xlabel('Sample no.', color='#110f0e', fontsize = 12)


ax1.set_ylabel('Throughput (Mbps)', color= '#110f0e', fontsize = 12)
x1 = ax1.plot(tu, linewidth = 1, c = '#110f0e', label = 't_{u}')

plt.hlines(y=th_energy ,xmin=0, xmax=40, linestyles = 'dashdot', color='#110f0e')
#ax1.axhspan(0, th_energy, facecolor='green', alpha=0.5)
#ax1.axhspan(th_energy, 25, facecolor='yellow', alpha=0.5)

ax2 = ax1.twinx()
ax2.set_ylabel('Energy (J)', color= '#694C40', fontsize = 12)
ax2.tick_params(axis='y', labelcolor='#694C40')
x2 = ax2.plot(A_acc_energy, '-', linewidth=2, color = '#966D5C', label='Dynamic')
x2 = ax2.plot(A_acc_energy_edge, linestyle=':', linewidth=2, color = '#966D5C', label='All-edge')
x2 = ax2.plot(A_acc_energy_split, '-.', linewidth=2, color = '#966D5C', label='Partitioned')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, frameon = False, fontsize = 11)

print(A_acc_energy[-1], A_acc_energy_split[-1], A_acc_energy_edge[-1])

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
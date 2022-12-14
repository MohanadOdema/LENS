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
tu = df1['tu_latency'].to_list()[:40]

B_latency = []
B_latency_cloud = []
B_latency_split = []

B_acc_latency = []
B_acc_latency_split = []
B_acc_latency_cloud = []

'''x_new = np.linspace(0, 500 ,50)
spl = make_interp_spline(np.asarray(p_frontX_lens), np.asarray(p_frontY_lens), k=3)
energy_lens_smooth = spl(x_new)'''

for throughput in tu:	

	latency_split = (((18816*8)/(throughput*1000)) + 46.257)/1000
	latency_cloud = (((150528*8)/(throughput*1000)))/1000 
	B_latency_cloud.append(latency_cloud)
	B_latency_split.append(latency_split)
	if throughput > th_latency:
		B_latency.append(latency_cloud)
	else:
		B_latency.append(latency_split)

i = 0
while(i<len(B_latency)):

	B_acc_latency.append(sum(B_latency[:i+1]))
	B_acc_latency_split.append(sum(B_latency_split[:i+1]))
	B_acc_latency_cloud.append(sum(B_latency_cloud[:i+1]))

	i = i+1
	
	
plt.rcParams["font.family"] = "Times New Roman"
fig, ax1 = plt.subplots()

ax1.grid(linestyle='dotted', axis='both', zorder = 0)
ax1.set_facecolor('#F7F7F7')
ax1.set_xlabel('Sample no.', color='#110f0e', fontsize = 12)


ax1.set_ylabel('Throughput (Mbps)', color= '#110f0e', fontsize = 12)
x1 = ax1.plot(tu, linewidth = 1, c = '#110f0e', label = 't_{u}')

plt.hlines(y=th_latency ,xmin=0, xmax=40, linestyles = 'dashdot', color='#110f0e')
#ax1.axhspan(0, th_energy, facecolor='green', alpha=0.5)
#ax1.axhspan(th_energy, 25, facecolor='yellow', alpha=0.5)

ax2 = ax1.twinx()
ax2.set_ylabel('Latency (s)', color= '#112C8F', fontsize = 12)
ax2.tick_params(axis='y', labelcolor='#112C8F')
x2 = ax2.plot(B_acc_latency, '-', linewidth=2, color = '#1638B3', label='Dynamic')
x2 = ax2.plot(B_acc_latency_cloud, linestyle=':', linewidth=2, color = '#1638B3', label='All-Cloud')
x2 = ax2.plot(B_acc_latency_split, '-.', linewidth=2, color = '#1638B3', label='Partitioned')

ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, frameon = False, fontsize = 11)

print(B_acc_latency[-1], B_acc_latency_split[-1], B_acc_latency_cloud[-1])

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
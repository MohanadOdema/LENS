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
tu = df1['tu'].to_list()

A_energy = []
A_energy_edge = []
A_energy_split = []

B_latency = []
B_latency_cloud = []
B_latency_split = []

A_acc_energy = []
A_acc_energy_split = []
A_acc_energy_edge = []

B_acc_latency = []
B_acc_latency_split = []
B_acc_latency_cloud = []



'''x_new = np.linspace(0, 500 ,50)
spl = make_interp_spline(np.asarray(p_frontX_lens), np.asarray(p_frontY_lens), k=3)
energy_lens_smooth = spl(x_new)'''

for throughput in tu:

	energy_edge = 279.534
	energy_split = (483.39*throughput + 1288.04)*((18816*8)/(throughput*1000000)) + 178.04
	A_energy_edge.append(energy_edge)
	A_energy_split.append(energy_split)
	if throughput > th_energy:
		A_energy.append(energy_split)
	else:
		A_energy.append(energy_edge)	

	latency_split = ((18816*8)/(throughput*1000)) + 46.257
	latency_cloud = ((150528*8)/(throughput*1000)) 
	B_latency_cloud.append(latency_cloud)
	B_latency_split.append(latency_split)
	if throughput > th_latency:
		B_latency.append(latency_cloud)
	else:
		B_latency.append(latency_split)

i = 0
while(i<len(A_energy)):
	A_acc_energy.append(sum(A_energy[:i+1]))
	A_acc_energy_split.append(sum(A_energy_split[:i+1]))
	A_acc_energy_edge.append(sum(A_energy_edge[:i+1]))

	B_acc_latency.append(sum(B_latency[:i+1]))
	B_acc_latency_split.append(sum(B_latency_split[:i+1]))
	B_acc_latency_cloud.append(sum(B_latency_cloud[:i+1]))

	i = i+1
	


'''fig, ax1 = plt.subplots()
ax1.grid(linestyle='dotted', axis='both', zorder = 0)


x1 = ax1.plot(tu, label = 'Traditional')
plt.show()'''

host = host_subplot(111, axes_class=AA.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()

offset = 20
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right", axes=par2,
                                        offset=(offset, 0))

par2.axis["right"].toggle(all=True)

#host.set_xlim(0, 2)
#host.set_ylim(0, 2)

host.set_xlabel("Samples")
host.set_ylabel("Throughput (Mbps)")
par1.set_ylabel("Energy (J)")
par2.set_ylabel("Latency (s)")

p1, = host.plot(tu)
p2, = par1.plot(A_acc_energy)
p2, = par1.plot(A_acc_energy_edge)
p2, = par1.plot(A_acc_energy_split)
p3, = par2.plot(B_acc_latency)
p3, = par2.plot(B_acc_latency_cloud)
p3, = par2.plot(B_acc_latency_split)

print(A_acc_energy_edge[-1], A_acc_energy_split[-1],A_acc_energy[-1])

print(B_acc_latency_cloud[-1], B_acc_latency_split[-1], B_acc_latency[-1])




#par1.set_ylim(0, 4)
#par2.set_ylim(1, 65)

#host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
#par2.axis["right"].label.set_color(p3.get_color())

plt.draw()
plt.show()

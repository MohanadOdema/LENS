import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri
from scipy.interpolate import make_interp_spline, BSpline


def pareto_dominates(u, v, tolerance=None):
  """ Returns true if u >= v elementwise, and at least
      one of the elements is not an equality.
  """
  #print(u)
  u = np.asarray(u, dtype=np.float32)
  v = np.asarray(v, dtype=np.float32)
  if tolerance is None:
    return np.all(u <= v) and not np.all(u == v) #OD: This assures that new value and current ones are not equal (even asserted the type)
  else:
    return np.all(u <= v) and not np.linalg.norm(u - v) <= tolerance

def update_pareto_set(vals, new_val):

  num_points = len(vals)
  new_vals = []
  #print("Current optimal points and values: ")
  #print(points, vals)
  
  for i in range(num_points):
    # If new_val does not dominate vals[i], keep it
    if not pareto_dominates(new_val, vals[i]):
      new_vals.append(vals[i])
  # Check if new_vals is not dominated by any vals[i].
  # If so, then keep it.
  dominated = False
  for i in range(num_points):
    if np.all(np.asarray(vals[i], dtype=np.float32) == np.asarray(new_val, dtype=np.float32)):
      dominated = True
      break #OD: This previous if condition was added to make sure the final pareto set does not contain redundant poin>    
    if pareto_dominates(vals[i], new_val):
      dominated = True
      break
  if not dominated:
    new_vals.append(new_val)
  #print("New optimal points and values: ")
  #print(new_points, new_vals)
  return new_vals

df1 = pd.read_excel(r'thompson300_partitioned.xlsx')
df2 = pd.read_excel(r'thompson300_unpartitioned.xlsx')


#df = pd.read_excel(r'exp1epoch20capital200rand.xlsx')



error_lens = []
energy_lens = []
error_unpart = []
energy_unpart = []
energy_part = []

error_lens = df1['Error'].to_list()
energy_lens = df1['Energy'].to_list()
error_unpart = df2['Error'].to_list()
energy_unpart = df2['Energy'].to_list()
energy_part = df2['Energy2'].to_list()

#error_lens = error_lens[:200]
#energy_lens = energy_lens[:200]
#error_unpart = error_unpart[:200]
#energy_unpart = energy_unpart[:200]
#energy_part = energy_part[:200]

combined_error = error_lens+error_unpart 
combined_energy = energy_lens+energy_part

error_energy_lens = sorted([[error_lens[i], energy_lens[i]] for i in range(len(error_lens))], reverse = False)
error_energy_unpart = sorted([[error_unpart[i], energy_unpart[i]] for i in range(len(error_unpart))], reverse = False)
error_energy_part = sorted([[error_unpart[i], energy_part[i]] for i in range(len(error_unpart))], reverse = False)

combined_sorted = sorted([[combined_error[i], combined_energy[i]] for i in range(len(combined_energy))], reverse = False)



p_front_lens = [error_energy_lens[0]]
for element in error_energy_lens[1:]:
	p_front_lens = update_pareto_set(p_front_lens, element)

p_front_unpart = [error_energy_unpart[0]]
for element in error_energy_unpart[1:]:
	p_front_unpart = update_pareto_set(p_front_unpart, element)

p_front_part = [error_energy_part[0]]
for element in error_energy_part[1:]:
  p_front_part = update_pareto_set(p_front_part, element)

p_front_combined = [combined_sorted[0]]
for element in combined_sorted[1:]:
  p_front_combined = update_pareto_set(p_front_combined, element)

#print(len(p_front200))

p_frontX_lens = [pair[0] for pair in p_front_lens]
p_frontY_lens = [pair[1] for pair in p_front_lens]

p_frontX_unpart = [pair[0] for pair in p_front_unpart]
p_frontY_unpart = [pair[1] for pair in p_front_unpart]

print(p_frontY_unpart)

p_frontX_part = [pair[0] for pair in p_front_part]
p_frontY_part = [pair[1] for pair in p_front_part]

p_frontX_combined = [pair[0] for pair in p_front_combined]
p_frontY_combined = [pair[1] for pair in p_front_combined]


print("Final Pareto")

plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12)
plt.rcParams["font.family"] = "Times New Roman"

fig, ax = plt.subplots()


x_new = np.linspace(min(p_frontX_lens),max(p_frontX_lens),50)
spl = make_interp_spline(np.asarray(p_frontX_lens), np.asarray(p_frontY_lens), k=3)
energy_lens_smooth = spl(x_new)

#print(p_frontX_lens)
#print(energy_lens_smooth)
#plt.ylim(0, 60)

ax.set_facecolor('#FAFAFA')
ax.grid(linestyle='dotted', axis='both', zorder = 0)

plt.xlim(170, 410)
plt.ylabel("Error (%)", fontsize = 14)
plt.xlabel("Energy (mJ)", fontsize = 14)
plt.scatter(energy_lens[:], error_lens[:], marker = 'X', s = 10, c = '#BEC9F3', label = 'LENS samples')
plt.scatter(energy_unpart[:], error_unpart[:], marker = '^', s = 10, c = '#A7A9A7', label='Traditional samples')


#plt1 = plt.plot(x_new, energy_lens_smooth, linewidth = 2, c = 'chocolate', label='LENS Pareto')
plt1 = plt.plot(p_frontY_lens, p_frontX_lens, '', linewidth = 2.5, c = '#284BD8', label='LENS Pareto')
plt1 = plt.plot(p_frontY_lens, p_frontX_lens, '*', linewidth = 2.5, c = '#284BD8')
plt2 = plt.plot(p_frontY_unpart, p_frontX_unpart, '--', linewidth = 2.5, c = '#605351', label='Traditional Pareto')
plt2 = plt.plot(p_frontY_unpart, p_frontX_unpart, '*', linewidth = 2.5, c = '#605351')
plt3 = plt.plot(p_frontY_part, p_frontX_part, '-', linewidth = 2.5, c = '#252925', label='Traditional+Partition Pareto')
plt3 = plt.plot(p_frontY_part, p_frontX_part, '*', linewidth = 2.5, c = '#252925')
#plt4 = plt.plot(p_frontY_combined, p_frontX_combined, '-', linewidth = 1.5, c = 'green', label='Combined')
#plt1 = plt.plot(p_frontX200, p_frontY200, c = 'green', label='After 200 iterations')

#ax.annotate('Model', xy=(10.39414, 39.22790), xytext=(13, 40), fontsize = 18, arrowprops=dict(width=0.01, headwidth=5,  facecolor='black', shrink=0.03),)

#ax.text(15.6, 40, '$\mathit{a}$', fontsize=18)

print(p_frontX_unpart)

print(p_frontX_lens)


plt.legend(loc="upper center", ncol=3, fontsize='large', framealpha=1)
plt.show()

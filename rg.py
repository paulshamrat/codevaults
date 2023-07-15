#Rg
# load the trajectory and topology files
import MDAnalysis as mda
from MDAnalysis.analysis import rms
import numpy as np
import matplotlib.pyplot as plt


u = mda.Universe('/workspaces/codevaults/1AKI_solv_ions.gro', '/workspaces/codevaults/md_0_1.xtc')

# select protein atoms for analysis
protein = u.select_atoms('protein')

# calculate the radius of gyration
com = np.array([protein.center_of_mass()])
Rg_list = []
for ts in u.trajectory:
    Rg = np.sqrt(np.sum((protein.positions - com)**2)/len(protein))
    Rg_list.append(Rg)

# plot the radius of gyration
plt.plot(np.arange(len(Rg_list)), Rg_list)
plt.xlabel('Time (frames)')
plt.ylabel('Radius of gyration (Å)')


# save the plot as a PNG file
plt.savefig('rg_plot.png', dpi=300)

# show the plot
plt.show()

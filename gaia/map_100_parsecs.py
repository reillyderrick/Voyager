from __future__ import division #always returns approximations from divisions
import numpy as np
import matplotlib.pyplot as plt
import ephem #for astronomy calculations, converting coordinate systems
import pandas as pd

#set up ra coordinates to work on graph
df = pd.read_csv('gaia/100_parsecs_ra_dec.csv')
df.loc[df['ra'] > 180, 'ra'] -= 360
df['ra'] = df['ra'] * -1

#plotting
tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection = 'mollweide')

ax.hexbin(np.radians(df['ra']), np.radians(df['dec']), cmap= plt.cm.Spectral_r, gridsize = 100, mincnt = 1, bins='log')

ax.set_title("Stars within 100 Parsecs of the Sun")
ax.set_xticklabels(tick_labels)
ax.set_xlabel("RA")
ax.set_ylabel("Dec")
ax.grid(True)

plt.savefig('gaia_100_parsecs.png')
plt.show()

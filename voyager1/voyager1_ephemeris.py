from __future__ import division #always returns approximations from divisions
import numpy as np
import matplotlib.pyplot as plt
import ephem #for astronomy calculations, converting coordinate systems
import pandas as pd

df = pd.read_csv('voyager1/voyager1_ephemeris.txt', skiprows = 57, skipfooter=216-165, engine='python')

df['date'] = df['date'].apply(lambda x: x[:12])

#set up ra and ecplitic longitude arrays
df.loc[df['ra'] > 180, 'ra'] -= 360
df['ra'] = df['ra'] * -1

df.loc[df['obsEcLng'] > 180, 'obsEcLng'] -= 360
df['obsEcLng'] = df['obsEcLng'] * -1

#set up plot for equatorial coordinates
tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection = 'mollweide')
ax.scatter(np.radians(df['ra']), np.radians(df['dec']))
ax.set_xticklabels(tick_labels)
ax.set_title("Voyager 1 Path from Jan 1, 1978 to Jul 1, 2030 on Equatorial Plane")
ax.set_xlabel("RA")
ax.set_ylabel("Dec")
ax.set_facecolor('xkcd:light blue')
ax.grid(True)

plt.savefig('voyager1_equatorial_ephemeris.png')
plt.show()

#set up plot for ecliptic coordinates
fig2 = plt.figure(figsize=(20, 10))
ax2 = fig2.add_subplot(111, projection = 'mollweide')
ax2.scatter(np.radians(df['obsEcLng']), np.radians(df['obsEcLat']))
ax2.set_xticklabels(tick_labels)
ax2.set_title("Voyager 1 Path from Jan 1, 1978 to Jul 1, 2030 on Ecliptic Plane")
ax2.set_xlabel("Longitude")
ax2.set_ylabel("Latitude")
ax2.set_facecolor('xkcd:light blue')
ax2.grid(True)

plt.savefig('voyager1_ecliptic_ephemeris.png')
plt.show()
# Convert RA/DEC from hh:mm:ss format to degree
# by Guilherme Limberg

from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
import pandas as pd

#------------------------------------------------------------
#Open the data file
data = []
with open("RADEC.csv",'r') as file:
	data = file.readlines()

# combine RA+DEC to facilitate the conversion
ra_dec = [] 

counter = -1
for line in data:
	counter = counter + 1
	if counter != 0:
		split_line = line.split(',')
		ra_dec.append(split_line[0]+' '+split_line[1])

#Put the coordinates into a bin to get them easier in degrees
coordinates = SkyCoord(ra_dec,unit=(u.hourangle,u.deg))

#Convert the astropy.SkyCoord object to pandas DataFrame
coord_df = pd.DataFrame({"ra":coordinates.ra.degree, "dec": coordinates.dec.degree})

#Save file: 
coord_df.to_csv("deg_coord.csv", index=False)


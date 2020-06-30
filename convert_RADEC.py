# Convert RA/DEC from hh:mm:ss format to degree
# by Guilherme Limberg

from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np
import pandas as pd
from astropy.table import Table

#------------------------------------------------------------
#Open the data file
data = Table.read("RADEC.csv")

ra = data["RA"]
dec= data["DEC"]

#Put the coordinates into a bin to get them easier in degrees
coordinates = SkyCoord(ra=ra*u.hourangle, dec=dec*u.deg)

#Convert the astropy.SkyCoord object to pandas DataFrame
coord_df = pd.DataFrame({"ra":coordinates.ra.degree, "dec": coordinates.dec.degree})

#Save file: 
coord_df.to_csv("deg_coord.csv", index=False)


import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord

# load the data (in this case, comma separated tables, but can be done with ascii files eventually)
data = pd.read_csv("your_data.csv")


# this next step simply combines the original RA and DEC columns
# mind the names of the columns for RA and DEC
coords = data["RA"].astype(str)+" "+data["Decl"].astype(str)

# it's a nuisance that we cannot just put this directly into a SkyCoord object... so we go around
coords_deg = [] # create array that will receive the values in astropy format
for i in range(len(coords)):
	coords_deg.append(SkyCoord(coords[i], unit=(u.hourangle, u.deg)))

# now we already have things in deg.
# so we just put these values in other arrays and merge with the original table

coords_ra_deg = []
coords_dec_deg = []

for i in range(len(coords)):
	coords_ra_deg.append(coords_deg[i].ra.value)

for i in range(len(coords)):
	coords_dec_deg.append(coords_deg[i].dec.value)

# to merge an existing pandas dataframe with new columns, we can just... :
data["RAdeg"] = coords_ra_deg
data["DECdeg"] = coords_dec_deg

# and save everything (comma separated)
data.to_csv("your_data.csv")

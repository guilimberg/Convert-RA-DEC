# Convert-RA-DEC

by Guilherme Limberg

This Python3 code allows you to convert positions (RA/DEC) from hh:mm:ss (or hh mm ss, it doesn't make any difference) format to degree (deg). This should be pretty useful for afterwards calculations of kinematical/dynamical properties among other uses. 

For this, you need Astropy, Numpy and Pandas packages installed.

Important: your input data file must have RA and DEC as the first two columns. 

The script is pretty straight foward, but since I couldn't find any online tool for doing this to big lists of objects, I decided to write one of my own and make it available to everyone. 

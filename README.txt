The rgiparser and rgimapper scripts are to be run in sequence, rgi parser before mapper, processing RGI outputs based on two user defined files

manifest.txt defines the file paths, latitude and longitude, and year of data collection for each processed file

visconfig is a generic file that should contain visualization naming information and a user defined cutoff for sequence identity. The format should be as follows:

Title = Visualization of AMR Data, Cutoff = 50

In the event that this syntax is repeated, the program will use the last encountered value formatted in this manner, or barring that, it will default to a cutoff of 0.

#script processor parsing output from data collation tool
import plotly.express as px
import pandas as pd
import time
import re

# because the output of the prior script is a .csv, it is not necessary to reprocess output files every time if data needs to be added to the set - it is enough to generate two output csv files and combine them manually.
# nevertheless, the rgiparser script will retain its behavior of overwriting anything in the "collected.csv" output file every time it is run - it is left to the user to ensure data is backed up

df = pd.read_csv('collected.csv')

# accept user defined configuration from file

try:
    config = open("visconfig",'r')
except:
    # if file is absent, recreate it
    config = open("visconfig",'w')
    config.write("Title = Placeholder, Cutoff = 0")
    config.close()
    config = open("visconfig",'r')

for line in config:
    usertitle = re.search(r'(?<=Title = ).+(?=\,)',str(line))
    cutoff = re.search(r'(?<=Cutoff = ).+(?=\n)',str(line))

# process user defined cutoff from visconfig file

if cutoff != None:
    try:
        cutoff = float(cutoff[0])
    except:
        cutoff = 0

# parse entries from summarized data by cutoff, to count occurrences and generate a dataset-wide histogram
df = df[df.Best_Identities >= cutoff]
spots = df.groupby(['Lat','Lon']).size().reset_index(name='Hits')
types = df.groupby(['Drug Class']).size().reset_index(name='Drugs')

fig = px.scatter_geo(spots, lat="Lat", lon="Lon", color="Hits", title=usertitle[0]+" Cutoff = "+str(cutoff))
fig2 = px.histogram(types, x="Drug Class", y="Drugs", title=usertitle[0]+" Cutoff = "+str(cutoff)+" Overall Summary")

#generate timestamp for .html figure output, then print to file as interactive html

now = time.strftime("%H:%M:%S", time.localtime())

path = str(now)+"_visualization.html"
fig.write_html(path)
fig2.write_html("Summary_"+path)
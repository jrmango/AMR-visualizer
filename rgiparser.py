# data parsing script to convert CARD RGI outputs into a file format with the downstream final visualizer
import re

# import manifest of output file paths to be processed and matched latitude/longitude coordinates
mfst = open("manifest.txt","r")
# open an active file reader to collect processed file
compiled = open("collected.csv","w")
# clear file and add header
compiled.truncate(0)
compiled.write("Cutoff,Best_Identities,Drug Class,Lat,Lon,Year\n")

# process the file
for row in mfst:
    mansplit = re.split(r',+', row)
    activepath = mansplit[0]
    manlat = mansplit[1]
    manlon = mansplit[2]
    mandate = mansplit[3]
    active = open(activepath, "r")
		#for each processed RGI output file, prepare a string item and iterator to hold selected entries from the formatted file 
    output = ""
    iterator = 0
    for entry in active:
        #included to skip headers
        if iterator > 0:
            #split by tabs
            tabsplit = re.split(r'\t', entry)
            #following header, add Cutoff ("loose" or "strict" matching) - cutoff is mostly included for informational purposes when reviewing the .csv output
            output += (tabsplit[5]+",")
            #following header, add Best_Identities - percent cover of best match. Call str() just in case
            output += (str(tabsplit[9])+",")
            #following header, add Drug class of resistance
            output += (tabsplit[14]+",")
            #incorporate latitude and longitude coordinates from the manifest file into the compiled dataset from which maps will be made
            output += (str(manlat)+","+str(manlon)+","+str(mandate))
            #put it all together and output to file
            compiled.write(output)
        iterator += 1
    active.close()

#Once all referenced output files in the manifest are processed for high level information, the "collected.csv" output is ready to be passed to the next script which will convert it to a graphic
#These scripts are kept separate to better facilitate repeated generation of relevant figures
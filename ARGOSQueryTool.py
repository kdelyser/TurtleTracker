# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data
#
# Created by: Kendall DeLyser (kendall.delyser@duke.edu)
# Created on: Sept, 2018

# Copy and paste a line of data as the lineString variable
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

# Use the split command to parse the items in lineString
lineData = lineString.split("\t")

# Assign variables to specific items in the list
recordID = lineData[0]              # ARGOS tracking record ID
obsDateTime = lineData[2]           # Observation date and time (combined)
obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
obsLC = lineData[3]                 # Observation location class
obsLat = lineData[5]                # Observation latitude
obsLon = lineData[6]                # Observation longitude

# Print information to the user
print ("Record {0} indicates Sara was seen at {1}N and {2}W on {3}".format(recordID,obsLat,obsLon,obsDate))

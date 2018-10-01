# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data
#
# Created by: Kendall DeLyser (kendall.delyser@duke.edu)
# Created on: Sept, 2018

# Create a variable pointing to the file with no header
fileName = "SaraNoHeader.txt"

# Open the file as a read-only file object
fileObj = open(fileName, 'r')

# Extract the first line from the file
lineString = fileObj.readline()

# Loop through the lines until all lines have been read
while lineString:  #this will run as long as the variable lineString has a value (so don't need to set it equal to anything or use another conditional statement)

    # Use the split command to parse the items in lineString into a list object
    lineData = lineString.split("\t")

    # Assign variables to specfic items in the list
    recordID = lineData[0]              # ARGOS tracking record ID
    obsDateTime = lineData[2]           # Observation date and time (combined)
    obsDate = obsDateTime.split()[0]    # Observation date - first item in obsDateTime list object
    obsTime = obsDateTime.split()[1]    # Observation time - second item in obsDateTime list object
    obsLC = lineData[3]                 # Observation Location Class
    obsLat = lineData[5]                # Observation Latitude
    obsLon = lineData[6]                # Observation Longitude

    # Print information to the user
    print ("Record {0} indicates Sara was seen at {1}N and {2}W on {3}".format(recordID,obsLat,obsLon,obsDate))

    # Move to the next line (will point to a None object once it reaches the end of the file)
    lineString = fileObj.readline()

# Close the file
fileObj.close()
    
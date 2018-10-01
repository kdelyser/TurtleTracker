# ARGOSQueryTool.py
#
# Description: Parses a line of ARGOS tracking data
#
# Created by: Kendall DeLyser (kendall.delyser@duke.edu)
# Created on: Oct, 2018

try:
    # Create a variable pointing to the file with no header
    fileName = "Sara.txt"

    # Open the file as a read-only file object
    fileObj = open(fileName, 'r')

    # Read the first line from the open file object
    lineStrings = fileObj.readlines()
    print ("There are {} records in the file".format(len(lineStrings)))
        
    # Close the file object
    fileObj.close()

    # Create empty dictionaries
    dateDict = {}
    locationDict = {}

    # Use a for loop to read each line, one at a time, until the list is exhausted
    for lineString in lineStrings:  #starting at Line 18 (item 17 of the file) skips all the original header information in the Sara.txt data file

        # Or you can skip any lines starting with non-data (the # or u characters)
        if lineString[0] in ('#', 'u'):
            continue

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

        # Filter records that get added to the dictionary by Location Class
        if obsLC in ('1', '2', '3'):

            # Add values to dictionary
            dateDict[recordID] = obsDate   
            locationDict[recordID] = (obsLat, obsLon) #this assigns coordinates as a tuple

    #Ask the user for a date, specifying the format
    userDate = input("Enter a date (M/D/YYYY)")

    # Create an empty key list to store data that matches the userDate
    keyList = []

    # Loop through all key:value pairs in the dateDict
    for k,v in dateDict.items():

        # See if the date (dict value) matches the user's date
        if v == userDate:
            keyList.append(k)  # add the key to the list created above

    # Check that at least one key was returned; tell the user if not
    if len(keyList) == 0:
        print("No observations recorded for {}.".format(userDate))
    else:
        # Loop through each key in the list and report the associated date location
        for k in keyList:
            theDate = dateDict[k]
            theLocation = locationDict[k]
            theLat = theLocation[0]
            theLon = theLocation[1]
            print("Record {0}: Sara was seen at {1}N, {2}W on {3}".format(k,theLat,theLon,theDate))

except Exception as e:
    print(e)

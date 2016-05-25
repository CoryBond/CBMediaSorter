import os
import re
import os.path
import datetime
import shutil

#Configuration
pictureDirectory = r'T:\Users\Cory\Pictures\example'
destinationDirectory = r'T:\Users\Cory\Pictures\Corys_Pictures'
parsingRegexPattern = '.*(?=_)'
datePattern = '%Y%m%d'
destinationRegexPattern = '%Y_%m_%d'

def pigeonHolePicture(fileName, date_match):
    # use regex to parse fileName info
    destination_name = parseDate(fileName, date_match)
    destination_path = destinationDirectory + '\\' + destination_name
    moveFile(destination_path)

def pigeonHoleVideo(fileName, date_match):
    # use regex to parse fileName info
    destination_name = parseDate(fileName, date_match)
    destination_path = destinationDirectory + '\\' + destination_name + '_video_'
    moveFile(destination_path)

def parseDate(fileName, date_match):
    date_object = datetime.datetime.strptime(date_match.group(0), datePattern)
    return date_object.strftime(destinationRegexPattern)

def moveFile(destinationPath):
    if not os.path.exists(destinationPath):
        os.makedirs(destinationPath)
    # move file to new directory if i
    shutil.move(pictureDirectory + '\\' + fileName, destinationPath + '\\' + fileName)

# Init/Entry_Point

if os.path.exists(pictureDirectory):
    # first compile regex
    parsingRegexMatcher = re.compile(parsingRegexPattern)
    for root, dirs, filenames in os.walk(pictureDirectory):
        for fileName in filenames:
            date_match = parsingRegexMatcher.search(fileName)
            if (date_match is not None):
                if(fileName.endswith('.jpg')):
                    pigeonHolePicture(fileName, date_match)
                elif (fileName.endswith('.mp4')):
                    pigeonHoleVideo(fileName, date_match)














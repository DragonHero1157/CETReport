"""
Docstring for Modules.ExtractData
    Contains the functions that perform the initial extraction of data from the input file

    Contents:
        Functions:
            get_ReportDate([str]):
            remove_Comments(file,str,str):
            get_DataRecs(input file):
"""
from datetime import datetime
import re
import csv
from Modules import GlobalVars

def get_ReportDate(dateLineList):
    """
    Docstring for get_ReportDate
        Extracts and converts strings from the input file that represent the date the report was generated.
    
        Args:
            [str]: list of strings found in the input file to contain the report date
        Returns:
            None; modifies the global variable, reportAsOfDate
    """
    daysofweekList = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
    found = False
    dateString: str = ""
    transformedDate: str = ""
#        print(f'dateLineList = {dateLineList}')
    # Iterate through word list and skip to the beginning of the date string
    for word in dateLineList:
        transformedWord: str = word.strip(', \"\n\t')
#            print(f'transformedWord = {transformedWord}')
        if transformedWord in daysofweekList:
            found = True
        if found:
            dateString += transformedWord + " "
#        print(f'dateString = {dateString}.')
    transformedDate = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', dateString.strip())
#        print(f'transformedDate = {transformedDate}.')
    dateFormat = "%A %B %d %Y %I:%M:%S %p"
    convertedDate = datetime.strptime(transformedDate, dateFormat)
#        print(f'convertedDate = {convertedDate}')
    GlobalVars.reportAsOfDate = f'{convertedDate}'

def removeComments(file, delimiterChar=',', commentChar='\"' ):
    """
    Docstring for removeComments
        Generator function used with reading a file
         * scans the file for comment delimited records & searches for the report generation date strings - must be performed first as
         * scans the file for non-data records and ignores/skips them
         * fills a buffer of valid data records for further processing

         Args:
            file: object obtained from the open()
            str: string for use in the scan to help identify a valid data record
            str: string for use in the scan to identify a comment line that potentially contains the report generation strings

        Returns:
            str: data record string
    """
    for inLine in file:
        if inLine.startswith(commentChar):
            get_ReportDate(inLine.split())
            continue
        elif delimiterChar not in inLine:
            continue
        yield inLine

def get_DataRecs(fName, dumpData=False):
    """
    Docstring for get_DataRecs
        With the help of a generator function while file reading, skips non-data records wherever they appear in the input file. Non-data records are defined as file records that do not start with the double-quote character and/or do not contain any comma characters.

        Args:
            str: name of file to open for reading
            bool: flag to indicate whether the file contents will be dumped or processed - determines what csv file reader method to use

        Returns:
            [str] | {str}: depending on the dumpData flag, either a list of strings or a dictionary of strings that represent all the filtered data records.
    """
    with open(fName, 'r') as file:
        content_iterator = removeComments(file)
        dataRecords = list(content_iterator)
        if dumpData:
           newRawBuffer = csv.reader(dataRecords)
        else:
           newRawBuffer = csv.DictReader(dataRecords)

    return newRawBuffer
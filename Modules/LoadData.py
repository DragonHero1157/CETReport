"""
Docstring for Modules.LoadData
    Contains the functions that perform the 'load' of the transformed data
    Typically, the 'load' function of an ETL process is into a database. However in this case the 'load' is to a new CSV file.
"""
import csv
from Modules import GlobalVars

def load_Data(transformedBuffer: dict, myArgv):
    """
    Docstring for load_Data
        Writes the transformed data to a comma delimited text file after writing a header record
        Uses the Python library csv class to easily format the output
    
    Args:
        dict: dictionary of associate progress report records

    Returns:
        None
    """
    # Create new CSV file from transformed data
    # Format header record by defining field names
    # print(f'reportAsOfDate = {reportAsOfDate}')
    headerFields = ['First Name',
                                'Last Name',
                                'Manager',
                                'Total Completed',
                                'Percent Completed',
                                GlobalVars.reportAsOfDate
                                ]
    # Write the header and data records out to a new/replaced CSV file using the csv dictionary writer method
    with open(myArgv.outFName, 'w') as file:
        outFile = csv.DictWriter(file, fieldnames=headerFields)
        outFile.writeheader()
        outFile.writerows(transformedBuffer.values())
"""
Docstring for Modules.LoadData
"""
import csv
from Modules import GlobalVars

def load_Data(transformedBuffer: dict, myArgv):
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
"""
Docstring for Modules.ConsolidateData
    Contains the functions that scan the input file and merges individual records for the same key value into a single record represented by a dictionary
    
    Functions:
        consolidate_Data(): 
"""
def consolidate_Data(rawRecord, consolidatedBuffer:dict):
    """
        consolidate_Data handles a raw CSV file that contains multiple records for an associate and consolidates them into a single dictionary entry
    """
    # Extract associate key value from raw CSV record
    associateKey = rawRecord['User Name']
    # Extract module+status data from raw CSV record
    newModule:tuple = (rawRecord['Module Title'],rawRecord['Module Status'])
    
    # if new associate encountered, create full dictionary item
    if associateKey not in consolidatedBuffer:
        # Assemble associate entry and seed with empty module list
        associateRecord = {}
        associateRecord.update({'First Name':rawRecord['First Name'],
                                'Last Name':rawRecord['Last Name'],
                                'Manager':rawRecord['Supervisor Name'],
                                'modules':[]
                                })
        # Append associate record to transformation buffer
        consolidatedBuffer[associateKey] = associateRecord
    # Update modules list with new module+status regardless of new or existing associate
    moduleList: list = consolidatedBuffer[associateKey]['modules']
    moduleList.append(newModule)
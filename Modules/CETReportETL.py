"""
    TransformCSV performs several transformations on the raw data that was exported from the Compliance Training portal reports
    
    Transformations:
        1. Remove any leading and trailing lines that are report comments and not data
        2. Consolidate records for the same associate based 'User Name' and transform modules+status into a list
        3. Calculate the count of modules and the percent complete for each associate
"""
import sys
from Objects import CommandLine
from Modules import GlobalVars, ExtractData, ConsolidateData, TransformData, LoadData

# -------------------------------------------------------------------------------------       
# ------------------------------------- Main() ----------------------------------------
# -------------------------------------------------------------------------------------

# Get command line arguments
myArgv = CommandLine.Args()

# Parse file for only the data records
cleanRawBuffer = ExtractData.get_DataRecs(myArgv.inFName, myArgv.doDump)

# If user specified dictionary approach 
if myArgv.doDump:
    # Dump file buffer to STDOUT & exit
    print(f"*** Dumping raw file buffer to STDOUT: {myArgv.inFName} ***\n\n")
    for currItem in cleanRawBuffer:
        print(currItem)
    sys.exit(0)

# Transform data consolidation of raw CSV file records and update 1st transformation buffer
consolidatedBuffer = {}
for rawItem in cleanRawBuffer:
    ConsolidateData.consolidate_Data(rawItem, consolidatedBuffer)
# debug: Dump consolidatedBuffer
# for entryKey, entryValue in consolidatedBuffer.items():
#     print(f"KEY: {entryKey}\nVALUE: {entryValue}")

# Transform consolidated data to convert module status into total count of module completion and % module completion for each associate record
transformedBuffer = TransformData.transform_Data(consolidatedBuffer)

# Load transformed data to new CSV file
LoadData.load_Data(transformedBuffer, myArgv)
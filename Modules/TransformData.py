import copy

def transform_Data(consolidatedBuffer):
# Perform module completion analysis on consolidated data and create new transformation buffer
# Create a deep copy of the consolidated data buffer
    transformedBuffer = copy.deepcopy(consolidatedBuffer)

    # Iterate on each entry and calculate the module completion statistics
    for entryKey, entryValue in transformedBuffer.items():
        # Get the module+status list
        modulesList = entryValue['modules']
        # Get the list size for the percentage calculation
        listSize = len(modulesList)
        # Initialize the completion count
        modulesComplete : int = 0
        for moduleEntry, moduleStatus in modulesList:
            # Iterate through the module+status list to total the number of completions
            match moduleStatus:
                case "Complete":
                    modulesComplete += 1
                case _:
                    pass
    #                print(f"Unknown status encountered: {moduleStatus}")
        # Update associate record with the total and percent complete
        transformedBuffer[entryKey]['Total Completed'] = modulesComplete
        transformedBuffer[entryKey]['Percent Completed'] = float(modulesComplete / listSize)
        # Remove the module+status list
        del transformedBuffer[entryKey]['modules']

        # debug: Dump transformed associate record to STDOUT
    #    print(f"Associate: {entryKey}\nData: {entryValue}")
    return transformedBuffer
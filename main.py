###################################
#### Main file ####################
##### By cmoraga-dev ##############


##### 0
# Dictionary iteration functions
# enumerate function -> allows to iterate an object using a numeric index and the original index
# Useful to get the previous and next node inside the loop
# Example:

exampleDict = {12:{'some': 'dictionary'}}

for index, key in enumerate(exampleDict):
            # Like arrays, start position would be 0. To get the last index, we can use -1.
            startPosition   = index == 0
            endPosition     = index == len(exampleDict) -1

            # This is a logic to get the previous and next node, preventing out of bounds based on position
            # However, there is some logic duplicated here.
            if startPosition:
                nextKey                 = list(exampleDict.keys())[index+1]
                duplicatedToTheRight    = exampleDict[key]['type'] == exampleDict[nextKey]['type']
                duplicatedToTheLeft     = False
            elif endPosition: 
                prevKey                 = list(exampleDict.keys())[index-1]
                duplicatedToTheLeft     = exampleDict[key]['type'] == exampleDict[prevKey]['type']
                duplicatedToTheRight    = False
            else:
                prevKey                 = list(exampleDict.keys())[index-1]
                nextKey                 = list(exampleDict.keys())[index+1]
                duplicatedToTheLeft     = exampleDict[key]['type'] == exampleDict[prevKey]['type']
                duplicatedToTheRight    = exampleDict[key]['type'] == exampleDict[nextKey]['type']

# End loop

# In a nested dictionary, get the key with the highest/lowest inner value. 
# This is like vlookup in excel (?)
max(exampleDict, key=lambda v: exampleDict[v]['some_inner_key'])

# I needed something like this, but I couldn't find it on Python.
# So I found this, added some little adjustments, and it does the trick :D
def isNumber (n):
    '''
    Custom function. Works with almost every object - as far as I know.
    '''
    try:
        float(n)
        return True
    except (ValueError, TypeError):
        return False


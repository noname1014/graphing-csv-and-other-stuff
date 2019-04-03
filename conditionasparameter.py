import rdcsv
# Arguments in format
# [attribute, condition], [attribute1, condition1]
# Data[attribute] satisfies condition and Data[attribute1] satisfies
def condition(left, op, right):
    exec("global check; check=(lambda a, b: " + str(op) + ")")
    return check(left, right)
def or_cond(*args):
    for i in range(0, len(args), 1):
        if args[i]:
            return True # Return a boolean value of True if any of the conditions are met (OR)
    return False # Return a boolean value of False if none of the conditions are met
def and_cond(*args):
    for i in range(0, len(args), 1):
        if not args[i]:
            return False # Return a boolean value of False if all of the conditions are not met (AND)
    return True # Return a voolean value of False if any of the conditions are not met
def filter(objects, *conditions): # Function for filtering objects based on their attributes.
    satisfy = [] # Array of objects that satisfy the conditions passed to the function.
    for obj in objects:
        satisfied = True
        for con in conditions: # Loop every condition passed to the function.
            attr = con[0] # Attribute to filter
            cond = con[1] # Condition to filter e.g. "a==b"
            val = con[2]  # The value to filter by.
            # Example:
            # filter(Data, [index, "a==b", 2])
            # Will filter all objects in Data and return all objects with attribute "index" equal to 2
            if not condition(obj[attr], cond, val): # If any of the conditions are not met, return a value of False
                satisfied = False
        if satisfied:
            satisfy.append(obj) # Add the object to the array containing all objects passed to function that satisfy the conditions
    return satisfy
avocado = rdcsv.read_csv("avocado.csv")
avocado = filter(avocado, ["index", "a==b", "52"]) # Example filtering. This will filter objects to only objects with an index of 27.
print(avocado) # Show results of reading the file.

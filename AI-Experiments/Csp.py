# Define the variables and domains
VARIABLES = ['csc', 'maths', 'phy', 'che', 'tam', 'eng', 'bio']  # subjects
DOMAIN = ['Monday', 'Tuesday', 'Wednesday']  # possible days

# Define the constraint pairs where the subjects cannot be on the same day
CONSTRAINT = [
    ('csc', 'maths'), ('csc', 'phy'), ('maths', 'phy'),
    ('maths', 'che'), ('maths', 'tam'), ('phy', 'tam'),
    ('phy', 'eng'), ('che', 'eng'), ('tam', 'eng'),
    ('tam', 'bio'), ('eng', 'bio')
] 

# Define a function to check if the current assignment is valid
def is_consistent(assignment, var, value):
    """
    Check if assigning 'value' to 'var' is consistent with the current assignment
    and the constraint pairs defined in CONSTRAINT.
    """
    # Ensure no two subjects in a constraint pair are assigned the same day
    for (v1, v2) in CONSTRAINT:
        if var == v1 and v2 in assignment and assignment[v2] == value:
            return False
        if var == v2 and v1 in assignment and assignment[v1] == value:
            return False
    
    return True
    
    

# Backtracking search to assign values to variables
def backtrack(assignment):
    """ Use backtracking to find a complete and valid assignment """
    
    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):
        # Ensure each domain value is assigned to at least one variable
        assigned_days = set(assignment.values())
        if len(assigned_days) == len(DOMAIN):  # Check if all days are used
            return assignment
        else:
            return None
    
    # Select an unassigned variable
    for var in VARIABLES:
        if var not in assignment:
            break
    
    # Try assigning each value in the domain to the selected variable
    for value in DOMAIN:
        if is_consistent(assignment, var, value):
            assignment[var] = value  # Assign the value
            
            # Recursively try to complete the assignment
            result = backtrack(assignment)
            if result:
                return result
            
            # If the result is not valid, backtrack (remove the assignment)
            del assignment[var]
    
    # If no valid assignment is found, return None
    return None

# Run the backtracking search
assignment = {}
solution = backtrack(assignment)

# Print the result
if solution:
    print("Assignment found:", solution)
else:
    print("No valid assignment found.")


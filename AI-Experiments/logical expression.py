import itertools

def evaluate_expression(expression, assignment):
    # Evaluate the logical expression with the current assignment
    return eval(expression, {}, assignment)

def satisfy(user_expression):
    variables = ['A', 'B', 'C']
    
    # Generate all possible combinations of truth values (True, False)
    for values in itertools.product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        
        # Check the user-defined proposition with the current assignment
        if evaluate_expression(user_expression, assignment):
            return True, assignment
            
    return False, None

def run():
    # Get the logical expression from the user
    user_expression = input("Enter a logical expression using A, B, C (e.g., '(A and not B) or C'): ")
    
    satisfiable, assignment = satisfy(user_expression)
    if satisfiable:
        print(f'satisfiable: true')
        print(f'assignment: {assignment}')
    else:
        print('satisfiable: false')

if __name__ == "__main__":
    run()

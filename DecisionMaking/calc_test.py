def per(op):
    """
    This function returns the priority of operators.
    Higher number = higher priority = do this first
    """
    match op:
        case '+':
            return 1  # Lower priority
        case '-':
            return 1  # Same as +
        case '%':
            return 2  # Higher priority - do before + or -
        case '/':
            return 2  # Higher priority
        case '*':
            return 2  # Higher priority
        case '^':
            return 3  # Highest priority

# Non-interactive test input
equation = "2 + 3 * 4"

# Break equation into tokens (removes spaces)
token = equation.split()

fin = int(token[0])  # fin stores our final result, start with first number

i = 1  # Start loop from index 1 (first operator is at index 1)

storeop = ''  # Will store a high-priority operator to do later
storevar = 0  # Will store the number that goes with storeop

# loop while there's at least an operator and a following number
while i < len(token) - 1:
    op = token[i]        # Current operator (+ or - or * etc)
    next_num = int(token[i+1])  # Next number after operator
    
    # Check if current operator has higher priority than next operator
    # If YES, we need to do current operation first
    if i + 2 < len(token):  # Check if there IS a next operator
        next_op = token[i+2]
        
        # If current operator has LOWER priority than next operator
        if per(op) < per(next_op):
            # Store this operation for later and jump to next operation
            storeop = op
            storevar = fin
            fin = next_num
            i += 2  # Move to next operator
            continue
    
    # Do the current operation
    if op == '+':
        fin = fin + next_num
    elif op == '-':
        fin = fin - next_num
    elif op == '/':
        fin = fin / next_num
    elif op == '%':
        fin = fin % next_num
    elif op == '*':
        fin = fin * next_num
    
    i += 1  # Move to next operator (this is Python syntax, not i++)

# Apply the stored operation at the end
if storeop != '':  # If we stored an operation
    if storeop == '+':
        fin = storevar + fin
    elif storeop == '-':
        fin = storevar - fin
    elif storeop == '/':
        fin = storevar / fin
    elif storeop == '%':
        fin = storevar % fin
    elif storeop == '*':
        fin = storevar * fin

print(f"{equation} = {fin}")

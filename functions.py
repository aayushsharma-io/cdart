# functions.py

def import_module(module_name):
    # Placeholder for importing modules
    return f"Imported module '{module_name}' successfully"

def declare_variable(variables, var_name, var_value):
    # Remove surrounding quotes for string literals
    if var_value.startswith('"') and var_value.endswith('"'):
        var_value = var_value[1:-1]
    else:
        try:
            var_value = int(var_value)
        except ValueError:
            pass  # Keep it as a string if it's not an integer or properly quoted string
    variables[var_name] = var_value
    return f"Variable '{var_name}' assigned value '{var_value}'"

def execute_state(expression, variables):
    if '+' in expression:
        parts = expression.split('+')
        left = parts[0].strip()
        right = parts[1].strip()
        if left.startswith('"') and left.endswith('"'):
            left = left.strip('"')
        else:
            left = variables.get(left, f"Error: '{left}' is not defined")

        if right.startswith('"') and right.endswith('"'):
            right = right.strip('"')
        else:
            right = variables.get(right, f"Error: '{right}' is not defined")

        if isinstance(left, str) and isinstance(right, str):
            return left + right
        elif isinstance(left, int) and isinstance(right, int):
            return left + right
        else:
            return f"Error: Cannot add {type(left)} and {type(right)}"
    elif expression.startswith('"') and expression.endswith('"'):
        # Handle string literals
        return expression.strip('"')
    else:
        # Handle variables
        return variables.get(expression, f"Error: '{expression}' is not defined")

def execute_state_int(expression, variables):
    if '+' in expression:
        parts = expression.split('+')
        left = parts[0].strip()
        right = parts[1].strip()
        if left.startswith('"') and left.endswith('"'):
            left = int(left.strip('"'))
        else:
            left = int(variables.get(left, f"Error: '{left}' is not defined"))

        if right.startswith('"') and right.endswith('"'):
            right = int(right.strip('"'))
        else:
            right = int(variables.get(right, f"Error: '{right}' is not defined"))

        if isinstance(left, int) and isinstance(right, int):
            return left + right
        else:
            return f"Error: Cannot add {type(left)} and {type(right)}"
    else:
        return f"Error: Invalid expression '{expression}'"

# You can define other necessary functions here as needed
def create_array(*args):
    return list(args)

def iterate_array(arr):
    return arr

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

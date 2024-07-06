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

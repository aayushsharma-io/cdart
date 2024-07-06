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

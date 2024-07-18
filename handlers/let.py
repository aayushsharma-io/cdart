def handle_let_declaration(variables, var_name, var_value):
    if var_value.startswith('"') and var_value.endswith('"'):
        var_value = var_value[1:-1]  # Remove the surrounding quotes for string values
    variables[var_name] = var_value
    return f"Variable '{var_name}' assigned value '{var_value}'"

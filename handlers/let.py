from functions.declare_variable import declare_variable

def handle_let_declaration(line, variables):
    parts = line.split('=')
    var_name = parts[0].split(' ')[1].strip()
    var_value = parts[1].strip().rstrip(';')  # Remove semicolon from variable value
    return declare_variable(variables, var_name, var_value)

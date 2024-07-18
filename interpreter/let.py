from handlers import handle_let_declaration

def interpret_let(line, variables):
    parts = line.split('=')
    var_name = parts[0].split(' ')[1].strip()
    var_value = parts[1].strip().rstrip(';')  # Remove semicolon from variable value
    return handle_let_declaration(variables, var_name, var_value)

from handlers import handle_state_int

def interpret_state_int(line, variables):
    expression = line.split('(')[1].split(')')[0].strip()
    return handle_state_int(expression, variables)

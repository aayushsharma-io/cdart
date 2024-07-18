from handlers.state import handle_state_int

def interpret_state_int(line, variables):
    expression = line.split('(', 1)[1].rsplit(')', 1)[0].strip()
    return handle_state_int(expression, variables)

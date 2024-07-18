from handlers.state import handle_state

def interpret_state(line, variables):
    expression = line.split('(', 1)[1].rsplit(')', 1)[0].strip()
    return handle_state(expression, variables)

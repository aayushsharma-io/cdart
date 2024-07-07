from handlers import handle_state

def interpret_state(line, variables):
    expression = line.split('(')[1].split(')')[0].strip()
    return handle_state(expression, variables)

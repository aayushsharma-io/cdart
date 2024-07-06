from functions.execute_state import execute_state
from functions.execute_state_int import execute_state_int

def handle_state(expression, variables):
    value = execute_state(expression, variables)
    return f"Output: {value}"

def handle_state_int(expression, variables):
    value = execute_state_int(expression, variables)
    return f"Output: {value}"

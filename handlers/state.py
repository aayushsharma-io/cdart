def handle_state(expression, variables):
    try:
        # Replace variable names in the expression with their values
        for var in variables:
            expression = expression.replace(var, str(variables[var]))

        # Evaluate the expression
        result = eval(expression)
        return f"Output: {result}"

    except Exception as e:
        return f"Error: Unable to evaluate expression '{expression}' - {str(e)}"

def handle_state_int(expression, variables):
    try:
        # Replace variable names in the expression with their values
        for var in variables:
            expression = expression.replace(var, str(variables[var]))

        # Evaluate the expression as integer
        result = eval(expression)
        return f"Output: {int(result)}"

    except Exception as e:
        return f"Error: Unable to evaluate expression '{expression}' - {str(e)}"

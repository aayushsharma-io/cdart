from handlers import handle_let_declaration

def interpret_let(line, variables):
    return handle_let_declaration(line, variables)

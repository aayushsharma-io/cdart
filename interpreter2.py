# interpreter.py

import tkinter as tk
from functions import import_module, declare_variable
from multiprocessing import Process

class CDARTInterpreterApp:
    def __init__(self, master):
        self.master = master
        master.title("CDART Interpreter")
        self.variables = {}  # Initialize variables dictionary

        self.input_text = tk.Text(master, height=720, width=720)
        self.input_text.pack()

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_code)
        self.execute_button.pack()

        self.output_text = tk.Text(master, height=5, width=50)
        self.output_text.pack()

    def execute_code(self):
        code = self.input_text.get("1.0", tk.END)
        result = self.interpret(code)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

    def interpret(self, code):
        lines = code.split('\n')
        output = ""
        for line in lines:
            if line.strip() == "":
                continue
            if line.startswith('import'):
                module = line.split(' ')[1].strip().rstrip(';')  # Remove semicolon from module name
                output += import_module(module) + '\n'
            elif line.startswith('let'):
                parts = line.split('=')
                var_name = parts[0].split(' ')[1].strip()
                var_value = parts[1].strip()
                output += declare_variable(self.variables, var_name, var_value) + '\n'
            elif line.startswith('state'):
                expression = line.split('(')[1].split(')')[0].strip()
                value = self.evaluate_expression(expression)
                if value is not None:
                    output += f"Output: {value}\n"
                else:
                    output += f"Error: Unable to evaluate expression '{expression}'\n"
            elif line.startswith('if'):
                condition = line.split('if ')[1].strip()
                if self.evaluate_condition(condition):
                    output += "Output: If condition is true\n"
                else:
                    output += "Output: If condition is false\n"
            elif line.startswith('else'):
                output += "Output: Else condition\n"
            elif line.startswith('for'):
                parts = line.split(' ')
                if len(parts) != 4:
                    output += "Error: Invalid for loop syntax\n"
                    continue
                var_name = parts[1]
                in_index = parts.index('in')
                iterable = ' '.join(parts[in_index + 1:])
                output += self.execute_for_loop(var_name, iterable)
            else:
                output += "Error: Invalid statement\n"
        return output

    def evaluate_expression(self, expression):
        if expression.isdigit():
            return int(expression)
        elif expression.startswith('"') and expression.endswith('"'):
            return expression[1:-1]
        elif expression in self.variables:
            return self.variables[expression][1:-1] if self.variables[expression].startswith('"') and self.variables[expression].endswith('"') else self.variables[expression]
        elif '+' in expression:
            parts = expression.split('+')
            evaluated_parts = []
            for part in parts:
                part = part.strip()
                if part in self.variables:
                    evaluated_parts.append(self.variables[part])
                else:
                    return None
            return ''.join(evaluated_parts)
        return None

    def evaluate_condition(self, condition):
        # Placeholder for evaluating conditions
        return True  # Change this implementation as per your requirements

    def execute_for_loop(self, var_name, iterable):
        # Placeholder for executing for loops
        return "Output: For loop executed\n"

def run_interpreter():
    root = tk.Tk()
    app = CDARTInterpreterApp(root)
    root.mainloop()

if __name__ == '__main__':
    Process(target=run_interpreter).start()

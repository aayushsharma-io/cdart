# interpreter.py

import tkinter as tk
from functions import import_module, declare_variable, execute_state
from multiprocessing import Process

class CDARTInterpreterApp:
    def __init__(self, master):
        self.master = master
        master.title("CDART Interpreter")
        master.configure(bg='lightgrey')  # Set a background color for the window
        master.resizable(True, True)  # Make the window resizable
        self.variables = {}  # Initialize variables dictionary

        self.input_text = tk.Text(master, height=30, width=100, bg='black', fg='white')  # Set the background and foreground color
        self.input_text.pack(fill=tk.BOTH, expand=True)  # Allow the text area to expand with the window

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_code)
        self.execute_button.pack()

        self.output_text = tk.Text(master, height=5, width=100)
        self.output_text.pack(fill=tk.BOTH, expand=True)  # Allow the text area to expand with the window

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
                var_value = parts[1].strip().rstrip(';')  # Remove semicolon from variable value
                output += declare_variable(self.variables, var_name, var_value) + '\n'
            elif line.startswith('state'):
                expression = line.split('(')[1].split(')')[0].strip()
                value = execute_state(expression, self.variables)
                output += f"Output: {value}\n"
            else:
                output += f"Error: Invalid statement '{line}'\n"
        return output

def run_interpreter():
    root = tk.Tk()
    app = CDARTInterpreterApp(root)
    root.mainloop()

if __name__ == '__main__':
    Process(target=run_interpreter).start()

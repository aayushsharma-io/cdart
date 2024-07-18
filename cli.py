import sys
import tkinter as tk
from cdart_interpreter import CDARTInterpreterApp

def run_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    root = tk.Tk()
    app = CDARTInterpreterApp(root)
    app.input_text.insert(tk.END, code)
    app.execute_code()
    root.mainloop()

def main():
    if len(sys.argv) != 3:
        print("Usage: cdart run <filename>")
        return

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "run":
        run_file(filename)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()

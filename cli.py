import sys
import os
from cdart_interpreter import CDARTInterpreterApp

def run_file(filename):
    if not os.path.isfile(filename):
        print(f"Error: File '{filename}' does not exist.")
        return

    with open(filename, 'r') as file:
        code = file.read()

    # Create a fake Tkinter root and CDART interpreter app
    root = tk.Tk()
    app = CDARTInterpreterApp(root)
    
    # Execute the code using the app's interpret function
    result = app.interpret(code)
    print(result)

def main():
    if len(sys.argv) < 3 or sys.argv[1] != 'run':
        print("Usage: cdart run <filename.cdart>")
        return

    filename = sys.argv[2]
    run_file(filename)

if __name__ == '__main__':
    main()

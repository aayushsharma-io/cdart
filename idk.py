import tkinter as tk
from tkinter import scrolledtext
import subprocess
import re

class Pide:
    def __init__(self, root):
        self.root = root
        self.root.title("pide - Advanced Minimalistic IDE")
        
        # Language selection
        self.language_var = tk.StringVar(value="python")
        self.language_menu = tk.OptionMenu(self.root, self.language_var, "python", "javascript", "java", "c")
        self.language_menu.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Text editor
        self.text_editor = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=25)
        self.text_editor.pack(expand=1, fill=tk.BOTH)
        self.text_editor.bind("<KeyRelease>", self.auto_complete)
        self.text_editor.bind("<Control-slash>", self.comment_line)  # Use "slash" instead of "/"
        
        # Button to run the code
        self.run_button = tk.Button(self.root, text="Run", command=self.run_code)
        self.run_button.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Output window
        self.output_window = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=10)
        self.output_window.pack(expand=1, fill=tk.BOTH)
        self.output_window.config(state=tk.DISABLED)  # Make it read-only
    
    def auto_complete(self, event):
        char = event.char
        if char in "({\"'":
            cursor_pos = self.text_editor.index(tk.INSERT)
            if char == "(":
                self.text_editor.insert(cursor_pos, ")")
            elif char == "{":
                self.text_editor.insert(cursor_pos, "}")
            elif char == "\"":
                self.text_editor.insert(cursor_pos, "\"")
            elif char == "'":
                self.text_editor.insert(cursor_pos, "'")
            self.text_editor.mark_set(tk.INSERT, cursor_pos)
    
    def comment_line(self, event):
        language = self.language_var.get()
        line_number = self.text_editor.index(tk.INSERT).split('.')[0]
        line_start = f"{line_number}.0"
        line_end = f"{line_number}.end"
        line_text = self.text_editor.get(line_start, line_end)
        
        if language == "python":
            comment_char = "#"
        elif language in ["javascript", "java", "c"]:
            comment_char = "//"
        
        if not line_text.strip().startswith(comment_char):
            self.text_editor.insert(line_start, comment_char + " ")
    
    def run_code(self):
        language = self.language_var.get()
        code = self.text_editor.get("1.0", tk.END)
        
        if language == "python":
            command = ["python", "-c", code]
        elif language == "javascript":
            command = ["node", "-e", code]
        elif language == "java":
            with open("Temp.java", "w") as file:
                file.write(code)
            command = ["javac", "Temp.java"]
            subprocess.run(command, capture_output=True, text=True)
            command = ["java", "Temp"]
        elif language == "c":
            with open("Temp.c", "w") as file:
                file.write(code)
            command = ["gcc", "Temp.c", "-o", "Temp"]
            subprocess.run(command, capture_output=True, text=True)
            command = ["./Temp"]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = e.stderr
        
        self.output_window.config(state=tk.NORMAL)
        self.output_window.delete("1.0", tk.END)
        self.output_window.insert(tk.END, output)
        self.output_window.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Pide(root)
    root.mainloop()
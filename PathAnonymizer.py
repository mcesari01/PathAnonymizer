import tkinter as tk
from tkinter import ttk
import re
import getpass
import pyperclip


class PathConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathname Anonymizer")
        self.root.geometry("600x200")

        self.username = getpass.getuser()

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Input Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_path = ttk.Entry(self.frame, width=60)
        self.input_path.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(self.frame, text="Anonymized Text:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = ttk.Entry(self.frame, width=60)
        self.output_path.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Button(self.frame, text="Anonymize", command=self.convert_path).grid(row=4, column=0, pady=10)
        ttk.Button(self.frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=4, column=1, pady=10)

    def replace_username_in_path(self, text):
        pattern = re.compile(r'\b' + re.escape(self.username) + r'\b', re.IGNORECASE)
        return pattern.sub("yourname", text)

    def convert_path(self):
        input_text = self.input_path.get()
        if input_text:
            converted_text = self.replace_username_in_path(input_text)
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, converted_text)
        else:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, "Please enter text")

    def copy_to_clipboard(self):
        output_text = self.output_path.get()
        if output_text and output_text != "Please enter text":
            pyperclip.copy(output_text)


def main():
    root = tk.Tk()
    app = PathConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
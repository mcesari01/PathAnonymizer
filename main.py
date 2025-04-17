import tkinter as tk
from tkinter import ttk
import re
import getpass
import pyperclip
import os


class PathConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Path Username Converter")
        self.root.geometry("600x200")

        # Get current username
        self.username = getpass.getuser()

        # Create and pack main frame
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input path label and textbox
        ttk.Label(self.frame, text="Input Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_path = ttk.Entry(self.frame, width=60)
        self.input_path.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Output path label and textbox
        ttk.Label(self.frame, text="Generic Path:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = ttk.Entry(self.frame, width=60)
        self.output_path.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Buttons
        ttk.Button(self.frame, text="Convert", command=self.convert_path).grid(row=4, column=0, pady=10)
        ttk.Button(self.frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=4, column=1, pady=10)

    def replace_username_in_path(self, path):
        pattern = re.compile(re.escape(self.username), re.IGNORECASE)
        return pattern.sub("<yourname>", path)

    def convert_path(self):
        input_text = self.input_path.get()
        if input_text and os.path.exists(input_text):
            generic_path = self.replace_username_in_path(input_text)
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, generic_path)
        else:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, "Invalid path")

    def copy_to_clipboard(self):
        output_text = self.output_path.get()
        if output_text and output_text != "Invalid path":
            pyperclip.copy(output_text)


def main():
    root = tk.Tk()
    app = PathConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
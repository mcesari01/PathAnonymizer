import tkinter as tk
from tkinter import ttk
import re
import getpass
import pyperclip


class PathConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pathname Anonymizer")

        self.username = getpass.getuser()

        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.anonymize_all_users = tk.BooleanVar(value=False)
        self.checkbox = ttk.Checkbutton(
            self.frame,
            text="Anonymize all users (/Users/*)",
            variable=self.anonymize_all_users
        )
        self.checkbox.grid(row=5, column=0, columnspan=2, sticky=tk.W)

        ttk.Label(self.frame, text="Input Path or Text:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_path = tk.Text(self.frame, height=4, width=60)
        self.input_path.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(self.frame, text="Anonymized Text:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = tk.Text(self.frame, height=4, width=60)
        self.output_path.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        ttk.Button(self.frame, text="Anonymize", command=self.convert_path).grid(row=4, column=0, pady=10)
        ttk.Button(self.frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=4, column=1, pady=10)
        self.root.update_idletasks()
        self.root.minsize(self.root.winfo_width(), self.root.winfo_height())

    def replace_username_in_path(self, text):
        if self.anonymize_all_users.get():
            pattern = re.compile(r'/Users/[^/\s\"\'\n]+([^\s\"\'\n]*)')
            return pattern.sub(r'/Users/yourname\1', text)
        else:
            pattern = re.compile(r'/Users/' + re.escape(self.username) + r'([^\s\"\'\n]*)')
            return pattern.sub(r'/Users/yourname\1', text)

    def convert_path(self):
        input_text = self.input_path.get("1.0", tk.END).strip()
        if input_text:
            converted_text = self.replace_username_in_path(input_text)
            self.output_path.delete("1.0", tk.END)
            self.output_path.insert("1.0", converted_text)
        else:
            self.output_path.delete("1.0", tk.END)
            self.output_path.insert("1.0", "Please enter text")

    def copy_to_clipboard(self):
        output_text = self.output_path.get("1.0", tk.END).strip()
        if output_text and output_text != "Please enter text":
            pyperclip.copy(output_text)


def main():
    root = tk.Tk()
    app = PathConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
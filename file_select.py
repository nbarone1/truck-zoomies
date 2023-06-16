# test file for file select
# functionality used to set up container for the application

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

file_path = filedialog.askopenfilename()

save_path = [1]

save_path = filedialog.asksaveasfilename(defaultextension=".csv")
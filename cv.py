#Script that will convert the selected XLS file to a CSV named 'File' to C:\
import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() 
df = pd.read_excel('%s'%(file_path))
df.to_csv('C:\\file.csv')
print('File Successfully Converted!')

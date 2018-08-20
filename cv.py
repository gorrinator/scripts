# Script that will convert the selected XLS file to a CSV named 'File' to C:\
import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() # dialog box to select the XLS file you would like to convert.
df = pd.read_excel('%s'%(file_path))
df.to_csv('C:\\file.csv') # pre-defined path where you would like the converted file to be saved.
print('File Successfully Converted!') # message to advise the script has completed.

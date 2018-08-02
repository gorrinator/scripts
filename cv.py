import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() 
df = pd.read_excel('%s'%(file_path))
df.to_csv('C:\\Users\\bag573\\Desktop\\301_redirect.csv')
print('File Successfully Converted!')
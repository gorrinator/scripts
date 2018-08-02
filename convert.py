#Script to convert an XLS sitting in a specific directory to a CSV file in a pre-defined path
import pandas as pd
df = pd.read_excel(r'#insert file path',encoding = "ISO-8859-1")
df.to_csv(r'#insert output path',index=False,encoding = "ISO-8859-1")
print('File Successfully Converted!')

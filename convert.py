#Script to convert an XLS sitting in a specific directory to a CSV file in a pre-defined path
import pandas as pd
df = pd.read_excel(r'C:\File.xls',encoding = "ISO-8859-1") #File path of the XLS file you would like to convert.
df.to_csv(r'C:\File.csv',index=False,encoding = "ISO-8859-1") #Output path for the CSV file to be created in.
print('File Successfully Converted!') #Advises the job has been completed.

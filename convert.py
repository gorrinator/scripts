import pandas as pd
df = pd.read_excel(r'C:\Users\bag573\Desktop\301_redirect.xls',encoding = "ISO-8859-1")
df.to_csv(r'C:\Users\bag573\Desktop\301_redirect.csv',index=False,encoding = "ISO-8859-1")
print('File Successfully Converted!')
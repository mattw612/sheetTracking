import pandas as pd
import numpy as np

from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel('C:\Programming\testData\BOM_long_181030.xlsx', sheetname='Sheet1')
 
print("Column headings:")
print(df.columns)
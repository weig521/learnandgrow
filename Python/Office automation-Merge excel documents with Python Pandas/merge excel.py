# merge all xlsx excel documents in one folder
import pandas as pd
from pathlib import  Path
files = Path('Jan').glob('*.xlsx')
dfs = []
for file in files:
    dfs.append(pd.read_excel(file))
df = pd.concat(dfs)
df.to_excel('merged.xlsx',index = False)

# merge all xlsx excel files in multiple diff folders
dfs_new = []
for file in ('Jan/1-15.xlsx','Feb/1-15.xlsx'):
    dfs_new.append(pd.read_excel(file))
df_new = pd.concat(dfs_new)
df_new.to_excel('Jan Feb 1-15.xlsx',index = False)

# this might not frequetly used, merge all excel xlsx files under selected working directory
import os
file_list = os.walk("./")
result = []
for dir_path, dirs, files in file_list:
    for file in files:
        file_path = os.path.join(dir_path,file)
        print(file_path)
        if 'xlsx' in file:
            df = pd.read_excel(file_path)
            result.append(df)
print(result)
DF = pd.concat(result)
DF.to_excel('Allexcel.xlsx',index = False)
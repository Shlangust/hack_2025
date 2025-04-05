import pandas as pd
import polars as pl

# Чтение XLS файла с помощью pandas
df1 = pd.read_excel("data.xls", engine='xlrd',sheet_name='1, 2 ц.к.',skiprows=7)
df2 = pd.read_excel("data.xls", engine='xlrd',sheet_name='третья ц.к.',skiprows=5)
# print(df1.keys())
l = []
l.append([df1[3][1]+df1[4][1]+df1[5][1]+df1[6][1],df1[7][1],df1[8][1],df1[9][1],df1[10][1]]) # 1
l.append([df1[3][5]+df1[4][5]+df1[5][5]+df1[6][5],df1[7][5],df1[8][5],df1[9][5],df1[10][5]]) # 2.1 night
l.append([df1[3][6]+df1[4][6]+df1[5][6]+df1[6][6],df1[7][6],df1[8][6],df1[9][6],df1[10][6]]) # 2.1 half
l.append([df1[3][7]+df1[4][7]+df1[5][7]+df1[6][7],df1[7][7],df1[8][7],df1[9][7],df1[10][7]]) # 2.1 pike
l.append([df1[3][9]+df1[4][9]+df1[5][9]+df1[6][9],df1[7][9],df1[8][9],df1[9][9],df1[10][9]]) # 2.2 night
l.append([df1[3][10]+df1[4][10]+df1[5][10]+df1[6][10],df1[7][10],df1[8][10],df1[9][10],df1[10][10]]) # 2.2 day

print(l)
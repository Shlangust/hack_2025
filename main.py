import time
import io

import polars as pl
import os
possible_values = ['Дата', 'День', 'Число']

def read(table):
    table_stream = io.BytesIO(table)

    df = pl.read_excel(table_stream)
    a = df[df.columns[0]].to_list()
    strt = 0
    val = ''

    for value in possible_values:
        if value in a:
            strt = a.index(value)
            val = value
            break
        elif value == df.columns[0]:
            strt = 0
            val = value
            break
    df = df.slice(strt, df.height - strt)
    df_clean = df.slice(2)

    new_columns = [val] + [str(i) for i in range(24)]
    df_clean = df_clean.rename({old: new for old, new in zip(df_clean.columns, new_columns)})

    json_data = df_clean.to_dicts()

    new_data = []
    for json in json_data:
        try:
            new_data.append({val: json[val], "energy_per_hours": [float(json[str(i)]) for i in range(24)]})
        except Exception:
            pass

    return new_data


# folder_path = 'C:/hack'

# Получение списка файлов
# files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
# start_time = time.time()
# a = read(files[0],'hor')
file_path = "hor.xlsx"

# Открываем файл в бинарном режиме и получаем байты
with open(file_path, "rb") as file:
    file_bytes = file.read()
print(read(file_bytes,'ver'))
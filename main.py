import polars as pl

def read(table,format):
    df = pl.read_excel(table)
    if format == 'hor':
        a = df[df.columns[0]].to_list()
        strt = a.index('Дата')+2

        df = df.slice(strt, df.height - strt)
        print(df)
        pandas_df = df.to_pandas()

        json_data = pandas_df.to_dict(orient="records")

        return json_data
    elif format== 'ver':
        print(df)
        a = df[df.columns[0]].to_list()
        strt = a.index('Дата') + 2
        df = df.slice(strt, df.height - strt)
        print('\n\n\n\n\n\n')
        print(df)
        pandas_df = df.to_pandas()

        json_data = pandas_df.to_dict(orient="records")

        return json_data
# print(read('data.xlsx','hor')[0])
# print(read('data1.xlsx','ver')[0])
print(read('data3.xlsx','hor'))
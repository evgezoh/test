import pandas as pd

data = pd.read_excel("data.xlsx", sheetname='begin')
data1 = pd.read_excel("data.xlsx", sheetname='end')

data.set_index(['ID'], inplace=True)

print(data.sort_values(['count_of_people']))

data.reset_index(inplace=True)
data1.set_index(['ID'], inplace=True)

print(data.join(data1))

print(data.rename({'small': 'Small'}, axis=1))

print(data)

print(data[dat['column'].isin(dat1['column'])])

data['avr'] = data['small'] + data1['big']
print(data)

a = pd.DataFrame(list(range(len(data['small']))), columns=['random'])

a[ (a['random'] > 5) & (a['random'] < 100) ] = value
# a[a['random'] % 2 == 1] = list(range(len(a[a['random'] % 2 == 1])))

data1 = pd.read_excel("data.xlsx", sheetname='Лист4')

print(data1.groupby(['ID', 'col']).sum())
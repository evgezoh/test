import pandas as pd
import numpy as np
from multiprocessing import Pool, Process
import time

# Merge rename sort reset index join sum ######################################
# data = pd.read_excel("data.xlsx", sheetname='begin')
#
# data1 = pd.read_excel("data.xlsx", sheetname='end')
#
# print(data)
# print(data1)
#
# print(pd.merge(data, data1, on='ID')) // left_on right_on

#data.set_index(['ID'], inplace=True)

#print(data.sort_values(['count_of_people']))

#data.reset_index(inplace=True)
#data1.set_index(['ID'], inplace=True)

#print(data.sort_values(['count_of_people']))

#print(data.join(data1))

#print(data.rename({'small': 'Small'}, axis=1))

#data.loc[data['small'] == 'a', 'small'] = 'A'
#print(data)


#data['avr'] = data['small'] + data1['big']
#print(data)



##############################################################################################




# data = pd.read_excel("data.xlsx", sheet_name='teacher')
#
# print(data.ix[: 10, :3])
#
# print(data.iloc[: 5, : 3])
#
# print(data.loc[:, ['ID', 'square']])
#
# df = data.ix[:, -3:]
#
# std_bus_stop = df.groupby('bus_stop')['neg_factor', 'opsum'].std()
#
# std_bus_stop.rename(columns={'neg_factor': 'std_neg', 'opsum': 'std_opsum'}, inplace=True)
#
# print(std_bus_stop[~(std_bus_stop['std_opsum'] < 1500000)])
#
# print(std_bus_stop)
#
# std_bus_stop_merge = pd.merge(df, std_bus_stop, left_on='bus_stop', right_index=True)
#
# print(std_bus_stop_merge)
#
# print(std_bus_stop_merge[std_bus_stop_merge['opsum'] < std_bus_stop_merge['std_opsum']])
#
# df_eq = pd.DataFrame(data.groupby(['square', 'crossroad'])['opsum'].mean())
# df_eq.reset_index(inplace=True)
#
# df_eq.to_excel('out.xlsx', '1')

# print(pd.merge(data, df_eq, left_on='square', right_index=True))





####### Multiprocessing ################

def f(a):
    for i in a:
        print(i)
        time.sleep(0.05)
    return a


if __name__ == '__main__':

    a = list(range(1000))

    # pool = Pool(processes=8)

    prs = []
    for i in range(2):
        if not i:
            pr = Process(target=f, args=(a[:len(a)//2], ))
            prs.append(pr)
            pr.start()
        else:
            pr = Process(target=f, args=(a[len(a)//2:], ))
            prs.append(pr)
            pr.start()

    for i in range(2):
        prs[i].join()

    # Доделать



    # apply_async
    # res = []
    # res.append(pool.apply_async(func=f, args=(a[: len(a) // 2], )))
    # res.append(pool.apply_async(func=f, args=(a[len(a) // 2:], )))
    #
    # for i in range(len(res)):
    #     print(res[i].get())






























































































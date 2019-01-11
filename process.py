from multiprocessing import Process, Pool
import time
import pandas as pd


# def fun(b):
#     return b
#
#
# if __name__ == '__main__':
#
#     data = pd.read_excel('data.xlsx')
#
#     pool = Pool(processes=2)
#
#     procs = []
#
#     procs.append(pool.apply_async(func=fun, args=(data[:len(data) // 2], )))
#     procs.append(pool.apply_async(func=fun, args=(data[len(data) // 2:], )))
#
#     table_res = pd.DataFrame(procs[0].get())
#     for i in range(1, 2):
#         table_res = table_res.append(pd.DataFrame(procs[i].get()))
#
#     print(table_res)





class PRO:

    def __init__(self):
        # self.start1()
        self.start2()

    def start1(self):
        data = pd.read_excel('data.xlsx')
        pool = Pool(processes=2)

        procs = []

        procs.append(pool.apply_async(func=self.proc, args=(data[:len(data) // 2],)))
        procs.append(pool.apply_async(func=self.proc, args=(data[len(data) // 2:],)))

        pool.close()
        pool.join()

        table_res = pd.DataFrame(procs[0].get())
        for i in range(1, 2):
            table_res = table_res.append(pd.DataFrame(procs[i].get()))

        print(table_res)

    def start2(self):
        data = pd.read_excel('data.xlsx')

        procs = []

        for i in range(2):
            if i != 2:
                procs.append(Process(target=self.proc, args=(data[:len(data) // 2], )))
                procs[i].start()
            else:
                procs.append(Process(target=self.proc, args=(data[len(data) // 2:], )))
                procs[i].start()

        for i in range(2):
            procs[i].join()

    def proc(self, b):
        return b


if __name__ == '__main__':

    pr = PRO()







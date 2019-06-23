import datetime
from calendar import monthrange

self.table_opsum = pd.read_excel('data.xlsx', 'opsum')

# Преобразовать строку в дату
datetime.datetime.strptime('201812', '%Y%m').date()
# Преобразовать Series к дате и времени по формату + к дате (году, месяцу, дню)
self.table_opsum['MONTH'] = pd.to_datetime(self.table_opsum['MONTH'], format='%Y%m').dt.date # year month day
# Получить Series дней в месяце
days_in_month = self.table_opsum['MONTH'].dt.days_in_month
# Изменить время для каждой строки Series
self.table_opsum['MONTH'] = self.table_opsum['MONTH'].apply(lambda x: datetime.datetime(x.year, x.month, monthrange(x.year, x.month)[1]))


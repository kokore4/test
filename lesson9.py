from datetime import datetime, timedelta

from utils.utils1 import *

# # d = datetime.now()
# print(f'Сейчас : {d}')
# one_hour_ago = d - timedelta(hours=1)
# print(f'А час назад было: {one_hour_ago}')
# # t = timedelta(hours=1)

a = Human('Петя')
b = Human('Вася')
print(a.get_name())
print(b.get_name())

# r = Rota([a], 'Девятая рота')
# r.add_human(b)
# r.watch_rota()

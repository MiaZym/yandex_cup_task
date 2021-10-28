import pandas as pd

fixed_data = pd.read_csv('ticket_logs.csv', sep=',', names=['Name', 'Number_phone'])
print("Первые 5 строк таблицы до форматирования:\n", fixed_data.head())
fd = fixed_data.copy()

# удаление скобок, тире и плюсов
for i in range(fd['Number_phone'].size):
    fd['Number_phone'][i] = fd['Number_phone'][i].replace('+', '').replace('(', '').replace(')', '').replace('-', '')

plus = fd.loc[fd['Number_phone'].str.contains(pat="+", regex=False)] # список спектаклей, в телефонах которых есть плюсы
print("После удаления скобок, тире и плюсов: \n ", fd.head(10))


worlds = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6,
          'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9
          }

# список тех спектаклей, где у номеров есть буквы
fd1 = fd.loc[fd['Number_phone'].str.contains(pat=r'[a-z]', regex=True)]  # индексы здесь "скопированы"
fd1 = pd.DataFrame(fd1.values, index=range(len(fd1)), columns=fd1.columns)  # смена индексов на последовательные цифры

# замена цифр на буквы
for k, v in worlds.items():
    v = str(v)
    for i in range(fd['Number_phone'].size):
        fd['Number_phone'][i] = fd['Number_phone'][i].replace(k, v)

print("после удаления букв:\n", fd.head(10))
# преобразую все номера в целый тип
for i in range(fd['Number_phone'].size):
    fd['Number_phone'][i] = int(fd['Number_phone'][i])

# удаление дублирующих номеров
fd = fd.drop_duplicates(subset=['Number_phone'], keep=False)
fd = pd.DataFrame(fd.values, index=range(len(fd)), columns=fd.columns) # снова трогаем индексы

# группировка и получение всех спектаклей и список телефонов для каждого соответственно
all_spectacle = fd.groupby('Name')['Number_phone'].apply(list).reset_index(name='list of number')
all_spectacle.to_csv("all_spectacle.csv")
print(all_spectacle)

print("Количество уникальных значений:\n", len(fd['Number_phone']))




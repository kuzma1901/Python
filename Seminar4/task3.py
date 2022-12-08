data = open('file.txt', 'w')
data.write('\nАнгела Меркель 5\n')
data.write('\nЭнакин Скайуокер 5\n')
data.write('\nФредди Меркури 3\n')
data.write('\nАлександр Пушкин 4\n')
data.close


dict = {'Ангела Меркель': '5', 'Энакин Скайуокер': '5',
          'Фредди Меркури': '3', 'Александр Пушкин': '4'}
for k in dict.values():
    k = int
    if k <= 4:
        str.upper(dict)
    


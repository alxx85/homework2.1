import module

def open_book():
    cook_book = {}
    list_book = ['ingridient_name', 'quantity', 'measure']
    with open('cookbook.txt') as f:
        for line in f:
            key = line.strip()
            if key not in cook_book:
                cook_book[key] = list()
            quantity = f.readline().strip()
            i = 0

            while i < int(quantity):
                lines = f.readline().strip()
                lines_list = lines.split(' | ')
                value = dict()
                for lst, lines_numb in enumerate(lines_list):
                    value[list_book[lst]] = lines_numb
                cook_book[key].append(value)
                i += 1
            f.readline()
    return cook_book


book = open_book()

dishes_list = list()
print('Список рецептов из книги:')
for key in book:
    print(key)

dishes_promt = input('\nВведите названия рецептов через запятую: ')
if ', ' in dishes_promt:
    dishes_list = dishes_promt.split(', ')
else:
    dishes_list.append(dishes_promt)

person = int(input('Введите колличество персон: '))

if person != '':
    module.get_shop_list_by_dishes(book, dishes_list, person)
else:
    print('Неверно указанно колличество персон!!!')

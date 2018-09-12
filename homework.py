from pprint import pprint

cook_book = {}
with open('cookbook.txt') as f:
    for line in f:
        key = line.strip()
#        print(key)
        if key not in cook_book.keys():
            cook_book[key] = list()
        quantity = f.readline().strip()
        i = 0
        line_list = []

        while i < int(quantity):
            lines = f.readline().strip()
            lines_list = lines.split(' | ')
            value = dict.fromkeys(['ingridient_name', 'quantity', 'measure'])
            value['ingridient_name'] = lines_list[0]
            value['quantity'] = lines_list[1]
            value['measure'] = lines_list[2]
            cook_book[key].append(value)
            i += 1
        f.readline()

dishes_list = list()
print('Список рецептов из книги:')
for key in cook_book.keys():
    print(key)

dishes_promt = input('\nВведите названия рецептов через запятую: ')
if ', ' in dishes_promt:
    dishes_list = dishes_promt.split(', ')
else:
    dishes_list.append(dishes_promt)

person = input('Введите колличество персон: ')

def get_shop_list_by_dishes(book_cook, dishes, person_count):
    book = {}
    for dishe in dishes:
        quantity = 0
        for list_book in book_cook[dishe]:
            key = book_cook[dishe][quantity]['ingridient_name']
            if key not in book.keys():
                book[key] = dict.fromkeys(['quantity', 'measure'])
                book[key]['quantity'] = int(book_cook[dishe][quantity]['quantity']) * int(person_count)
                book[key]['measure'] = book_cook[dishe][quantity]['measure']
            else:
                book[key]['quantity'] += int(book_cook[dishe][quantity]['quantity']) * int(person_count)

            quantity += 1

    pprint(book)
if (person != '') and (type(person) == int ):
    get_shop_list_by_dishes(cook_book, dishes_list, person)
else:
    print('Неверно указанно колличество персон!!!')
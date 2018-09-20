from pprint import pprint

def get_shop_list_by_dishes(book_cook, dishes, person_count):
    book_recipe = {}
    for dishe in dishes:
        for lst_numb in range(len(book_cook[dishe])):
            key = book_cook[dishe][lst_numb]['ingridient_name']
            if key not in book_recipe:
                book_recipe[key] = dict()
                book_recipe[key]['quantity'] = int(book_cook[dishe][lst_numb]['quantity']) * int(person_count)
                book_recipe[key]['measure'] = book_cook[dishe][lst_numb]['measure']
            else:
                book_recipe[key]['quantity'] += int(book_cook[dishe][lst_numb]['quantity']) * int(person_count)

    pprint(book_recipe)

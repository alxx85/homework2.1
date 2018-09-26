from pprint import pprint

def get_shop_list_by_dishes(book_cook, dishes, person_count):
    book_recipe = {}
    for dishe in dishes:
        for ingredient in book_cook[dishe]:
            key = ingredient['ingridient_name']
            if key not in book_recipe:
                book_recipe[key] = dict()
                book_recipe[key]['quantity'] = int(ingredient['quantity']) * int(person_count)
                book_recipe[key]['measure'] = ingredient['measure']
            else:
                book_recipe[key]['quantity'] += int(ingredient['quantity']) * int(person_count)

    pprint(book_recipe)

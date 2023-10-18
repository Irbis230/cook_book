def read_recipes(ingredients=None):
    recipes = []
    with open('a.txt', 'r', encoding='utf-8') as file:
        cook_book = {}
        print(file)
                for items in file:
                    ingredient_data = lines[i].strip().split('|')
                    ingredient = {
                        'название ингредиента': ingredient_data[0].strip(),
                        'количество': ingredient_data[1].strip(),
                        'единица измерения': ingredient_data[2].strip(),
                    }
                    ingredients.append(ingredient)
                    i += 1
                recipe['ингредиенты'] = ingredients
                recipes.append(recipe)
            except Exception as e:
                print(f"Ошибка в парсинге рецепта: {e}")
                i += 1
    return recipes
file_name = 'recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count, recipes):
    shop_list = {}
    for dish_name in dishes:
        for recipe in recipes:
            if recipe['название'] == dish_name:
                for ingredient in recipe['ингредиенты']:
                    ingredient_name = ingredient['название ингредиента']
                    measure = ingredient['единица измерения']
                    quantity = int(ingredient['количество']) * person_count

                    if ingredient_name not in shop_list:
                        shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
                    else:
                        if shop_list[ingredient_name]['measure'] == measure:
                            shop_list[ingredient_name]['quantity'] += quantity
                        else:
                            print(f"Единицы измерения для '{ingredient_name}' не совпадают. Проверьте рецепты.")
    return shop_list

if __name__ == "__main__":
    file_path = "cook_book.txt"
    recipes = read_recipes(file_path)
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes, person_count, recipes)

    for ingredient, info in shop_list.items():
        print(f"{ingredient}: {info['quantity']} {info['measure']}")
# import random
# import json

# info_way = '/home/hello/Desktop/hacaton/info.json'
# id_number = '/home/hello/Desktop/hacaton/id.txt'

# def get_data():
#     with open(info_way) as file:
#         return json.load(file)


# def list_of_products():
#     data = get_data()
#     return f'Список всех товаров: {data}'

# def save_info(data):
#     with open(info_way, 'w') as file:
#         json.dump(data, file)

# def info_product():
#     data = get_data()
#     try:
#         id = int(input('Введите id продукта: '))
#         product = list(filter(lambda x: id == x['id'], data))
#         return product[0]
#     except:
#         return 'Введен неверный id!'

# def get_id():
#     with open(id_number) as file:
#         id = int(file.read())
#         id += 1
#     with open(id_number, 'w') as file:
#         file.write(str(id))
#     return id


# def create_product():
#     data = get_data()
#     try:
#         product = {
#             'id': get_id(),
#             'brand': input('Введите марку товара: '),
#             'model': input('Введите модель товара: '),
#             'year': int(input('Введите год выпуска товара: ')),
#             'description': input('Введите описание: '),
#             'price': round(float(input('Введите цену продукта: ')), 2)
#         }
#     except: 
#         return 'Неверные данные!'
#     data.append(product)
#     save_info(data)
#     return 'Создан новый товар!'

# def update_product():
#     data = get_data()
#     try:
#         id = int(input('Введите id продукта который Вы хотите изменить: '))
#         product = list(filter(lambda x: x['id'] == id, data))[0]
#         print(f'Товар для обновления: {product["brand"]}')
#     except:
#         return 'Введен неверный id!'

#     index = data.index(product)
#     choice = input('Что Вы хотите изменить?(1-brand, 2-model, 3-year, 4-description, 5-price): ')
#     if choice.strip() == '1':
#         data[index]['brand'] = input('Введите новое название марки: ')
#     elif choice.strip() == '2':
#         data[index]['model'] = input('Введите новое название модели: ')
#     elif choice.strip() == '3':
#         try:
#             data[index]['year'] = int(input('Введите новый год выпуска товара: '))
#         except:
#             return 'Неверное значение для цены!'
#     elif choice.strip() == '4':
#         data[index]['description'] = input('Введите новое описание товара: ')
#     elif choice.strip() == '5':
#         try:
#             data[index]['price'] = round(float(input('Введите новую цену для товара: ')), 2)
#         except:
#             return 'Неверное значение для цены!'
#     else:
#         return 'Неверное значение для обновления!'
#     save_info(data)
#     return 'Товар обнолён!'



# def delete_product():
#     data = get_data()
#     try:
#         id = int(input('Введите id продукта: '))
#         product = list(filter(lambda x: x['id'] == id, data))[0]
#         print(f'Товар для удаления {product["brand"]}')
#     except:
#         return 'Введен неверный id!'
#     choice = input('Удалить этот товар?(yes/no)')
#     if choice.lower().strip() != 'yes':
#         return 'Товар не удален!'
#     else:
#         data.remove(product)
#         save_info(data)
#         return 'Товар удален!'


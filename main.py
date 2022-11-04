# from func import list_of_products, info_product, delete_product, create_product, update_product

# def main():
#     print('Здравствуйте! В нашем маркет-плейсе Вы можете совершать следующие действия: \n\tСписок товаров-1\n\tДетальный обзор-2\n\tСоздать товар-3\n\tИзменить товар-4\n\tУдалить товар-5')
#     choice = (input('Введите действие(1,2,3,4,5): '))
#     if choice.strip() == '1':
#         print(list_of_products())
#     elif choice.strip() == '2':
#         print(info_product())
#     elif choice.strip() == '3':
#         print(create_product())
#     elif choice.strip() == '4':
#         print(update_product())
#     elif choice.strip() == '5':
#         print(delete_product())
#     else:
#         print('Неверный выбор!')

#     answer = input('Хотите продолжить?(yes/no)')
#     if answer.lower().strip() == 'yes':
#         main()
#     else:
#         print('До свидания!')
    
# main()
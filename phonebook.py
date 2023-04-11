import os

def add_person():
    last_name = input('Введите фамилию: ') # 'Иванов'
    name = input('Введите имя: ') # 'Иван'
    surname = input('Введите отчество: ') #'Иванович'
    phone = input('Введите номер телефона: ') #'9784561230'
    data = open('C:\\Users\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt' ,'a', encoding='utf-8')
    data.writelines([last_name,' ', name, ' ', surname, ' ', phone, '\n']) # 1-й вар.
    #data.writelines([last_name + ' ', name + ' ', surname + ' ', phone]) #2-й вар.
    data.close()

def print_data():
    with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())

def search():
    search_name = input('Введите данные: ')
    with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)

def load_data():
    with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in text_data:
                    data.write(line)

def change_contact():
    print('Для изменения контакта: ')
    card = search()
    with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'r', encoding="utf-8") as data: 
        all = data.readlines() 
        for i in range(len(all)): 
            if card == all[i]: 
                new_contact = input("Введите новые данные контакта: ") 
                all[i] = new_contact
                cont_2 = ''.join(all) 
                with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'w', encoding="utf-8") as data: 
                    data.write(f'{cont_2}')
                    print ('Контакт изменён')                                       

def remove_contact():
    with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'r', encoding='utf-8') as data:
        X = input('Введите данные для удаления: ')
        lines = data.readlines()
        with open('C:\\Users\\Юлия\\Desktop\\дзпайтон\\дз8\\files\\phonebook.txt', 'w', encoding='utf-8') as data:
            for line in lines:
                if X in line:
                    print("Контакт удален")
                else:
                    print(line)    
                    data.write(line)          

def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - изменить контакт
6 - удалить контакт
7 - выход''')
    user_input = input('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        change_contact()        
    elif user_input == '6':
        remove_contact()       
    elif user_input != '7':    
        print('Не правильный ввод') 
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - изменить контакт
6 - удалить контакт
7 - выход''')
        user_input = input('Введите нужный вариант: ')

def main():
    ui()

if __name__ == "__main__":
    main()
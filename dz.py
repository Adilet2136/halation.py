# 1. Создайте файл data.json с произвольными данными.
# Напишите программу, которая загружает его содержимое в Python-объект и выводит на экран

import json
with open('data.json') as file:
    python_data=json.load(file)
    print(python_data)








# 2) Создайте словарь с данными о пользователе (name, age, email).
# Запишите его в файл user.json


user ={"name":"sultan","age":21,
"email":"tlbks@gmail.com"}

with open('user.json','w') as file:
    json.dump(user,file) 


# 3) Дана JSON-строка:
# '{"product": "Laptop", "price": 1200, "in_stock": true}'
# Преобразуйте ее в Python-словарь и выведите значение ключа "price".
import json 
jason ='{"product": "Laptop", "price": 1200, "in_stock": true}'
jason = json.loads(jason)
print(jason.get('prise'))

# 4) Дан файл products.json с массивом товаров (id, name, price).
# Напишите функцию, которая принимает id товара и возвращает его данные.
# [
#   {"id": 1, "name": "Laptop", "price": 1200},
#   {"id": 2, "name": "Smartphone", "price": 800},
#   {"id": 3, "name": "Tablet", "price": 500}
# ]

def get_info (x):
    with open ('products.json') as file:
        list_=json.load(file)

    for i in list_:
        if x == i.get('ic'):
            return i
        
print(get_info(3)) 
# 5) Дан config.json с настройками программы:
# {
#   "theme": "light",
#   "language": "en",
#   "volume": 70
# }
# Напишите функцию, которая изменяет переданный параметр (например, theme → "dark") и сохраняет изменения.

# 6) Дан students.json, содержащий список студентов с их баллами.
# Напишите функцию, которая фильтрует студентов с баллом выше 80 и сохраняет их в top_students.json.
# [
#   {"name": "Alice", "score": 85},
#   {"name": "Bob", "score": 78},
#   {"name": "Charlie", "score": 90},
#   {"name": "Dave", "score": 65}
# ]

# 7) Есть два файла: employees1.json и employees2.json, содержащие списки сотрудников.
# Напишите программу, которая объединяет их в один список и сохраняет в all_employees.json, исключая дубликаты

# employees1.json:
# [
#   {"id": 1, "name": "John Smith", "department": "HR"},
#   {"id": 2, "name": "Jane Doe", "department": "IT"}
# ]

# employees1.json:
# [
#   {"id": 2, "name": "Jane Doe", "department": "IT"},
#   {"id": 3, "name": "Emily Johnson", "department": "Marketing"}
# ]

# 8) Создайте log.json, в который можно записывать события вида:
# {"timestamp": "2025-03-10 12:30:45", "event": "User logged in", "user_id": 123}
# Напишите функцию log_event(event, user_id), которая добавляет новую запись в этот файл.
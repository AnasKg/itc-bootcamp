########## Пример добавления данных(INSERT) ###########
import psycopg2

# Выполняется соединение с базой данных, указывается название БД, user, хост и пароль
connection = psycopg2.connect(
    dbname='market', user='ulan', password='123', host='localhost')


# Курсор предназначен для общения с БД, т.е. выполнение SQL команд
cursor = connection.cursor()

query_for_select_product_types = 'SELECT * FROM product_types'
cursor.execute(query_for_select_product_types)

records = cursor.fetchall()  # это переменная содержит список записей в виде tuple
print(records)


# Выполняем запрос через курсор
# Чтобы передать значение в запрос вставляем %s в запрос, и передаем значение в массиве
cursor.execute('INSERT INTO product_types (product_type_name) VALUES (%s);', ('новый тип продукта',))

print('Результат после добавления!')
cursor.execute(query_for_select_product_types)

records = cursor.fetchall()  # это переменная содержит список записей в виде tuple
print(records)

# в конце после выполнения запросов надо закрывать курсор и соединение с БД
cursor.close()
connection.close()

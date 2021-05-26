
########## Пример выборки с передачей данных ###########
import psycopg2

# Выполняется соединение с базой данных, указывается название БД, user, хост и пароль
connection = psycopg2.connect(
    dbname='market', user='ulan', password='123', host='localhost')


# Курсор предназначен для общения с БД, т.е. выполнение SQL команд
cursor = connection.cursor()


# Выполняем запрос через курсор
# Чтобы передать значение в запрос вставляем %s в запрос, и передаем значение в массиве
cursor.execute('SELECT * FROM product_types WHERE product_type_id=%s', (3,))

''' Для того чтобы получить результат запроса используются следующие функции:
    * fetchone() - возвращает 1 строку
    * fetchall() - возвращает список(list) всех строк
    * fetchmany(size=3) - возвращает заданное количество строк
'''

records = cursor.fetchall()  # это переменная содержит список записей в виде tuple

print(records)

# в конце после выполнения запросов надо закрывать курсор и соединение с БД
cursor.close()
connection.close()

import psycopg2

# Выполняется соединение с базой данных, указывается название БД, user, хост и пароль
connection = psycopg2.connect(dbname='market', user='ulan', password='123', host='localhost')


# Курсор предназначен для общения с БД, т.е. выполнение SQL команд
cursor = connection.cursor()

########## Пример выборки данных с таблицы (SELECT) ###########
# Пишем запрос как string
query_for_select_product_types = 'SELECT * FROM product_types'

# Выполняем запрос через курсор
cursor.execute(query_for_select_product_types)

''' Для того чтобы получить результат запроса используются следующие функции:
    * fetchone() - возвращает 1 строку
    * fetchall() - возвращает список(list) всех строк
    * fetchmany(size=3) - возвращает заданное количество строк
'''

records = cursor.fetchall() # это переменная содержит список записей в виде tuple

print(records)

# так как переменная records является списком(list) можно пройтись по циклу
for record in records:
    print(record)

# в конце после выполнения запросов надо закрывать курсор и соединение с БД
cursor.close()
connection.close()

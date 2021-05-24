import psycopg2

connection = psycopg2.connect(dbname='main',
	user='hidden', host='localhost', password='123')

cursor = connection.cursor()

zapros = "SELECT * FROM users LIMIT 2"

cursor.execute(zapros)

res = cursor.fetchall()
print(res)

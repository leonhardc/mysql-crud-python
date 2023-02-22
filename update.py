import mysql.connector
import datetime

connection = mysql.connector.connect(
    host='localhost', #your host
    user='Leonardo', #your user
    password='8BItp2mnaDzeGgMN', # your user password
    database='teste' #your database
)

cursor = connection.cursor()

sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
data = (
    'Segundo usuário editado',
    'segundousuarioeditado@teste.com.br',
    2
)

cursor.execute(sql, data)
connection.commit()

recordsAffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsAffected, ' registros afetados.')
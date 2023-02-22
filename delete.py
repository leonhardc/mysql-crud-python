# how to delete a data from database by Leonardo Rodrigues

import mysql.connector
import datetime


connection = mysql.connector.connect(
    host='localhost',
    user='Leonardo',
    password='8BItp2mnaDzeGgMN',
    database='teste'
)

cursor = connection.cursor()

sql = "DELETE FROM users WHERE id = %s"
data = (2, )

cursor.execute(sql, data)
connection.commit()

recordsAffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsAffected, ' registros afetados.')
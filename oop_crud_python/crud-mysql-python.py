import mysql.connector
import datetime

class CrudMysql:

    def __init__(self, host=None, user=None, password=None, database=None) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        if(self.host is None or self.user is None or self.password is None or self.database is None):
            print("Error: don't init the object. Plase, check the arguments correctly.")
            return

        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except:
            print("Error: it's not possible connect")
            return


    def create(self, name=None, email=None, date=None):
        # inset a data to database
        if(name is None or email is None):
            print('Error: name or email is None.')
            return

        if(date is None):
            date = datetime.datetime.today()
        
        cursor = self.connection.cursor()
        sql = "INSERT INTO users (name, email, created) VALUES (%s,%s,%s)"


        data = (name, email, date)
        cursor.execute(sql, data)
        self.connection.commit()
        userid = cursor.lastrowid
        cursor.close()

        print('Foi cadastrado um novo usuário de ID: ', userid)


    def read(self):
        # read all rows from database
        cursor = self.connection.cursor()
        sql = 'SELECT * FROM users'

        cursor.execute(sql)
        results = cursor.fetchall()

        cursor.close()

        return results

    def update(self, id=None, name=None, email=None):
        # update name and email to database
        cursor = self.connection.cursor()

        if(name is not None and email is not None):        
            sql = "UPDATE users SET name=%s, email=%s WHERE id=%s"
            data = (name, email, id)
        
        if(name is None):
            sql = "UPDATE users SET email=%s WHERE id=%s"
            data = (email, id)
        
        if(email is None):
            sql = "UPDATE users SET name=%s WHERE id=%s"
            data = (name, id)

        cursor.execute(sql, data)
        self.connection.commit()

        recordsAffected = cursor.rowcount

        cursor.close()

        print(recordsAffected, ' registros afetados.')

        return

    
    def delete(self, id=None):
        # delete a row from database
        if(id is None):
            print('Error: id is None')
            return

        cursor = self.connection.cursor()

        sql = "DELETE FROM users WHERE id = %s"
        data = (id,)

        cursor.execute(sql, data)
        self.connection.commit()

        recordsaffected = cursor.rowcount

        cursor.close()

        print(recordsaffected, " registros excluídos")
        return

    def close_connection(self):        
        self.connection.close()
        return True



        


        



import connection
from connection import Error

class Read_Table(connection.Connection):
    def __init__(self, database):
        super().__init__(database)

    def read_table(self, table):
        result = None
        query = "SELECT * FROM %s" %table
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print('An error occured.\ne')

    def read_row(self, table):
        try: 
            query = "SELECT * FROM %s" %table
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Error as e:
            print('An error occured.\ne')

    def read_rows(self, table, column, value):
        try:
            query = "SELECT * FROM %s WHERE %s = %s" %table %column %value
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Error as e:
            print('An error occured\ne')





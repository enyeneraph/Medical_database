import connection
from connection import Error

class Update_Table(connection.Connection):
    def __init__(self, database):
        super().__init__(database)
    
    def alter_table(self,):
        pass

    def insert_values(self, table, data):
        query = "INSERT INTO %s VALUES(%s, %s ..s)" %table
        data = [(val, val, ...), (val, val, ...)]

        try:
            self.cursor.executemany(query, data)
        except Error as e:
            print('An error occured\ne')



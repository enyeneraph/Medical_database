import connection
from connection import Error



class Database(connection.Connection):
    # A class for creating and deleting database.
    def __init__(self, database):
        super().__init__()
        query = 'CREATE DATABASE %s' %database

        try:
            self.command_handler(query)
            print('Database created successfully')

        except Error as e:
            print('An error occured/n {}'.format(e))

    
    def delete_db(self,database):
        '''deletes a database'''
        try:
            query = 'DROP DATABASE %s' %database
            self.command_handler(query)
            print('%s successfully deleted' %database)
        except Error as e:
            print('An error occured/n {}'.format(e))






        

a = Database('ebenezer')
a.delete_db('ebenezer')
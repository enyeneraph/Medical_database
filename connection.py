import mysql.connector
from mysql.connector import Error


class Connection:
    '''Connects the admin to the mysql and  an existing database.''' 
    def __init__(self, database = None):
        self.database = database
        try:
            self.connection = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                password = 'bobo23',
                database = self.database)


            print('Database connection successful')

            self.cursor = self.connection.cursor()
        except Error as e:
            print('An error occured.\nDatabase not created\n{}'.format(e))
    
    def command_handler(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print('An error occured.\n{}'.format(e))
    


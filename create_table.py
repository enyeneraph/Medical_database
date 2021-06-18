import connection
from connection import Error

tables = {}

def column(*args, sep = ' '):
    try:
        return sep.join(args)
    except Error as e:
        return 'oops! An error occured. Ensure that your values are entered in the right order as required by mysql.'

def columns(*args, sep= ', '):
    try:
        return sep.join(args)
    except Error:
        print('An error occured')

def create_table_query(name, columns):
    return ("CREATE TABLE %s (%s)" %name %columns)

def create_table(database, query):
    db = connection.Connection(database)
    for i in tables:
        db.command_handler(tables[i])


v = column('id', 'int', 'NOT NULL', 'AUTO_INCREMENT', 'PRIMARY KEY')
s = column('specialty', 'VARCHAR(100)', 'NOT NULL', 'UNIQUE KEY')

q = columns(v,s)
#this strategy is demanding for the user trying to create a table. Another strategy would be to have the user type it in the way they would in mysql, then have a set of fuctions break it down for python.

# # tables['Specialties'] = ("CREATE TABLE specialties(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, specialty VARCHAR(100) NOT NULL UNIQUE KEY)")
#create table format here

# def column(col_name, d_type, default = 'NULL', increment = '', key='', reference_definition = '' ):
#     return col_name + ' ' +  d_type + ' ' +  default + ' ' + increment + ' ' + ' ' +  key + ' ' + reference_definition


# tables['Specialties'] = ('CREATE TABLE specialties(' + v + ', ' + s  + ')')
# tables['Doctor'] = ("CREATE TABLE doctors(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200) NOT NULL, gender CHAR(1) NOT NULL, years_of_practice INT NOT NULL, specialty VARCHAR(100), FOREIGN KEY(specialty) REFERENCES Specialties(Specialty))")
# tables['Diagnoses'] = ("CREATE TABLE Diagnoses(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, diagnoses VARCHAR(200) NOT NULL UNIQUE KEY) ")
# tables['Patients'] = ("CREATE TABLE patients(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(200) NOT NULL, gender CHAR(1) NOT NULL, age INT NOT NULL, diagnoses VARCHAR(200) NOT NULL, FOREIGN KEY(diagnoses) REFERENCES Diagnoses(diagnoses))")

def create_table(database, query):
    db = connection.Connection(database)
    for i in tables:
        db.command_handler(tables[i])

# create_tables('medical_records')
















# class Table(connection.Connection):
#     def __init__(self, database, tbl_name,):
#         try:
#             super().__init__(database)

#             query = 'CREATE TABLE %s(%s)' %tbl_name %args
#             self.cursor.execute(query)
#             print('Table created successfully')
#         except Error as e:
#             print('Oops! an error occured\ne')



#     def delete_tb(self, tbl_name):
#         try:
#             query = 'DROP TABLE %s' %tbl_name
#             self.cursor.execute(query)
#         except Error as e:
#             print('Oops! an error occured\ne')




# b = Table('test1', 'test7', 'name VARCHAR(20), gender CHAR(1)' )
# b.delete_tb('test7')
import pyodbc

server = 'potential.database.windows.net'
database = 'MyDatabase'
username = 'potential'
password = 'CN240opp'
driver = '{SQL Server}'
conn = pyodbc.connect(
    'DRIVER=' + driver +
    ';SERVER=' + server +
    ';PORT=1433'
    ';DATABASE=' + database +
    ';UID=' + username +
    ';PWD=' + password)
cursor = conn.cursor()

# This use to create table but I don't want to create another
# then I'll not make it to be create table function

cursor.execute(f"CREATE TABLE MLD(\
                Name nvarchar(50),\
                Status int,\
                CDR float,\
                id nvarchar(255))")

"""
sql = ('''
        INSERT INTO MyDatabase.dbo.MLD (Name, Status, CDR, id)
        VALUES
        ('n0002.png',0,2.40,'XYA12')
       ''')
cursor.execute(sql)
"""

conn.commit()

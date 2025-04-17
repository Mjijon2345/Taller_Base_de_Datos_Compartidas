import pyodbc

def conectar():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MATEO;'
        'DATABASE=TechStore;'
        'Trusted_Connection=yes;'
    )

import pyodbc
import pandas as pd

#Necessário a instalação do driver ODBC para SQL SERVER

#link para download: https://docs.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15

#String de conexão para localizar os bancos de dados corretos

params = '''DRIVER={ODBC Driver 17 for SQL Server};
            SERVER=tcp:fgv-db-server.database.windows.net,1433;
            DATABASE=fgv-db;
            Persist Security Info={False};
            UID=student;
            PWD=@dsInf123;
            MultipleActiveResultSets=False;
            Encrypt =True;
            TrustServerCertificate =False;
            Connection Timeout=30;'''
            
#Usando a biblioteca pyodbc para fazer a conexão
cnxn = pyodbc.connect(params)

#Query para mostrar tabelas disponíveis para acesso
sql = """SELECT * FROM INFORMATION_SCHEMA.TABLES"""

#Usando pandas para fazer dataframe das queries
df = pd.read_sql(sql, cnxn)

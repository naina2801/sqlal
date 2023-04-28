# import shutil
# var = shutil.copy(r'\\WusAzeUat13\SIG2FileServer\Docbase/2023\04\19\QMT-00001\INC-0000018401\alumasc.pdf', r'C:\Users\Unaina\Desktop\vj anna\13-04\SIG\SIG\Test\alumasc.pdf')
# print(var)


import pandas as pd
import pyodbc as odbc
# from sqlalchemy import *

conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=SAUAZEDBS04;'
    r'DATABASE=Extract_AMX;'
    r'UID=extract_readonly;'
    r'PWD=CW@F2q@VSw1g;'
)
cnxn = odbc.connect(conn_str)
# cursor = cnxn.cursor()
# with engine.begin() as conn:
df = pd.read_sql_query('''
select document_id,document_processed_status,document_modified_on,document_created_on,invoice_number,additional_field_1,additional_field_2,additional_field_3,invoice_apicall_status,document_remark
from tbl_documents as doc INNER JOIN tbl_invoices as inv ON doc.document_id = inv.invoice_document_id
where cast(document_created_on as date)= '2023-04-24' and document_processed_status = 'failed'   order by 1 desc;''',cnxn)
print(df.to_string())
# -----------------------------------------------------
# import pandas as pd
# import pyodbc as odbc
# from sqlalchemy.engine import URL
# conn = URL.create(
#     "mssql+pyodbc",
#     username="extract_readonly",
#     password="CW@F2q@VSw1g",
#     host="SAUAZEDBS04",
#     database="Extract_AMX",
#     DRIVER='{SQL Server}'
# )
# cnxn = odbc.connect(conn)
# df = pd.read_sql_query('select * from tbl_suppliers',cnxn)
# print(df.to_string())

#-----------------------------------------------
#-------------------------------
# import pandas as pd
# import pyodbc
# import sqlalchemy as sa
# import urllib
# from sqlalchemy import create_engine, event
# from sqlalchemy.engine.url import URL
#
# server = 'SAUAZEDBS04'
# database = 'Extract_AMX'
# username = 'extract_readonly'
# password = 'CW@F2q@VSw1g'
#
# params = urllib.parse.quote_plus("DRIVER={SQL Server};"
#                                  "SERVER=" + server + ";"
#                                                       "DATABASE=" + database + ";"
#                                                                                "UID=" + username + ";"
#                                                                                                    "PWD=" + password + ";")
#
# engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
#
# qry = "SELECT t.[group] as [Region],t.name as [Territory],C.[AccountNumber]"
# qry = qry + "FROM [Sales].[Customer] C INNER JOIN [Sales].SalesTerritory t on t.TerritoryID = c.TerritoryID "
# qry = qry + "where StoreID is not null and PersonID is not null"
#
# with engine.connect() as con:
#     rs = con.execute(qry)
#
#     for row in rs:
#         print(row)

#
# import pandas as pd
# from sqlalchemy import create_engine, text
# from sqlalchemy.engine.url import URL
# conn_str = (
#     r'DRIVER={SQL Server};'
#     r'SERVER=SAUAZEDBS04;'
#     r'DATABASE=Extract_AMX;'
#     r'UID=extract_readonly;'
#     r'PWD=CW@F2q@VSw1g;'
# )
#
# conn_url = URL.create("mssql+pyodbc", query={"odbc_connect": conn_str})
# engine = create_engine(conn_url)
# df = pd.read_sql_query('select * from tbl_suppliers', engine)
# print(df)

# from sqlalchemy import create_engine
# import pandas as pd
# DRIVER='SQL Server'
# SERVER='SAUAZEDBS04'
# DATABASE='Extract_AMX'
# UID='extract_readonly'
# PWD='CW@F2q@VSw1g;'
# DATABASE_CONNECTION = f'mssql://{UID}:{PWD}@{SERVER}/{DATABASE}?driver={DRIVER}'
# engine = create_engine(DATABASE_CONNECTION)
# connection = engine.connect()
# df = pd.read_sql_query("SELECT * FROM [dbo].[tbl_suppliers]",connection)
# print(df)
# import pandas as pd
# from sqlalchemy import create_engine
# import pyodbc
# import os
# conn_str = (
#     r'DRIVER={SQL Server};'
#     r'SERVER=SAUAZEDBS04;'
#     r'DATABASE=Extract_AMX;'
#     r'UID=extract_readonly;'
#     r'PWD=CW@F2q@VSw1g;'
# )
# def mssql_engine(user = os.getenv('UID'), password = os.getenv('PWD')
#                  ,host = os.getenv('SERVER'),db = os.getenv('DATABASE')):
#     engine = create_engine(f'mssql+pyodbc://{user}:{password}@{host}/{db}?driver=SQL+Server')
#     return engine
# query = 'SELECT * FROM [tbl_suppliers]'
# df = pd.read_sql(query, mssql_engine())
# print(df)



# import pandas as pd
# import pyodbc as odbc
#
# conn_str = (
#     r'Driver = {SQL Server};'
#     r'Server = SAUAZEDBS04;'
#     r'Database = Extract_AMX;'
#     r'Trust_Connection = yes;'
# )
# cnxn = odbc.connect(conn_str)
#
# query = "SELECT * FROM "
# df = pd.read_sql(query, sql_conn)
# df.head()




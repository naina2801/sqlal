
from sqlalchemy import *
import pandas as pd
from sqlalchemy.orm import sessionmaker


tbl_name = 'tbl_suppliers'
params =("DRIVER={SQL Server};"
         "SERVER=SAUAZEDBS04;"
         "DATABASE=Extract_AMX;"
         "UID=extract_readonly;"
         "PWD=CW@F2q@VSw1g")

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
query = '''select document_id,document_processed_status,document_modified_on,document_created_on,invoice_number,additional_field_1,additional_field_2,additional_field_3,invoice_apicall_status,document_remark
from tbl_documents as doc INNER JOIN tbl_invoices as inv ON doc.document_id = inv.invoice_document_id
where cast(document_created_on as date)= '2023-04-28' and document_processed_status = 'failed' order by 1 desc;'''
# Session = sessionmaker(bind=engine)
# session = Session()
# df = pd.read_sql_query(sql=text(query), con=engine.connect())
# print(df.to_string())
# st = session.query('tbl_warehouses')
#
# for std in st:
#     print(std)
# with engine.connect() as conn:
#     for row in conn.execute(st):
#         print(row)
# tbl = session.query('tbl_suppliers')
# for tb in tbl:
#     print(tb.supplier_name)
with engine.connect() as conn:

    result = conn.execute(text("select * from {}".format(tbl_name))).fetchall()
    print(result)
    df = pd.read_sql_query(sql=text(query), con=engine.connect())
    print(df.to_string())

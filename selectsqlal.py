from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
import pandas as pd
from sqlalchemy import or_

db_uri = ("DRIVER={SQL Server};"
          "SERVER=SAUAZEDBS04;"
          "DATABASE=Extract_AMX;"
          "UID=extract_readonly;"
          "PWD=CW@F2q@VSw1g")
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(db_uri))

joinqu = '''
select document_id,document_processed_status,document_modified_on,document_created_on,invoice_number,additional_field_1,additional_field_2,additional_field_3,invoice_apicall_status,document_remark
from tbl_documents as doc INNER JOIN tbl_invoices as inv ON doc.document_id = inv.invoice_document_id
where cast(document_created_on as date)= '2023-04-27' and document_processed_status = 'failed'  order by 1 desc;
'''

meta = MetaData()
table = Table('tbl_suppliers',
              meta,
              autoload=True,
              autoload_with=engine
              )

# select * from 'user'
select_st = select([table])
conn = engine.connect()
res = pd.read_sql_query(sql=(select_st), con=engine.connect())
print(res.to_string())
# df = pd.read_sql_query(sql=(joinqu), con=engine.connect())
# print(df.to_string())

    # .where(
   # table.c.l_name == 'Hello')

# for _row in res:
#     print(_row)
#

#
# tbl_name = 'tbl_suppliers'
# params = urllib.parse.quote_plus
#
# engine = create_engine()
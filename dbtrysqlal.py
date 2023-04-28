
from sqlalchemy import *
from sqlmodel import *
params =("DRIVER={SQL Server};"
         "SERVER=SAUAZEDBS04;"
         "DATABASE=Extract_AMX;"
         "UID=extract_readonly;"
         "PWD=CW@F2q@VSw1g")


class tbl_suppliers():
    tbl_name = 'tbl_suppliers'
    engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
    with Session(engine) as sesn:
        print(sesn.execute("select * from {}".format(tbl_name)).fetchall())

st = select(__class__)
print(st)

# with engine.connect() as conn:
#
#     result = conn.execute(text("select * from {}".format(tbl_name))).fetchall()
#     print(result)
#     df = pd.read_sql_query(sql=text(tbl_name), con=engine.connect())
#     print(df)


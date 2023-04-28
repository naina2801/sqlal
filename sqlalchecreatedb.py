from sqlalchemy import create_engine, ForeignKey,Column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import urllib
import pandas as pd
from sqlalchemy import *
from sqlalchemy.sql import text
import pyodbc as db
params = urllib.parse.quote_plus("DRIVER={SQL Server};"
                                 "SERVER=SAUAZEDBS04;"
                                 "DATABASE=Extract_AMX;"
                                 "UID=extract_readonly;"
                                 "PWD=CW@F2q@VSw1g")
engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
nm ='tbl_warehouses'
class Extractamx():
    def tbl_suppliers(self):
        meta = MetaData()
        table = Table('tbl_suppliers',
                      meta,
                      autoload=True,
                      autoload_with=engine
                      )
        select_st = select([table])
        # conn = engine.connect()
        res = pd.read_sql_query(sql=(select_st), con=engine.connect())
        print(res.to_string())

class Warehouses():
    def tbl_warehouses(self):
        meta = MetaData()
        ware = Table('tbl_warehouses',
                      meta,
                      Column('warehouse_id',Integer),
                      Column('warehouse_master_id', Integer),
                      Column('warehouse_outlet', NVARCHAR),
                      Column('warehouse_state', NVARCHAR),
                      Column('warehouse_customernumber', NVARCHAR),
                      Column('warehouse_customername', NVARCHAR),
                      Column('warehouse_created_by', NVARCHAR),
                      Column('warehouse_created_on', DATETIME),
                      Column('warehouse_modified_by', NVARCHAR),
                      Column('warehouse_modified_on', DATETIME),
                      Column('warehouse_is_active', BOOLEAN),
                      Column('warehouse_is_deleted', BOOLEAN),
                      autoload=True,
                      autoload_with=engine
                      )
        s = ware.select().where(ware.c.warehouse_outlet == 'Epping')
        # s = select([text("ware.warehouse_id, ware.warehouse_outlet from ware")]).where(text("ware.c.warehouse_customernumber == 'J000107'"))
        res =pd.read_sql_query(sql=(s), con=engine.connect())
        print(res.to_string())

e = Extractamx()
# e.tbl_suppliers()
w= Warehouses()
w.tbl_warehouses()
# e.tbl_warehouses()
#

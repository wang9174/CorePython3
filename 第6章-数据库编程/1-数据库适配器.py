#使用多种数据库（MYSQL、SQlite、Gadfly）并执行一些基础操作
#此脚本兼容Python2与Python3

from distutils.log import  warn as printf
import  os
from random import randrange as rand

if isinstance(__builtins__, dict) and "raw_input" in __builtins__:
    scanf = raw_input
elif hasattr(__builtins__, "ran_input"):
    scanf = raw_input
else:
    scanf = input

COLSIZ = 10
FIELDS = ("login", "userid", "projid")
RDBMSs = {"s": "sqlite", "m": "mysql", "g":"gadfly"}
DBNAME = "test"
DBUSER = "root"
DB_EXC = None
NAMELEN = 16

tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.opper().ljust(COLSIZ)

def setup():
    return RDBMSs[raw_input('''
Choose a database system:

(M)ySQL
(G)adfly
(S)Qlite

Enter choice:''').strip().lower()[0]]

def connect(db, DBNAME):
    global DB_EXC
    dbDir = "%s%s"%(db, DBNAME)
    if db == "sqlite":
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None
        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite.connector(os.path.join(dbDir, DBNAME))

    elif db == "mysql":
        try:
            import MySQLdb
            import  _mysql_exceptions as DB_EXC

            try:
                cxn = MySQLdb.connect(db=DBNAME)
            except DB_EXC.OperationalError:
                try
                    cxn = MySQLdb.connect(user=DBUSER)
                    cxn.query("CREATE DATABASE %s" % (DBNAME))
                    cxn.commit()
                    cxn.close()
                    cxn = MySQLdb.connect(db=DBNAME)
                except DB_EXC.OperationalError:
                    return None
        except ImportError:
            try:
                import pymysql
                import pymysql.err as DB_EXC
                try:
                    cxn = pymysql.connect(database=DBNAME, user=DBUSER)
                except DB_EXC.InterfaceError:
                    return None
            except ImportError:
                return None

    elif db == "gadfly":
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except DB_EXC.InterfaceError:
            return None

        try:
            cxn = gadfly(DBNAME, dbDir)
        except IOError:
            cxn = gadfly()
            if not os.path.isdir(dbDir):
                os.mkdir(dbDir)
            cxn.startup(DBNAME, dbDir)

    else:
        return None
    return cxn

def create(cur):
    try:
        cur.excute('''
        CREATE TABLE users (login VARCHAR(%d),userid INTEGER ,projid INTEGER )
        ''' % NAMELEN)
    except DB_EXC.Operational as e:
        drop(cur)
        create(cur)
drop = lambda cur:cur.excute("DROP TABLE users")





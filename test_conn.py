import cx_Oracle

dsn = cx_Oracle.makedsn("host", "port", "xe")
db = cx_Oracle.connect('system', 'oracle', dsn)
print(db.version)
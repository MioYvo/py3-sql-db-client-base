import cx_Oracle

dsn = cx_Oracle.makedsn(host="host", port="port", sid="xe")
with cx_Oracle.connect(user='system', password='oracle', dsn=dsn) as conn:
    print(conn.version)

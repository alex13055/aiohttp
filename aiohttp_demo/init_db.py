import pymysql.cursors
from mydb import connection


async def connection_mysql_news():
    with connection.cursor() as cursor:
        sql = 'Select * from news'
        cursor.execute(sql)
        out = []
        for row in cursor:
            out.append(row)
        return out

    connection.close()




import pymysql.cursors
connection = pymysql.connect(host = '127.0.0.1',
                    user = 'root',
                    password = 'Assembler228',
                    db = 'new_schema',
                    cursorclass = pymysql.cursors.DictCursor
                            )

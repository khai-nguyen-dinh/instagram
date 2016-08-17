import MySQLdb


def insert_db(fullname,email,username,password,status):
    db = MySQLdb.connect('localhost', 'root', 'nguyendinhkhai', 'higgsvalley')
    cursor = db.cursor()
    try:
        sql = ("INSERT INTO user "
                        "(fullname, email, username, password, status) "
                        "VALUES (%s, %s, %s, %s, %s)")
        data_user = (fullname,email,username,password,status)
        cursor.execute(sql,data_user)
        db.commit()
    except Exception as e:
        print (e)
        db.rollback()
    finally:
        cursor.close()
        db.close()
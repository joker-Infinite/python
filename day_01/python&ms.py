#!/usr/bin/python

if __name__ == '__main__':
    import pymysql

    db = pymysql.connect(host="localhost", user="root", password="root", database="user")
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user ')
    data = cursor.fetchone()
    print(data)
    db.close()


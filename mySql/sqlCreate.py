#!/usr/bin/python
if __name__ == '__main__':
    import pymysql

    db = pymysql.connect(host="localhost", user="root", password="root", database="user")
    cursor = db.cursor()
    # cursor.execute('CREATE DATABASE imooc')
    cursor.execute('CREATE TABLE imooc_base (username varchar(30),age int,sex varchar(10))')

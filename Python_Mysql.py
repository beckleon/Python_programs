#coding:utf8

#####pip install codecs

import mysql.connector
import codecs
import sys
stdout = sys.stdout
stderr= sys.stderr
reload(sys)  
sys.setdefaultencoding('utf-8')
sys.stdout = stdout
sys.stderr=stderr

connMy = mysql.connector.connect(host='localhost',user='root',password='',database='test',port=3306, charset="utf8")
cur=connMy.cursor()

#############execute multi statments#####################
SQL='''
CREATE TABLE Test1 (id int(5) NOT NULL, content Blob NOT NULL, PRIMARY KEY (id));
CREATE TABLE Test2 (id int(5) NOT NULL, content Blob NOT NULL, PRIMARY KEY (id));
CREATE TABLE Test3 (id int(5) NOT NULL, content Blob NOT NULL, PRIMARY KEY (id))
'''
'''
for result in cur.execute(SQL, multi=True):
    pass

'''
############import from SQL file with chinese charactors############
file = open("createTable.sql")
text=file.read()
for result in cur.execute(text.decode('gbk').encode("utf-8"), multi=True):
    pass


connMy.commit()
cur.close()
connMy.close()

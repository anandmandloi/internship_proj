import pymysql

def connection():
	conn=pymysql.connect(host="localhost",user="root",passwd="dusty",db="projdb")
	c=conn.cursor()
	return c,conn
def connectionfile():
	conn=pymysql.connect(host="localhost",user="root",passwd="dusty",db="filetest")
	c=conn.cursor()
	return c,conn
	

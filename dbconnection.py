import mysql.connector


class DBconnection:
        def __init__(self,username,password):
            self.mydb = mysql.connector.connect(host="localhost",user=username,password=password,database="empmgmt")
        
        def getconnetion(self):
              return self.mydb
        
        def closeconnection(self):
              self.mydb.close()


# username = input("Enter username : ")
# password = input("Enter password : ")
# conn = DBconnection(username,password)
# print(conn.getconnetion())


import dbconnection
from texttable import Texttable

 
username = input("Enter username : ")
password = input("Enter password : ")
db = dbconnection.DBconnection(username,password)
conn = db.getconnetion()
cr = conn.cursor()

class EmployeeManagement():
    def addemp(self,name,email,salary,did):
        try: 
            query = f'insert into employees(name,email,salary,did) values("{name}","{email}","{salary}","{did}");'
            cr.execute(query)
            conn.commit()
            return True
        except:
            return False
        
    def viewemp(self):
        query = f'select * from employees;'
        res = cr.execute(query)
        res = list(cr.fetchall())
        res.insert(0,("Emp ID", "Name", "Mail","Salary","Date Created","Date Updated","Dep ID"))
        return (res)

    def updateemp(self,user,key,value):
        query = f'update employees set {key}="' +value+  f'" where id={user}'
        cr.execute(query)
        conn.commit()

    def deleteemp(self,id):
        query = f'delete from employees where id={id}'
        cr.execute(query)
        conn.commit()  

class Department():
    def addDep(self,dname):
        query = f'insert into department(name) values("{dname}");'
        cr.execute(query)
        conn.commit()

    def viewdep(self):
        query = f'select * from department;'
        res = cr.execute(query)
        res = list(cr.fetchall())
        res.insert(0,("Dep ID","Name","Date Created","Date Updated"))
        return (res)

    def deletedep(self,id):
        query = f'delete from department where id={id}'
        cr.execute(query)
        conn.commit() 

class Custom():
    def cusquery(self,query):
        try : 
            cr.execute(query)
            if ("select" or "view" ) in query:
                return list(cr.fetchall())
            conn.commit()
        except:
            return False

# print(db.getconnetion())


    
    



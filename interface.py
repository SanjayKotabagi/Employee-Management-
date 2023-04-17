import EmployeeM as E
from texttable import Texttable


emp = E.EmployeeManagement()
dep = E.Department()

while True:
    print("""Select any one : 
            1. Add Employee
            2. View Employee
            3. Update Employee
            4. Delete Employee
            5. Add Department
            6. Remove Department
            7. View Department
        """)
    
    opt = int(input("Enter Option : "))
    if opt == 1:
        name = input("Enter Employee Name : ")
        mail = input("Enter Employee Mail : ")
        salary = input("Enter Employee Salary : ")
        departmentid = input("Enter Employee Department ID : ")
        res = emp.addemp(name,mail,salary,departmentid)
        if res:
            print("Employee Added succefully")
        else:
            print("Error in adding employee.")

    elif opt == 2:
        print("Employees Are : ")
        employees = emp.viewemp()
        table = Texttable()
        table.add_rows(employees)
        print(table.draw())
        
    elif opt == 3:
        user = input("Enter Employee id you want to update : ")
        key = input("Enter attribute you want to update : ")
        value = input(f"Enter new valye for {key} : ")
        emp.updateemp(user,key,value)
    
    elif opt == 4:
        id = int(input("Enter ID : "))
        emp.deleteemp(id)

    elif opt == 5:
        dname = input("Enter Department Name : ")
        dep.addDep(dname)

    elif opt == 6:
        id = int(input("Enter ID of Department : "))
        dep.deletedep(id)

    elif opt == 7:
        dnames = dep.viewdep()
        table = Texttable()
        table.add_rows(dnames)
        print(table.draw())
            

from validate import *
class Employee:
    empRecords={}
    def __init__(self, employee_id, employee_name, salary, age, gender, address, city, dob, doj, department_name, designation, pan_card_number, aadhar_number,marriage,nationality,phone,email):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.salary=salary
        self.age=age
        self.gender=gender
        self.address=address
        self.city=city
        self.dob=dob
        self.doj=doj
        self.department_name=department_name
        self.designation=designation
        self.pan_card_number=pan_card_number
        self.aadhar_number=aadhar_number
        self.marriage=marriage
        self.nationality=nationality
        self.phone=phone
        self.email=email
        if self.department_name in self.empRecords.keys():
            self.empRecords[self.department_name].append(self.employee_name)
        else:
            self.empRecords[self.department_name]=[self.employee_name]
    
    def display_details(self):
        print("Employee Record Added: ")
        print("1|Employee ID: ",self.employee_id)
        print("2|Employee Name: ",self.employee_name)
        print("3|Marital Status: ",self.marriage)
        print("4|Salary: ",self.salary)
        print("5|Age: ",self.age)
        print("6|Gender: ",self.gender)
        print("7|Address: ",self.address)
        print("8|City: ",self.city)
        print("9|DOB: ",self.dob)
        print("10|DOJ: ",self.doj)
        print("11|Department Name: ",self.department_name)
        print("12|Designation: ",self.designation)
        print("13|PAN Card Number: ",self.pan_card_number)
        print("14|Aadhar Number: ",self.aadhar_number)
        print("16|Contact Number: ",self.phone)
        print("17|Email ID is: ",self.email)
        print("18|Nationality: ",self.nationality)

    @classmethod
    def departmentDetails(self):
        for k,v in self.empRecords.items():
            print(k,"=",v)
    
employee_list=[]
    
while True:
    print("Welcome to Employee Management System!")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Display Employee")
    print("3 for Searching Employee")
    print("4 for Employee Details in specific department")
    print("5 to Delete Employee Record")
    print("6 for Updating Employee Record")
    print("7 to Get Maximum Salary")
    print("8 to Exit")
    
    ch=int(input("Enter your choice: "))
    if ch==1:
        while True:
            employee_id=input("Enter Employee Id: ")
            if validate_employee_id(employee_id):
                break
            else:
                print("Enter correct employee id!")
        while True:
            employee_name=input("Enter Employee Name: ")
            if validate_name(employee_name):
                break
            else:
                print("Invalid Name. Please enter again.")
        while True:
            marriage=input("Enter marital status: ")
            if validate_marriage(marriage):
                break
            else:
                print("Incorrect entry!")
        while True:
            salary=input("Enter salary: ")
            if validate_salary(salary):
                break
            else:
                print("Wrong amount!")
        while True:
            age=input("Enter age: ")
            if validate_age(age):
                break
            else:
                print("Incorrect entry!")
        while True:
            gender=input("Enter gender: ")
            if validate_gender(gender):
                break
            else:
                print("Incorrect entry!")
        while True:
            address=input("Enter Address: ")
            if validate_address(address):
                break
            else:
                print("Incorrect entry!")
        while True:
            city=input("Enter City: ")
            if validate_city(city):
                break
            else:
                print("Incorrect entry!")
        while True:
            dob=input("Enter DOB: ")
            if validate_dob(dob):
                break
            else:
                print("Incorrect entry!")
        while True:
            doj=input("Enter DOJ: ")
            if validate_doj(doj):
                break
            else:
                print("Incorrect entry!")
        while True:
            department_name=input("Enter Department: ")
            if validate_department(department_name):
                break
            else:
                print("Incorrect entry!")
        while True:
            designation=input("Enter Designation: ")
            if validate_designation(designation):
                break
            else:
                print("Incorrect entry!")
        while True:
            pan_card_number=input("Enter PAN: ")
            if validate_pan(pan_card_number):
                break
            else:
                print("Incorrect entry!")
        while True:
            aadhar_number=input("Enter Aadhar number: ")
            if validate_aadhar(aadhar_number):
                break
            else:
                print("Incorrect entry")

        obj=Employee(employee_id, employee_name,marriage,salary,age,gender,address,city,dob,doj,department_name,designation,pan_card_number,aadhar_number)

        employee_list.append(obj)
    
    elif ch==2:
        for i in employee_list:
            i.display_details()
        
    elif ch==3:
        while True:
            print("Press A: To search the Employee by Employee ID")
            print("Press B: To search the Employee by their name")
            print("Press C: To exit the searching window.")
            ch1=input("Enter the choice: ")
            if ch1=='A':
                a=input("Enter the Employee ID: ")
                for i in employee_list:
                    if i.employee_id==a:
                        i.display_details()
            elif ch1=='B':
                a=input("Enter the name of the Employee: ")
                for i in employee_list:
                    if i.employee_name==a:
                        i.display_details()
            elif ch1=='C':
                break
    elif ch==4:
        Employee.departmentDetails()
    elif ch==5:
        while True:
            print("Press A: To delete record by Employee ID")
            print("Press B: To delete record by Employee Name")
            print("Press C: To exit")
            ch2=input("Enter the choice: ")
            if ch2=='A':
                a=input("Enter the Employee ID: ")
                for i in employee_list:
                    if i.employee_id==a:
                        employee_list.remove(i)
                        print("Deletion Performed!")
            elif ch2=='B':
                a=input("Enter the name of the Employee: ")
                for i in employee_list:
                    if i.employee_name==a:
                        employee_list.remove(i)
                        print("Deletion Performed!")
            elif ch2=='C':
                break
    elif ch==6:
        while True:
            print("Choose the detail to be updated: ")
            print("Press 1: Update name")
            print("Press 2: Update address")
            print("Press 3: Update DOB")
            print("Press 4: Update salary: ")
            print("Press i: Update salary of employee by employee id")
            print("Press ii: Update salary of all employees from specific department")
            print("Press iii: Update salary of all employees")
            print("Press 5: Exit")

            ch3=input("Enter your choice: ")
            if ch3=='1':
                employee_id=input("Enter Employee ID to update name: ")
                new_name=input("Enter new name: ")

                for i in employee_list:
                    if i.employee_id==employee_id:
                        i.employee_name=new_name
                        print("Name has been Updated!!")
            elif ch3=='2':
                employee_id=input("Enter Employee ID to update address: ")
                new_address=input("Enter new address: ")

                for i in employee_list:
                    if i.employee_id==employee_id:
                        i.address=new_address
                        print("Address has been Updated!!")
            elif ch3=='3':
                employee_id=input("Enter Employee ID to update DOB: ")
                new_dob=input("Enter new dob: ")

                for i in employee_list:
                    if i.employee_id==employee_id:
                        i.dob=dob
                        print("DOB has been Updated!!")
            elif ch3=='4':
                employee_id=input("Enter Employee ID to update salary: ")
                new_salary=input("Enter new salary: ")

                for i in employee_list:
                    if i.employee_id==employee_id:
                        i.salary=new_salary
                        print("Salary has been Updated!!")
            elif ch3=='i':
                employee_id=input("Enter Employee ID to update salary of specific employee: ")
                new_salary=float(input("Enter new salary: "))

                for i in employee_list:
                    if i.employee_id==employee_id:
                        i.salary=new_salary
                        print("Salary has been Updated!!")
            elif ch3=='ii':
                department_name=input("Enter department name to update salary: ")
                new_salary=int(input("Enter new salary: "))

                for i in employee_list:
                    if i.department_name==department_name:
                        i.salary=new_salary
                        print("Salary has been Updated!!")
            elif ch3=='iii':
                new_salary=int(input("Enter amount to be updated: "))

                for i in employee_list:
                    i.salary==new_salary
                    print("Salary has been Updated!!")
            elif ch3=='5':
                break
                    
    elif ch==7:
        salary_list=[]
        for i in employee_list:
            salary_list.append(i.salary)

            if len(salary_list)==0:
                print("!! Employee list is empty !!")
                print(" ")
            else:
                max_salary=max(salary_list)
                print("Employee with maximum salary: ")
                for i in employee_list:
                    if i.salary==max_salary:
                        i.display_details()

    elif ch==8:
        print("Exit the Employee Management System")
        break
    else:
        print("Invalid Choice")        
                

    
    

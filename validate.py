def validate_employee_id(employee_id):
    if not employee_id.isdigit():
        return False
    return True

def validate_name(employee_name):
    l=employee_name.split(" ")
    if len(l) >3 or len(l)<1:
        return False
    elif "".join(l).isalpha()==False:
        return False
    else:
        for i in l:
            if i.istitle()==False:
                return False
    return True

def validate_marriage(marriage):
    status=["married","single","divorced"]
    if marriage.lower() in status:
        return True
    else:
        print("Invalid entry!!")
    return
 
def validate_salary(salary):
    salary=float(salary)
    if salary<0:
        return False 
    else:
        return True

def validate_age(age):
    age=int(age)
    if age<18 or age > 100:
        return False 
    else: 
        return True
 
def validate_gender(gender):
    accepted_genders = ["female" , "male", "non-binary"]
    if gender.lower() in accepted_genders:
        return True 
    else:
        print("Validation Error: invalid gender, please choose from (male, female, non-binary)")
    return

def validate_address(address):
    if not address.isalnum():
        return False
    return True

def validate_pan(pan_card_number):
    if len(pan_card_number)!=10:
        return False
    for char in pan_card_number[:5]:
        if not char.isalpha() or not char.isupper():
            return False
    for char in pan_card_number[5:9]:
        if not char.isdigit():
            return False
    if not pan_card_number[9].isalpha() or not pan_card_number.isupper():
            return False
    return True

def validate_aadhar(aadhar_number):
    if len(aadhar_number)!=12:
        return False
    if not aadhar_number.isdigit():
            return False
    return True

def validate_department(department_name):
    valid_department=['SALES','TRANSPORT','IT','FINANCE','CYBER']
    if department_name.upper() in valid_department:
        return True
    else:
        print("Invalid Designation!!")
    return

def validate_designation(designation):
    valid_designation=['HR','MANAGER','DEVELOPER','DRIVER','FINANCER']
    if designation.upper() in valid_designation:
        return True
    else:
        print("Invalid Designation!!")
    return

def validate_city(city):
    valid_city= ['PUNE', 'GURGAON', 'BANGALORE']
    if city.upper() in valid_city:
        return True
    else:
        print("Validation Error: Please enter a valid city.")

def validate_dob(dob):
    l=dob.split("/")
    dd=int(l[0])
    mm=int(l[1])
    yy=int(l[2])

    if mm ==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12 :
        max_days =31
    elif mm==4 or mm==6 or mm==9 or mm==11 :
        max_days = 30
    elif yy%4 ==0 and yy%100!=0 or yy %400==0:
        max_days=28
    else:
        max_days=29

    if mm<1 or mm>12:
        return False
        print("Validation Error: Enter a valid month ")

    elif dd<1 or dd>max_days:
        return False
        print("validation error : Please enter a valid date ")
    else :
        return True

def validate_doj(doj):
    return validate_dob(doj)
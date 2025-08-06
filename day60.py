<<<<<<< HEAD
# Day: 60(Getters and Setters)

# Getters and setters are methods basically used to get and set attribute values of a object, surely
#  we are able to get that the usual way too but setter and getter are a good approach and supports encapsulation
#   too. We can add validations through it and a bunch of other stuff too.

# Each attribute does need a separate getter and setter for it.

class Student:    
    def __init__(self,name,age,roll_no):
        self._name=name
        self._age=age
        self._roll_no=roll_no

    @property
    def name(self):         #Getter for name
        return self._name
    @name.setter
    def name(self,value):     #Setter for name
        if not value:            
            print("Name can't be empty")
        else:
            self._name=value

    @property    
    def age(self):              #Getter for age
        return self._age
            
    @age.setter
    def age(self,value):          #Setter for age
        if value<0 or value>120:
            print("Age can't be negative or above 120")
        else:
            self._age=value
    @property                    #Getter for roll_no
    def roll_no(self):
        return self._roll_no
        

student_1=Student("Abdullah",20,"Laiba ka roll no hehe")

print(student_1.name)
print(student_1.age)
print(student_1.roll_no)

student_1.name="Ali"
student_1.age=81
student_1.roll_no="Nice one"
print(student_1.name)
print(student_1.age)
print(student_1.roll_no)

'''
🧠 Exercise: "Build a Smart Employee Class"
Create a class called Employee with the following:

Attributes (all private using _):
_name: the employee's name

_salary: their monthly salary

_email: email address (should be auto-generated)

_company: fixed company name, like "OpenAI" (read-only)

✅ Requirements:
name:

Must be a non-empty string.

Use @property and @name.setter.

salary:

Must be a number greater than 0.

Use @property and @salary.setter.

email:

Should auto-generate based on the name, e.g.:

css
Copy
Edit
john.doe@openai.com
(Assume lowercase and replace spaces with dots)

Make it a read-only property.

company:

Should always return "OpenAI".

Make it read-only (no setter).

'''

            
class Employee:
    def __init__(self,name,salary):
       self._name=name
       self._salary=salary
       self._company="openai"
       
    @property
    def name(self): return self._name       #Getter for name
    @name.setter
    def name(self,name):                    #Setter for name
        if not name:
             print("Name cannot be empty")
        else:
            self._name=name
            
    @property                               #Getter for salary
    def salary(self): return self._salary        
    
    @salary.setter                          #Setter for salary
    def salary(self,salary):
        if salary<0:
            print("Salary should be greater than 0")
        else:
            self._salary=salary
    
    @property
    def company(self): return self._company     #Getter (only for company)        
    
    @property                               #Getter (only) for email
    def email(self):
        corrected_email=self._name.strip().lower().replace(" ",".")
        return (f"{corrected_email}@{self._company}.com")
    
e = Employee("John Doe", 6000)

print(e.name)           # John Doe
print(e.salary)         # 6000
print(e.company)        # openai
print(e.email)          # john.doe@openai.com

e.name = ""             # Name cannot be empty
e.salary = -500         # Salary should be greater than 0
=======
# Day: 60(Getters and Setters)

# Getters and setters are methods basically used to get and set attribute values of a object, surely
#  we are able to get that the usual way too but setter and getter are a good approach and supports encapsulation
#   too. We can add validations through it and a bunch of other stuff too.

# Each attribute does need a separate getter and setter for it.

class Student:    
    def __init__(self,name,age,roll_no):
        self._name=name
        self._age=age
        self._roll_no=roll_no

    @property
    def name(self):         #Getter for name
        return self._name
    @name.setter
    def name(self,value):     #Setter for name
        if not value:            
            print("Name can't be empty")
        else:
            self._name=value

    @property    
    def age(self):              #Getter for age
        return self._age
            
    @age.setter
    def age(self,value):          #Setter for age
        if value<0 or value>120:
            print("Age can't be negative or above 120")
        else:
            self._age=value
    @property                    #Getter for roll_no
    def roll_no(self):
        return self._roll_no
        

student_1=Student("Abdullah",20,"Laiba ka roll no hehe")

print(student_1.name)
print(student_1.age)
print(student_1.roll_no)

student_1.name="Ali"
student_1.age=81
student_1.roll_no="Nice one"
print(student_1.name)
print(student_1.age)
print(student_1.roll_no)

'''
🧠 Exercise: "Build a Smart Employee Class"
Create a class called Employee with the following:

Attributes (all private using _):
_name: the employee's name

_salary: their monthly salary

_email: email address (should be auto-generated)

_company: fixed company name, like "OpenAI" (read-only)

✅ Requirements:
name:

Must be a non-empty string.

Use @property and @name.setter.

salary:

Must be a number greater than 0.

Use @property and @salary.setter.

email:

Should auto-generate based on the name, e.g.:

css
Copy
Edit
john.doe@openai.com
(Assume lowercase and replace spaces with dots)

Make it a read-only property.

company:

Should always return "OpenAI".

Make it read-only (no setter).

'''

            
class Employee:
    def __init__(self,name,salary):
       self._name=name
       self._salary=salary
       self._company="openai"
       
    @property
    def name(self): return self._name       #Getter for name
    @name.setter
    def name(self,name):                    #Setter for name
        if not name:
             print("Name cannot be empty")
        else:
            self._name=name
            
    @property                               #Getter for salary
    def salary(self): return self._salary        
    
    @salary.setter                          #Setter for salary
    def salary(self,salary):
        if salary<0:
            print("Salary should be greater than 0")
        else:
            self._salary=salary
    
    @property
    def company(self): return self._company     #Getter (only for company)        
    
    @property                               #Getter (only) for email
    def email(self):
        corrected_email=self._name.strip().lower().replace(" ",".")
        return (f"{corrected_email}@{self._company}.com")
    
e = Employee("John Doe", 6000)

print(e.name)           # John Doe
print(e.salary)         # 6000
print(e.company)        # openai
print(e.email)          # john.doe@openai.com

e.name = ""             # Name cannot be empty
e.salary = -500         # Salary should be greater than 0
>>>>>>> e23d7bf6f4021c6deb0956d47a6cd73c70ecaa2a

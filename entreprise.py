class Person:
    def __init__(self, firstName, familyName):
        self.firstName = firstName
        self.familyName = familyName

    def info(self):
        return f"Name: {self.firstName} {self.familyName}"
    

class Company:
    MainType = "company"
    CEO= 'Vadim'

    def __init__(self, name, location, field):
        self.name = name
        self.location = location
        self.field = field
        self.Employees = []
        
    
    def getName(self):
        return self.name
    

    
    def getLocation(self):
        return self.location
    
    def getField(self):
        return self.field
    
    def getEmployees(self):
        return self.Employees
    
    def addEmployee(self, Employee):
        if Employee not in self.Employees:
            self.Employees.append(Employee)
        
        else:
            print("They already work here")


class Employee(Person):
    def __init__(self, fname, lname, company, salary):
        Person.__init__(self, fname, lname)
        self.company = company
        self.salary = salary
        company.addEmployee(Person)

    def info(self):
        return Person.info(self)+", "+str(self.company.getName())+", "+str(self.salary)
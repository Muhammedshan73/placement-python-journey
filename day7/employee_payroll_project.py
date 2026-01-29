class Employee:
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name,monthly_salary):
        super().__init__(emp_id, name)
        self._monthly_salary = monthly_salary
        #encapusulation becuase salary is protected
    def calculate_salary(self):
        return self._monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name,hours_worked,rate_per_hour):
        super().__init__(emp_id, name)
        self._hours_worked = hours_worked
        self._rate_per_hour = rate_per_hour
    def calculate_salary(self):
        return self._hours_worked*self._rate_per_hour
    
class PayrollApp:
    def __init(self):
        self.employee = None
    def create_employee(self,emp_type):
        if  emp_type == "FullTime":
            self.employee = FullTimeEmployee(1,"shan",5000)
        else:
            self.employee = PartTimeEmployee(2,"aroo",80,500)
        return "Employee created"
    def get_salary(self):
        self.employee

    

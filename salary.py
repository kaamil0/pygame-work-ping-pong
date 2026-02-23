class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_info(self):
        print("Employee Information")
        print(f"Name     : {self.name}")
        print(f"Position : {self.position}")
        print(f"Salary   : ${self.salary:.2f}")



emp1 = Employee("Kaamil Tairu", "Engineer", 75000)
emp1.display_info()
emp1.give_raise(5000)
emp1.display_info()

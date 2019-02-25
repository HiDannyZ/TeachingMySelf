class Employee:
    def __init__(self, firstName = None, lastName = None,pay = None):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = "ch" + firstName + lastName + "@yahoo.com"

if __name__ == '__main__':
    print("hi")
    Andy = Employee()
    Danny = Employee()
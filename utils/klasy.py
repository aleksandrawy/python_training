class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__private_field = "some private value"

    def get_salary_after_tax(self):
        return self.salary * 0.71 #  this needs self to access instance members

    @staticmethod
    def this_does_not_have_self(a, b):  # this method belongs to the class, but do not have access to instance or class fields
        print(a + b)


    @classmethod
    def this_method_gets_the_class_and_not_the_instance(cls):
        print("This is a classmethod of class {}".format(cls))
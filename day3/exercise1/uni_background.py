class Person(object):
    def __init__(self, first_name, last_name):
        self.full_name = first_name + ' ' + last_name
    
    @property
    def printName(self):
        print(self.full_name)

    
    def get_name(self):
        return self.full_name

class Student(Person):
    def __init__(self, name, surname, subject):
        super(Student, self).__init__(name, surname)
        self.__subject = subject
        self.__full_name = Person.get_name(self)

    @property
    def printNameSubject(self):
        print(self.__full_name +', '+self.__subject)


class Person():
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def walk(self):
        print('Walking')

# Inheritance starts here
class Member(Person):
    def __init__(self, name, email, mem_id):
        super().__init__(name, email)
        self.mem_id = mem_id

member = Member('Ali' , 'ali@gmail.com' , 'mem-001')
print(member.mem_id)
print(member.walk())

class Librarian(Person):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary
                
libraian = Librarian('Smith' , 'smith@gmail.com', 2393)
print(libraian.email)
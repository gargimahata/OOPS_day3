class ineuron:
    def __init__(self):
        self.students1 = 100

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "data analytics"
i.students()

class ineuron1:
    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)

    def students_change(self,new_value):                  #setter method- useful to set a new value.
        self.__students1 = new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "bid data"
i1.students()
i1.students_change("sudhanshu")
i1.students()

#encapsulation- Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
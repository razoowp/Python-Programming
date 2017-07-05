<<<<<<< HEAD
#This creates class person
=======
#class person
>>>>>>> 52da50923ac90c4ab9be99ef18734f4916d8e291
class Person:
    def setFullName(self, firstName, lastName):
        self.firstName = firstName;
        self.lastName = lastName;
    def printFullName(self):
        print("My Full Name is: ", self.firstName, " ", self.lastName)

#creating object of class person
personName = Person()
personName.setFullName("raju","thapa")
personName.printFullName()

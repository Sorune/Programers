
class Dog:

	def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return "이름 : "+self.name +"나이: "+ str(self.age)

        def bark(self):
            print("bow wow")
        
        def birthyear(self, year):
            return print(year- self.age)

my_dog = Dog("똥개", 17)
my_dog.bark()
my_dog2 = Dog("시고르자브종", 18)
my_dog2.bark()
print(my_dog)
print(my_dog2)
my_dog3 = Dog("몰라",1)

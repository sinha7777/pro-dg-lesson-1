#opps - object Oriented programing structure
# the term class is the blueprint of an object (properties,functions)
#objects are nothing but a instance of a class

class Students():
    def __init__(self,name,age,fav_color,hobby,grade):
        self.name = name
        self.age = age
        self.fav_color = fav_color
        self.hobby = hobby
        self.grade = grade
        self.intro = ""

    def showdetails(self):
        print("The details of the students are:") 
        print("Name :",self.name)
        print("Age :",self.age)
        print("Fav_color",self.fav_color)
        print("Hobby",self.hobby)
        print("Grade :",self.grade)

    def intro_student(self):
        self.intro = input("Please intoduce yourself")
        print(self.intro)

#object
s1=Students("Viraat",12,"blue","coding",7)
s1.showdetails()
s1.intro_student()

s2=Students("Mihir",12,"green","football",7)
s2.showdetails()
s2.intro_student()

s3=Students("Kashif",12,"orange","swimmng",7)
s3.showdetails()
s3.intro_student()
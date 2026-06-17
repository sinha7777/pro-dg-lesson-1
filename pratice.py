class Headphones():
    def __init__(self,size,weight,color):
        self.size = size
        self.weight = weight
        self.color = color

    def Show_details(self):
        print("The properties of the headphone's are:")
        print("Size :",self.size)
        print("Weight :",self.weight)
        print("Color :",self.color)

s1=Headphones(15,750,"black")
s1.Show_details()
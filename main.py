#create a class
class students:
    platform = "Vedanshi"
    course = "python"
    def __init__(self,country,name,favcolor):
        self.country = country
        self.name = name
        self.favcolor = favcolor

#object
stu1 = students("Bangaladesh", "tasheen", "white")
stu2 = students("portugal", "Vedanshi", "green")
stu3 = students("Africa", "chiamalite", "blue")


print("my students names are: 1.{} 2.{} 3.{}".format(stu1.name,stu2.name,stu3.name))
# %%
class Point:
    def draw(self, param):
        print(param)


point = Point()
point.draw("Hi from class")
# checj if point is instance og the Point
isinstance(point, Point)
# %%
# class with constructors


class Point2:
    # this is like static field in c#, this var is same in all instance of this class
    defaultColor = "red"
    #Class method is similar as static method in c#
    # cls is only convention
    @classmethod
    def zeroPoint(cls):
        return cls(0, 0)  # or Point2(0,0)

    def __init__(self, x, y):
        # instance attributes
        self.x = x
        self.y = y

    def draw(self):
        print(self.x, self.y)
        print(self.defaultColor)


point2 = Point2(10, 16)
# dynamic object, i can add new properties, same as javascript
point2.z = 100
point2.draw()
print(point2.x)
print(Point2.defaultColor)
print(point2.defaultColor)
zeroP = Point2.zeroPoint()
print(zeroP.x, zeroP.y)


# %%
# example of magic method in python
# overide __str__ method

class People:
    def __init__(self, firstname, lastname):
        self.Firstname = firstname
        self.LastName = lastname

    def __str__(self):
        return f"{self.Firstname} - {self.LastName}"

    def printObject(self, object: People):
        print(object.Firstname, object.LastName)

    def draw(self):
        """
        Draw fullname to console
        """
        print(self.Firstname, self.LastName)

    def __eq__(self, other) -> bool:
        """
        compare two object example
        """
        return self.Firstname == other.Firstname and self.LastName == other.LastName


myPerson = People("Miroslav", "Polednak")
myPerson2 = People("Pavel", "Novák")
myPerson.draw()
myPerson.printObject(myPerson2)
print(myPerson)
print(myPerson == myPerson2)


# %%
# example of implementation python container (custom dictionary)
class DcContainer:
    def __init__(self):
        self.__tags = {}

    def Add(self, tag: str):
        # __ is for private property
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        """
        This is example of dictionary indexer
        """
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, key: str, value: int):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        """
        This method alove iteration over tags
        """
        return iter(self.__tags)


con = DcContainer()
con.Add("java")
con.Add("java")
con.Add("java")
con.Add("C#")
con.Add("Python")
con.Add("Python")
print(con.__tags)
# print(con.Tags)
# con["Python"] = 20
# print(con["Python"])
# print(len(con))
for value in con:
    print(value)


# %%

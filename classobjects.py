#__init__function

class details:
    def __init__(self, name, age):
        self.name=name
        self.age=age
p1=details("arun",24)
print(p1.name)
p1.age=44
print(p1.age)


#__init__function and Object Method

class person:
     def __init__(self,name,age) -> None:
         self.name=name
         self.age=age
     def hello(sel):
         print("your name is "+sel.name)
p1=person("Arun",24)
p1.hello()


#__str__()Function

class NameAge:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p2=NameAge("Arun",24)
print(p2)
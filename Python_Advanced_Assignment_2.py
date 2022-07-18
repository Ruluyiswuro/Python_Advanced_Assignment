"""
PYTHON ADVANCED ASSIGNMENT 2

Q1. WHat is the relationship between classes and modules?

Ans : A Python class is like an outline/blueprint for creating a new object. An object is anything that we wish to
manipulate or change while working through the code. Every time a class object is instantiated, which is when we declare
a new variable, a new object is initiated from scratch.

Modules are that files that have .py extension containing Python code that can be imported inside another Python
Program. In simple terms, we can consider a module to be same as the code library or a file that contains a set of
functions / classes that we want to include in your application.
"""

"""
Q2. How do you make instances and classes?

Ans : To create a class instance, we call a class by it's name and pass the arguments which it's __init__ method accepts.
Example: 
student = ineuron('FSDS', '2022') where student is an instance of class ineuron with attributes FSDS and 2022.

Whereas, for creating a class, we use the Class keyword which is followed by class name and semicolon.
Example:
Class ineuron:
    def __init__(self, batch, year):
        self.batch = batch
        self.year = year
"""

"""
Q3. Where and how should be class attributes created?
Ans : Class attributes belongs to the class itself, these attributes will be shared by all the instances of the class. 
Hence, theses attributes are usually created/defined in the top of class definition outside all methods.

Example :
Class student:
    batch_year = 2022
    def __init__(self, background, qualification):
        self.background= background
        self.qualification = qualification
Here, batch_year is shared by all the instances of the class student.
"""

"""
Q4. Where and how instance attributes created?
Ans : Instance attributes are passed to the class when an object of the class is created. Unlike class attributes,
instance attributes are not shared by all objects of the class. Instead, each object maintain its own copy of instance
attributes at object level. Instance attributes are usually defined within the __init__ method of class.
Example :
Class ineuron:
    def __init__(self, batch, year,course_name):
        self.batch = batch
        self.year = year
        self.course_name = course_name
ruluyi = ineuron('FSDS 2020', 2022, 'Full Stack Data Science')
Here, ruluyi is the instance of class ineuron with different variables.
"""

""""
Q5. What does the term "self" in a Python class mean?
Ans : The term self represents the instance pf the class(it represents the object itself). By using the "self" keyword
we can access the attributes and methods of the class within the class in python. It binds the attributes with the 
given arguments
"""

"""
Q6. How does a Python class handle operator overloading?

Ans : Python classes handle operator overloading by using a; special methods called Magic methods. These special methods
usually begin and end with __(double underscore).
Examples :
+ -> __add__()
- -> __sub__(), etc
"""
class student:
    def __init__(self, FSDS_2022):
        self.FSDS_2022= FSDS_2022
    def __add__(self,other):
        return self.FSDS_2022 + other.FSDS_2022
i2022 = student(500)
i2021 = student(400)
print(f'Total student in 2 years is : {i2022+i2021}')
#Total student in 2 years is : 900

"""
Q7. When do you consider allowing operator overloading of your classes?

Ans : We consider allowing operator overloading when we want to have different meaning for the sane operator.
For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable 
because ‘+’ operator is overloaded by int class and str class.
"""

"""
Q8. What is the most popular form of operator overloading?

Ans : The most popular form of operator overloading in Python is the special method called Magic methods. It usually 
begin and end with __(double underscore). E.g. __<method name>__.
"""

"""
Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Ans : Classes and objects are the two most important concepts to grasp in order to comprehend Python OOP code as more 
formally objects are entities that represents instances of general abstract concept called class.
Along with classes and objects the other important concepts to grasp are:

1. Inheritance
2.Abstraction
3.Polymorphism
4.Encapsulation
"""
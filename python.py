Python @codecademy

Link > https://www.codecademy.com/enrolled/courses/python-for-programmers

Getting Started 

Python - programming language 

Applications
* Software development (e.g. Developing a website with the Flask library)
* Data science (e.g. Creating a machine learning model with Tensorflow)
* Automation (e.g. Creating a script to automate data analysis using Excel)


Naming conventions
- for functions and classes

Indentation

Comments

IDEs

Basic Syntax

Program Structure - 

Hello world

ubuntu (python3 installed) > sublime py file > run in termial using python3 command and file name
SS -> https://docs.google.com/document/d/1t-aNz_xikW_tOGfEHH-B7uLsuar-xC0YSB15sDUEPTE/edit?usp=sharing

main () fuction
>  In Python, we frequently use the main() function to define the starting point of our program.
> Including the main() function allows us to import and run this program in another script.

Input and output - 

> Python has a built-in function called input() that takes in the user’s input
> You can store user input as a variable to use later.

> To display output, you can use Python’s built-in function print()

> You could also use formatted string literals by starting the print argument with f and inserting a Python expression between { and }.

or also {}.format(str) , 

print(f'my name is {name}')
print('my age is {}'.format(age))

Variables - 

declaring a variable 

Casting - changing to specific type of the variable using built-in data types in Python. Str(), int(), float()

Printing the Data Type - type()

Data Types in python - 

1. Integer - ints store integer values. We can specify that the variable is a integer by using a whole number or we can use int() to cast numerical variables as an integer
2. Float - floats store numerical values with decimal points. float() is the built-in function that stores numerical values with their decimal points.
3. Boolean - boolean variables hold two values, True or False. We can use the words True or False to assign it to our variable or use bool().
      The bool() function will always return True unless the variable is empty, 0, None or False.
4. String - string variables hold characters and can be created by using single quotes ’ or double quotes ”. You can also use the built-in function str() to specify that you are storing a string.

Operators - 

1. Arithmetic Operators
Operator    Name of Operation   Example Description
+   Addition    x + y   x plus y
-   Subtraction x - y   x minus y
*   Multiplication  x * y   x multiplied by y
**  Exponentiation  x ** y  x raised to the power of y
/   Division    x / y   x divided by y
//  Floor Division  x // y  x divided by y, returning integer
%   Modulo  x % y   The remainder of x divided by y

2. Assignment Operators
Operator    Example Description
=   x = 4   Assign 4 to x
+=  x += 4  Add 4 to existing value of x
-=  x -= 4  Subtract 4 from existing value of x
*=  x *= 4  Multiply existing value by 4
/=  x /= 4  Divide existing value by 4
%=  x %= 4  Modulo existing value by 4

3. Comparison Operators

Returns true or false
Operator    Description Example
==  Equal to    x == y
!=  Not equal to    x != y
>   Greater than    x > y
<   Less than   x < y
>=  Greater than or equal to    x >= y
<=  Less than or equal to   x <= y

4. Logical Operators

and , or , not

Returns True or false
Operator    Description Example
and If both statements are true, returns True   x > 2 and y > 1
or  If one of the statements are true, returns True x > 3 or y > 5
not If used, returns the reverse of the actual result   not(x > 10 and y > 5)

Control Flow

if , else, elif 

conditional statements, which are used to execute a sequence of code based on the given boolean values.

If statement >

An if statement evaluates whether the given expression is evaluated as True. If the condition evaluates to be True, the code is executed. If the condition evaluates to be False, the code does not execute.

else Statements >

else statement after an if statement allows for another set of code to be ran if the if statement evaluates the expression to be False

elif Statements >

An elif statement, which is short for else if

can be added between an if statement and an else statement to evaluate for another condition. The code under the elif statement will only execute if the preceding if statement evaluates to be False.

score = 70
 
if score >= 80:
   print('You pass the course with flying colors!')
 
elif score > 65:
   print('You pass the course! Talk to your instructor.')
  
else:
   print('You do not pass the course!')



Loops 

A loop is used to execute code repeatedly

For and While loops >

for loops >

for loop is used to iterate over items and execute code on each item. It has two keywords, for and in, which are used to describe the element and the object that is being iterated over

nums = [1, 2, 3, 4, 5]
 
for num in nums:
  print(num + 1)


for loops with range()

The range() function can be used with the for loop to execute a block of code multiple times. The code below iterates between numbers 0 to 2 and prints each number

for i in range(3):
  print(i)

output > 0,1,2

Nested for loops

Loop inside a loop

teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
  for name in team:
    print(name)


output >

Jody
Abe
Abhishek
Kim
Taylor
Jen


while loops >

while loop is used to execute code while its condition evaluates to be True.

In the example below, the while loop will run and print i as long as the value of i is less than 6.

i = 1
while i < 6:
  print(i)
  i += 1

note -> while , Infinite loops
never terminates because the condition is always evaluated to be True.


Pass, Break, Continue

Keywords -> pass, break and continue which are used to control or disrupt loops.


Pass > Nothing gets executed when pass is placed under a condition.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
   if 'j' in name.lower():
       pass
   else:
       print(name)

output > 
Hannah
Manny
Ezekiel

Break > The break keyword terminates a loop
If a certain condition is met, the loop stops iterating and breaks at that point.

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
  if 'h' in name.lower():
      break
  else:
      print(name)


Output > 
Joyce

Continue >

The continue keyword skips over an iteration if the condition is met and goes onto the next iteration

names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
for name in names:
   if 'j' in name.lower():
       continue
   else:
       print(name)

Output >

Hannah
Manny
Ezekiel

Pass and continue
The difference between the continue keyword and pass is that continue goes onto the next iteration while pass simply does not do anything.


Error Handling >

try, except and finally which are used for error handling

try and except

The clause “try” attempts to execute a block of code and “except” executes another block of code if -> try fails.


nums = [0, 1, 2, 3]
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')


nums = ['x', 'y', 'z']
 
try:
   print(sum(nums))
 
except:
   print('Cannot print the sum! Your variables are not numbers.')

The try clause above will fail because the list nums has strings, which cannot be added together with sum(). Instead, the code under except will be executed:

Output 
> Cannot print the sum! Your variables are not numbers.

finally

The finally clause executes a block of code regardless of which clause, try or except, was executed. 

 The finally clause is useful in cases where both of your try and except might fail.

nums = ['x', 'y', 'z']
 
try:
   print(sum(nums))
 
except:
   print(sum(nums))
 
finally:
   print('Hope you got the result you want!')
 Function Basics

A function in Python contains code that is executed when it is called
Functions make code reusable and repeatable

Creating a Function -> def is the built-in keyword in Python that is used to declare functions.

def add_three(num1, num2, num3):
   sum_three = num1 + num2 + num3
   return sum_three

Using a Function -> Functions can be used by calling the function name with parenthese

add_three(2, 4, 6)

Parameters > 
Parameters are treated as local variables within the body of the function.

def greetings(language):
   if language == 'Spanish':
       greeting = 'Hola'
 
   elif language == 'English':
       greeting = 'Hello'
 
   elif language == 'French':
       greeting = 'Bonjour'
 
   print(greeting)


 The function below has the parameter language.


Arguments>

Arguments are values that can be passed into the function and used as parameters

We can call the above function with the argument French like this:

greetings('French')

Output > 'Bonjour'


def greetings(language):  <——— Parameter : language 
   if language == 'Spanish':
       greeting = 'Hola'
 
   elif language == 'English':
       greeting = 'Hello'
 
   elif language == 'French':
       greeting = 'Bonjour'
 
   print(greeting)

greetings('French') <——— Argument : French


Recursion

Process of repeatedly calling a function within itself

def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)


The above function factorial is a recursive function because it calls itself within the function. A recursive function contains two parts: recursive step and base case.

Recursive Step
The line of code under the else statement is the recursive step, because it calls the function factorial().

Base Case
In the above function, the recursion stops when num == 1. This case is called the base case, which should be defined in every recursive function. Having a base case helps to avoid infinite recursions. 

Lambda Functions
anonymous function that is defined without a name

lambda argument(s): expression

add_two = lambda x: x + 2

add_two(5)

Why ? 
1. When we want to write a quick function with one line
2. map(), filter(), and apply() to filter for data


Map >

Applies given function to each item of a given iterable (list, tuple, etc.) and returns map object(which is an iterator) of the results 

Syntax: map(fun, iter)

numbers = [5, 6, 7, 8]

def double(n):
    return n * 2

# Using map to double all numbers
result = map(double, numbers)

Output > [10, 12, 14, 16]


Filter >

filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

Syntax: filter(function, sequence)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Define a function to check if a number is even
def is_even(n):
    return n % 2 == 0

# Use filter to filter out even numbers
even_numbers = filter(is_even, numbers)

Output > [2, 4, 6, 8, 10]


Reduce >

applies a given function to the elements of an iterable, reducing them to a single value.

Syntax: reduce(func, iterable[, initial])


from functools import reduce 

# Define a list of numbers
numbers = [1, 2, 3, 4]

def add(a, b):  
    return a + b 

# use reduce function to sum numbers in numbers list
sum = reduce(add, num_list)  


With Lambda

from functools import reduce

items = [1,2,3,4,5]

sum_all = reduce(lambda x,y : x + y, items)


Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that allows for the organization of code with data states and functionalities.
Code with OOP is modular, abstract, and easy to maintain

Classes and Objects

backbones of OOP

Classes

A class is a data type that encapsulates information and functions as a blueprint for objects

class Dog:
   # this is a blank class
   pass

Objects

An object is an instance of a class, which means the object contains everything from the class that it’s instantiated from

pepper = Dog()
print(pepper)

constructors and destructors

Constructors are functions that are called when an object of a class is created and destructors are called when object is deleted.

Constructors

Constructors are special functions that are executed when an object is instantiated
In Python, the __init__() function is used as the constructor and is called when creating an object.

init()

It is common practice for classes to contain Python’s built-in __init__() method as the constructor

 __init__() method would be called every time the ClassSchedule class is instantiated, and used to initialize a newly created object:

class ClassSchedule:
   def __init__(self, course):
       self.course = course


Instance Variables

The self parameter in the __init__() method refers to the current instance and the instance variable course allows for input to assign a value

We can create a class instance by calling the class and inputting the value for course

first = ClassSchedule('Chemistry')
print(first.course)

another example

class Dog:
    def __init__(self , name):
        self.name = name


d1 = Dog('tommy')

print(d1.name)


Output > tommy

Destructors

Destructors are special functions THAT ARE CALLED WHEN OBJECTS GET DELETED
Python, the __del__() method is commonly used as the destructor and is called when an object is deleted.

del()

Python’s built-in __del__() method represents the destructor in a class

In the example below, the __del__() method would be called every time an object initiated from the ClassSchedule class is deleted.

class ClassSchedule:
   def __init__(self, course):
       self.course = course
  
   def __del__(self):
       print('You successfully deleted your schedule')


The self parameter in the __del__() method refers to the current object.

sched = ClassSchedule('Chemistry')
del sched

Output > You successfully deleted your schedule

Eg - 

# Create Class Computer  
class Computer:  
    
    #  Initialize the class  
    def __init__(self):  
        print('Class Computer is created.')  
    
    # Call the destructor  
    def __del__(self):  
        print('The destructor is called.')  
    
def Create_obj():  
    print('The object is created.')  
    object = Computer()  
    print('Function ends here.')  
    return object  
    
print('Call the Create_obj() function.')  
object = Create_obj()  
print('The Program ends here.') 

Output > 

Call the Create_obj() function.
The object is created.
Class Computer is created.
Function ends here.
The Program ends here.
The destructor is called.

# The destructor is invoked when the program is finished or when all references to the object are erased, not when the object is removed from scope

In Python, we use a destructor to handle all of these cleaning chores


Access Modifications

Access modifiers are used to control or restrict access to members, also known as variables and methods, within a class.

These modifiers play an important role in limiting access to secure the members within the class

three access modifiers within Python:
*       Public Access Modifiers
*       Protected Access Modifiers
*       Private Access Modifiers


Public Access Modifier

> By default, all members within a class are public, and there’s no need to specify access modifiers for public members.
> Being public means that these members can easily be accessed outside of the class, in another part of the program

class ClassSchedule:
   def __init__(self, course, instructor):
       self.course = course
       self.instructor = instructor
  
   def display_course(self):
       print(f'Course: {self.course}, Instructor: {self.instructor}')

sched = ClassSchedule('Chemistry', 'Mr. Doe') # initializing
 
sched.display_course() # prints Course: Chemistry, Instructor: Mr. Doe
sched.course # prints 'Chemistry


All members here are accessible outside of the class. For example, we can access the variable course and method display_course() without any limitations:

Protected Access Modifier

Protected access modifiers, denoted with the prefix _, prevent members from being accessed outside of the class, unless it’s from a subclass.

class from the example above and make the members course and instructor protected with the _

class ClassSchedule:
   def __init__(self, course, instructor):
       self._course = course # protected
       self._instructor = instructor # protected
  
   def display_course(self):
       print(f'Course: {self._course}, Instructor: {self._instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')
sched.display_course()


Private Access Modifier

Private access modifiers, denoted with the prefix __, declare members to be accessible within the class only

Members with this modifier will be marked private and any attempt to access these members outside of the class will cause an Attribute Error message.

class ClassSchedule:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
  
   def display_course(self):
       # public
 
       print(f'Course: {self.__course}, Instructor: {self.__instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')
 
sched.__course # this will throw an Attribute Error because we're trying to access a private member
 
sched.display_course() # this won't throw an Attribute Error because this method is public


Eg - 
class ClassSchedule:
   def __init__(self, course, instructor):
       self.__course = course # private
       self.__instructor = instructor # private
 
   def display_course(self):
       # public
 
       print(f'yess: {self.__course}, Instructor: {self.__instructor}')
 
sched = ClassSchedule('Biology', 'Ms. Smith')

# the following will throw an Attribute Error because we're trying to access a private member
#sched.__course 
 

# this line won't throw an Attribute Error because this method is public
sched.display_course() 


OOP

Encapsulation

OOP 1 -> Encapsulation

Is a fundamental concept that describes wrapping variables and methods in one unit.

In encapsulation code and date are wrapped together within a single unit from being modifield  by accident.

# we restrict access to methods and variables. this prevent data from direct modification.

# access modifier concept is used in encapsulation 

example of encapsulation is a class, as it “encapsulates” members such as variables and methods in one single unit.

# can use protected and private access modifers


Class Variables -> A class can contain variables that can only be accessed by an object of the class.

class UserInfo:
   def __init__(self, username, email_address):
       self.username = username
       self.email_address = email_address
user = UserInfo('user123', 'abc@edf.ghi')
 
user.username
user.email_address

The data saved in the object can be accessed using the variables. For example, calling user.username will return ’user123’, and calling user.email_address will return ’abc@efd.ghi’.

Class Methods -> A class can also contain methods that can be accessed by objects of the class.

class UserInfo:
   def __init__(self, username, email_address):
      self.username = username
      self.email_address = email_address
 
   def check_username(self, username_to_check):
       if username_to_check == self.username:
           return True
       else:
           return False


We can call the method check_username on our object to run the method:

user = UserInfo('user123', 'abc@edf.ghi')
 
user.check_username('user123') # returns True
user.check_username('user456') # returns False


Abstraction

OOP 2 -> Abstraction

Abstraction is used to hide the internal details and show only functionalities.

It refers to a programming approach by which only the relevant data about an object is exposed, hiding all the other details.

A class is said to be an abstract class if it cannot be instantiated, that is you can have an object of an abstract class. You can however use it as a base or parent class for constructing other classes.


Create an Abstract Class - use @abstractmethod

To create an abstract class in Python, it must inherit the ABC class that is defined in the ABC module. and abstractmethod

Moreover, the class must have at least one abstract method. Again, an abstract method is the one which cannot be called but can be overridden

from abc import ABC, abstractmethod
class demo(ABC):

   @abstractmethod
   def method1(self):
      print ("abstract method")
      return

   def method2(self):
      print ("concrete method")


method1() is an abstract method

Note that the class may have other non-abstract (concrete) methods.


If you try to declare an object of demo class, Python raises TypeError −

obj = demo()
         ^^^^^^
TypeError: Can't instantiate abstract class demo with abstract method method1


Abstract Method Overriding -> using super()

from abc import ABC, abstractmethod
class democlass(ABC):
   @abstractmethod
   def method1(self):
      print ("abstract method")
      return
   def method2(self):
      print ("concrete method")

# An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

class concreteclass(democlass):
   def method1(self):
      super().method1()
      return
      
obj = concreteclass()
obj.method1()
obj.method2()

Output >

abstract method
concrete method


Inheritance

OOP 3 -> Inheritance

Enables the transfer of methods and properties of one class to another

Inheritance allows for reusability of code as well as extending the capability of new classes


Parent Class / base class ->  is the class whose methods and properties transfer over to the child class

We can define a parent class like we would for any class, with the constructor and any methods and properties we want to include

class Person:
   def __init__(self, name, age):
       self.name = name 
       self.age = age 
  
   def print_info(self):
       print(f'{self.name} is {self.age} years old')

Child Class / derived class ->  is the class that inherits methods and properties from the parent class

The child class must contain the following:
1. Name of the parent class in the definition of the child class
2. Constructor of the parent class called within the constructor of the child class

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def print_info(self):
      print(self.name)
      print(self.age)
 
class Teacher(Person):
  def __init__(self, name, age, subject):
      self.subject = subject
 
      Person.__init__(self, name, age)


# Code for parent person class and child teacher class with printing each methods

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print(self.name)
        print(self.age)
        
# 1. Name of the parent class in the definition of the child class
class Teacher(Person):
    def __init__(self,name,age, subject):
        self.subject = subject
# 2. Constructor of the parent class called within the constructor of the child class
        Person.__init__(self, name , age)
   
   
myTeacher = Teacher("ram" , 55 , "maths")

myTeacher.printinfo()

# Output -> ram and 55

print(myTeacher.subject)
# output -> maths



polymorphism

OOP 4 -> Polymorphism

concept of classes sharing methods with the same name

in classes - In Python, classes are allowed to contain methods that share the same name as another method from a different class

The code below shows two different classes that are independent of each other with some methods of the same names:

class Checking():
   def type(self):
       print('You have a checking account at the Codecademy Bank.')
 
   def balance(self):
       print('$20 left in your checking.')
 
class Savings():
   def type(self):
       print('You have a savings account at the Codecademy Bank.')
  
   def balance(self):
       print('$1000 left in your savings.')


# Code Example

class Checking():
   def type(self):
       print('You have a checking account at the Codecademy Bank.')
 
   def balance(self):
       print('$20 left in your checking.')
 
class Savings():
   def type(self):
       print('You have a savings account at the Codecademy Bank.')
 
   def balance(self):
       print('$1000 left in your savings.')


account_a = Checking()
account_b = Savings()
 
for account in (account_a, account_b):
   account.type()
   account.balance()


Output -> 

You have a checking account at the Codecademy Bank.
$20 left in your checking.
You have a savings account at the Codecademy Bank.
$1000 left in your savings.


Built-in Data Structures

String - single / double quotes

operations - indexing and slicing is done

indexing -> to access a certain character of the string

print(stringname[0]) -> get first character

slicing - using a range of indices to access multiple characters

string[0:n] / n is not included

negative indexing -> -n : 0


Build in functions

len() -> It takes the string as an argument to count the characters in the string

intro3 = "Hi there."
len(intro3) # evaluates 9

str.lower(), str.upper() / convert to lower and upper

str.title()

intro = "My name is jeff!"
print(intro.title()) # prints 'My Name Is Jeff!'


str.split() -> .split() takes a string and splits the string into a list of strings. By default, the function splits by whitespace but the separator can be specified as an argument.

intro = "My name is Jeff!"
print(intro.split()) # prints ['My', 'name', 'is', 'Jeff!']
print(intro.split('name')) # prints ['My ', ' is Jeff!']
print(intro.split('!')) # prints ['My name is Jeff', '']

Lists

In Python, lists are ordered collections of items that can contain different data types such as strings, integers, float values and many more.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]

can person indexing and slicing of list, same as string.

lst[0] -> abc

last[0:2] - > abc , 123

build in methods

len() ->  It takes the list as an argument to count the items in the list.

lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst2 = [0, 1, 2, 3, 4]
lst3 = ['I love sushi so much!', 'I also love curry!']
 
print(len(lst1)) # prints 6
print(len(lst2)) # prints 5
print(len(lst3)) # prints 2

.append() ->  .append() takes an item as an argument to add the item to the end of a list.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.append(99) 

# appends 99 at the end of the list
print(lst)

# Output -> ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i'], 99]

.pop() ->  takes an index and removes an item at that given index and returns that item. If no index is provided, it takes the last item from the list.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.pop() # removes ['g', 'h', 'i']
lst.pop(0) # removes 'abc'

.remove() -> .remove() removes an item that’s passed as the argument.

lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
lst.remove(62) # removes 62 from the list


# notes - argument is necessary in remove, unlike pop method

Tuples

just like list, but immutable ( meaning we can’t modify a tuple’s elements after creating one)

Tuples are one of the built-in data structures in Python. Just like lists, tuples can hold a sequence of items and have a few key advantages:
*       Tuples are more memory efficient than lists
*       Tuples have a slightly higher time efficiency than lists


This is mostly because tuples are immutable, meaning we can’t modify a tuple’s elements after creating one, and do not require an extra memory block like lists. Because of this, tuples are great to work with if you are working with data that won’t need to be changed in your code.

syntax - ()

Just like lists, tuples are sequences and can hold objects of different data types.

my_tuple = ('abc', 123, 'def', 456)

-> like apply indexing and slicing like list and strings

 Build in functions

len() - >  It takes the tuple as an argument to count the items in the tuple.

my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')
print(len(my_tuple)) # prints 6

max () ->
The built-in function max() returns the tuple’s maximum value. Note that this function requires all of the values to be of the same data type. 
> If used with numerical values, the function returns the maximum value. 
> If used with string values, the function returns the value at the tuple’s maximum index as if it was sorted alphabetically. The string closer to the letter “Z” in the alphabet would have a higher index.


returns the highest alphabetical character in a string

alpha = ("red" , "redx" , "z")

print(max(alpha))

my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
 
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

min() -> 
The built-in function min() returns the tuple’s minimum value. Similar to the max() function, the min() function requires all of the values to be of the same data type. If used with numerical values, the function returns the minimum value.

If used with string values, the function returns the value at the tuple’s minimum index as if it was sorted alphabetically. The string closer to the letter “A” in the alphabet would have a lower index.

my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"
my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!

.index() -> 
The built-in method `.index()’ takes in a value as the argument to find its index in the tuple.

my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

.count() -> occursance

The built-in method `.count()’ takes in a value as the argument to find the number of occurrences in the tuple.

my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1



Dictionaries

> In Python, dictionaries are defined with curly brackets {}
> Dictionaries contain what’s called key-value pairs, which refer to pairs of a key and a value separated by a colon :.
> The values can hold and be a mix of different data types, including lists or even nested dictionaries. However, keys must be an immutable data type such as strings, numbers or tuples

groceries = {
        'fruits': ['mangoes', 'bananas', 'kiwis'],
            'protein': ['beef', 'pork', 'salmon'],
            'carbs': ['rice', 'pasta', 'bread'],
            'veggies': ['lettuce', 'cabbage', 'onions']

}

Accessing and Writing Values

In contrast to other data structures such as lists and tuples, there are no built-in ways to use indexing and slicing to access the values in a certain order in the dictionaries. A value within a dictionary can be accessed with its key.

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
party_planning['Location'] # returns 'Our Backyard'

Likewise, values can be updated in the dictionary using its key:

party_planning['Location'] = 'At the park'
party_planning['Location'] # prints 'At the park'

Similarly, a new key-value pair can be added to a dictionary:

party_planning['Dress Code'] = 'Casual'

Common Built-in Functions

len()

The length of a dictionary can be measured using the built-in function len(). It takes the dictionary as an argument to count the number of key-value pairs in the dictionary.

party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}
 
len(party_planning) # returns 5


.update()

> takes dict as argument 
> The built-in method update() takes in a dictionary as an argument to update an existing dictionary
> Any new key-value pairs will be added to the existing dictionary, but overlapping key-value pairs from the new dictionary will overwrite the key-value pairs in the existing dictionary.

shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

.keys() and .values()

The built-in functions .keys() and .values() can be used to return the list of keys and values of a dictionary.

shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
 
shopping_list.keys() # returns dict_keys(['jewelry', 'clothes', 'budget'])
shopping_list.values() # returns dict_values(['earrings', 'jeans', 200])


Sets

> A set is an immutable, unordered collection of unique elements that can consist of integers, floats, strings and tuples
> However, sets cannot hold mutable elements such as lists, dictionaries.

In Python, a set is created with curly braces {} with items inside the braces separated by commas. See an example here:

set1 = {'Jenny', 26, 'Parker', 10.5}
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}

The built-in function set() can be used with a list argument to create a set from that list. Note that this will drop any duplicate elements in the list, as sets can only contain unique, non-duplicated elements. Here we can see lst being used with the set() function to create a set set2:

lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set2 = set(lst)
print(set2) # prints {10.5, 26, 'Jenny', 'Parker'}

Note -> cannot index the sets

TypeError: 'set' object is not subscriptable


Accessing and Writing Values

Sets do not have indexes or keys. We can use in to check to see if the element exists in the set:

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
print('Chau' in students) # returns True

Common Built-in Methods

.add()

Because sets are immutable, existing elements within the sets cannot be changed. However, new elements can be added using the built-in method add() which takes in an element to add to a set

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
 
students.add('George')

Note -> It’s important to note that if an element already exists in the set, the new element will not be added, as sets do not allow duplicate elements

.update() and .union()


update() -> The built-in method .update() takes in any iterable object, such as tuples, lists, dictionaries or sets, and adds the object to an existing set. Any duplicated elements will not be added.

students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students1.update(students2)

print(students1)

Output -> {'Carlos', 'Dmitry', 'Chau', 'Alice', 'Zhuo', 'Amy', 'Jane', 'Lily', 'Bridgette'}

# adding student 2 to student 1

Similarly, the built-in method .union() takes an iterable object and joins the new object with the existing object:

students1 = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
 
students3 = students1.union(students2)

print(students3)

output -> {'Amy', 'Zhuo', 'Carlos', 'Chau', 'Jane', 'Bridgette', 'Dmitry', 'Alice', 'Lily'}

# adding student 1 and student 2 to student 3

.remove() -> 

The built-in method .remove() takes in an element and removes it from the set. See an example below:

students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
students.remove('Bridgette')

for loops -> 

Because sets are iterable, we can utilize a for loop to iterate through a set.


Queues and Stacks

Two types of data structures: queues and stacks.

> They are both data structures that can hold a collection of items
> They both aren’t built into Python, but we can leverage Python’s built-in data structures, such as lists, to create them

difference

queue stores items in a first-in, first-out (FIFO) format

stack stores items in a last-in, first-out (LIFO) format


Stack 

append -> last of list
pop -> remove from last of list

use list to implement stack - simple implementation without specific functions and node

data = []

# enqueue
data.append(5)
data.append(10)
# dequeue
data.pop()
data.pop()

only limit list to append(n) and pop() to be a stack

Queue

data = []

# enqueue
data.append(5)
data.append(10)
# dequeue
data.pop(0)
data.pop(0)


# Peak -> look of last in stack and first in queue element


Custom implementation using class 

-> used to limit operation of our custom data structures

# stack

class Stack:
    
    def __init__(self):
        self.data = []
        
# enqueue
        def push(self,data):
            return self.data.append(data)
       
# dequeue 
        def pop(self):
            return self.data.pop()
        
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)

p = stack.pop()
f = stack.data[0]

print(p)
print(f)

output -> 
15
5

# queue

class Queue:
    
    def __init__(self):
        self.data = []
        
    def push(self,data):
        return self.data.append(data)
        
    def pop(self):
        return self.data.pop(0)
        
queue = Queue()

queue.push(5)
queue.push(10)
queue.push(15)

p = queue.pop()
f = queue.data[0]

print(p)
print(f)

Output -> 

5
10

YT video link -> https://www.youtube.com/watch?v=IxQHWt0GpsU

in code academy its implemented using “nodes”


=============================================

￼















"""
OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON
===========================================

This program demonstrates:

1. Class and Object
2. Constructor (__init__)
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

Author: Educational Example
"""

from abc import ABC, abstractmethod


# ==========================================================
# 1. CLASS AND OBJECT
# ==========================================================

print("\n" + "=" * 60)
print("1. CLASS AND OBJECT")
print("=" * 60)

# Class Definition
class Student:
    """
    A class is a blueprint/template for creating objects.
    """

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


# Creating Objects
student1 = Student("John", 20)
student2 = Student("Alice", 22)

print("\nStudent 1 Details")
student1.display()

print("\nStudent 2 Details")
student2.display()


# ==========================================================
# 2. ENCAPSULATION
# ==========================================================

print("\n" + "=" * 60)
print("2. ENCAPSULATION")
print("=" * 60)

class BankAccount:
    """
    Encapsulation means hiding data and controlling access.
    """

    def __init__(self, owner, balance):
        self.owner = owner

        # Private variable
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("Rahul", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Current Balance:", account.get_balance())

# Direct access will fail:
# print(account.__balance)


# ==========================================================
# 3. INHERITANCE
# ==========================================================

print("\n" + "=" * 60)
print("3. INHERITANCE")
print("=" * 60)

class Animal:
    """
    Parent/Base Class
    """

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    """
    Child/Derived Class
    """

    def bark(self):
        print("Dog is barking")


dog = Dog()

# Inherited method
dog.eat()

# Own method
dog.bark()


# ==========================================================
# 4. POLYMORPHISM
# ==========================================================

print("\n" + "=" * 60)
print("4. POLYMORPHISM")
print("=" * 60)

class Bird:
    def sound(self):
        print("Bird makes sound")


class Sparrow(Bird):
    def sound(self):
        print("Sparrow Chirps")


class Crow(Bird):
    def sound(self):
        print("Crow Caws")


birds = [Sparrow(), Crow()]

for bird in birds:
    bird.sound()

"""
Same method name (sound)
Different behaviors

This is Polymorphism.
"""


# ==========================================================
# 5. ABSTRACTION
# ==========================================================

print("\n" + "=" * 60)
print("5. ABSTRACTION")
print("=" * 60)

class Vehicle(ABC):
    """
    Abstract Class
    """

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts using key/button")


class Bike(Vehicle):

    def start(self):
        print("Bike starts using self-start/kick")


car = Car()
bike = Bike()

car.start()
bike.start()


# ==========================================================
# 6. REAL-WORLD EXAMPLE
# ==========================================================

print("\n" + "=" * 60)
print("6. REAL-WORLD OOP EXAMPLE")
print("=" * 60)

class Employee:

    company = "ABC Technologies"  # Class Variable

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID      : {self.emp_id}")
        print(f"Name    : {self.name}")
        print(f"Salary  : ₹{self.salary}")
        print(f"Company : {Employee.company}")


emp1 = Employee(101, "Arun", 50000)
emp2 = Employee(102, "Kiran", 60000)

print("\nEmployee 1")
emp1.display()

print("\nEmployee 2")
emp2.display()


# ==========================================================
# SUMMARY
# ==========================================================

print("\n" + "=" * 60)
print("OOP SUMMARY")
print("=" * 60)

print("""
1. Class
   Blueprint for objects.

2. Object
   Instance of a class.

3. Constructor
   Special method (__init__) executed automatically.

4. Encapsulation
   Hides data using private members.

5. Inheritance
   Child class acquires properties of parent class.

6. Polymorphism
   Same method, different behavior.

7. Abstraction
   Hides implementation details and shows only functionality.

Advantages of OOP:
------------------
✓ Code Reusability
✓ Modularity
✓ Better Security
✓ Easy Maintenance
✓ Scalability
✓ Real-world Modeling
""")
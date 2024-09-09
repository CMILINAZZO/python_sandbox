
# Function based on a list

def vitals(index):
   vital_signs = ["BP", "150/100 mmHg", "HR", "90 bpm", "RR", "18 breaths per minute"]
   blood_pressure = vital_signs[1]
   print(vital_signs[0])
   print("Blood Pressure " + blood_pressure)
   heart_rate = vital_signs[3]
   print(vital_signs[2])
   print("Heart Rate " + heart_rate)
   resp_rate = vital_signs[5]
   print(vital_signs[4])
   print("Respiratory Rate " + resp_rate)

vitals(0)


# Hello name function

'''
def hello_name(name):
  print("Hello " + name + "!")

hello_name("Carrie")
'''


# Input

print("Type your name.")
my_name = input()

print("Type the password.")
password = input()

if my_name == "Carrie" and password == "password":
  print("Hello Carrie")
  print("Access granted.")
else:
  print('Access denied.')

def errorMsg():
  if my_name != "Carrie" and password != "password":
    print("The name and password are incorrect.")
  if my_name == "Carrie" and password != "password":
    print("The password is incorrect.")
  if my_name != "Carrie" and password == "password":
    print("The name is incorrect.")

errorMsg()


  # Tuples are basically the same as lists, EXCEPT:
  # They are typed with parentheses instead of brackets.
  # They cannot have their values modified, appended or removed.


# The following won't work:

""""
eggs = ('hello', 42, 0.5)
eggs[1] = 99
"""


# Function based on a tuple

def cars():
  tuple_cars = ("chevrolet", "ford", "tesla", "toyota")
  print("Enter your car's brand in lowercase.")
  my_car = input()
  if my_car in tuple_cars:
    print("Your car is here.")
  else:
    print("Your car is not here.")

if my_name == "Carrie" and password == "password":
  cars()


# Function based on a dictionary

myDog = {'size': 'medium', 
         'color': 'white, brown and black',
         'disposition': 'anxious, sweetheart, occasionally spicy'}

def doggySize():
  print(my_name + "'s dog is " + myDog['size'] + " sized.")

doggySize()


# Trying try

try:
  poopoo()
except:
  print("A function was called that does not exist.")


# More complicated stuff


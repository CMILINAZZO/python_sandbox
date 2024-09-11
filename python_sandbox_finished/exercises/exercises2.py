
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

def hello_name(name):
  print("Hello " + name + "!")
hello_name("Carrie")


# Tuples are basically the same as lists, EXCEPT:
# They are typed with parentheses instead of brackets.
# They cannot have their values modified, appended or removed.

# And so, the following won't work:

'''
eggs = ('hello', 42, 0.5)
eggs[1] = 99
'''


# Function based on a tuple

def cars():
  tuple_cars = ("chevrolet", "ford", "tesla", "toyota")
  print("Enter your car's brand (in lowercase.)")
  my_car = input()
  if my_car in tuple_cars:
    print("Your car is here.")
  else:
    print("Your car is not here.")
cars()


# Function based on a dictionary

myDog = {'size': 'medium', 
         'color': 'white, brown and black',
         'disposition': 'anxious, sweetheart, occasionally spicy'}
def doggySize():
  print("Carrie's dog is " + myDog['size'] + " sized.")
doggySize()


# Trying try

try:
  poopoo()
except:
  print("A function was called that does not exist.")


# Nested lists

def nested_list():
   nested_list = [["BP", "HR", "RR"], [150, 90, 18]]
   print(nested_list[0][0])
   print(nested_list[1][0])
   print(nested_list[0][1])
   print(nested_list[1][1])
   print(nested_list[0][2])
   print(nested_list[1][2])
nested_list()


# Birthdays

def birthdays():
   birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
   while True: 
      print('Enter a name: (blank to quit)')
      name = input()
      if name == '':
         break
      if name in birthdays:
         print(birthdays[name] + ' is the birthday of ' + name)
      else:
         print('I do not have birthday information for ' + name)
         print('What is their birthday?')
         bday = input()
         birthdays[name] = bday
         print('Birthday database updated.')
birthdays()
# This does not actually update the dictionary. Is there a way to get it to actually update the dictionary?
# Would it need to write a new file?


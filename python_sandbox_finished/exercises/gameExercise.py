#Game - (soon to be) FIXED VERSION

#Dictionaries
inventory = {"bread": 12,
             "emeralds": 13,
             "lead": 1,
             "torch": 6,
             "iron sword": 1}

#Functions
def errorMsg():
  if my_name != "Carrie" and password != "password":
    print("The name and password are incorrect.")
  if my_name == "Carrie" and password != "password":
    print("The password is incorrect.")
  if my_name != "Carrie" and password == "password":
    print("The name is incorrect.")

def sum_values(inventory):
  total = 0
  for value in inventory.values():
    if isinstance(value, (int,float)):
      total += value
  return total

def nameAndPassword():
    global my_name, password
    while True:
        if my_name == "Carrie" and password == "password":
            print("Access granted. Welcome back to The Game,", my_name, "!")
            break
        else:
            print('Access denied.')
            errorMsg()

            print("Type your name.")
            my_name = input()

            print("Type the password.")
            password = input()


print("Type your name.")
my_name = input()

print("Type the password.")
password = input()

nameAndPassword()

user_input = input("Enter 'I' to view inventory: ")

if user_input.upper() == "I":
  for key, value in inventory.items():
    print(f"{key}: {value}")
  total_items = sum_values(inventory)
  print("Total number of items:", total_items)

# Next, add a way to add or remove specific items from inventory. (Add an inventory limit - like 35.)
# Add health and hunger points, and a way to view health points & hunger points.
# Add a way to gain/lose those.
# Add a way to change name and password.
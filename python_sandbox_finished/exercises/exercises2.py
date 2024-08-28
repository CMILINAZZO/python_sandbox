
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



"""
Task 6: Sensor Data

Create an empty list.

Ask the user how many sensor readings they want to enter.

Then take each reading from the user and store it in the list.

Finally, display all readings.
"""
list_1=[]
n=int(input("how may sensor readings "))
for i in range(n):
  values=int(input("enter sensor vaule"))
  list_1.append(values)
print(list_1)
for i in list_1:
  print("vaules",i)

# Online Python compiler (interpreter)
# Write and run Python online using this editor.
student_data=[["ashika",22,450],["roshan",22,450],["rahul",23,430],["nithya",23,420],["jegan",26,450]]
print(student_data)
print("Students name")
i=1
for values in student_data:
  
  print(f"student name{i}:{values[0]}")
  i+=1
print("Students marks")
i=1
for values in student_data:
  
  print(f"student {i} :{values[2]}")
  i+=1
i=1
for values in student_data:
  
  print(f"student name{i}:{values[0]}")
  i+=1

m=int(input("enter which student mark to modify"))
m-=1
mark=int(input("enter new mark"))
student_data[m][2]=mark
print("updated mark")
i=1
for values in student_data:
  
  print(f"student {i} :{values[2]}")
  i+=1
student_data.pop(3)
print(student_data)
student_data.append(["nithya",22,400])
print(student_data)
#for student in student_data:
#  sorted(student[2])
 # print(student[2])
count=0
for student in student_data:
  if 450==student[2]:
    count+=1
print(count)
print("enter a student's name and display that student's position in the dataset.")
student_name=input("enter student name")
i=0
for student in student_data:
  if student_name in student:
    print("student position",i+1)
    break
  i=i+1
else:
  print("invaild student")

student_data.sort(key=lambda student: student[2], reverse=True)

print(student_data)


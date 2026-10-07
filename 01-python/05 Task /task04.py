#•	Student marks calculator 
num=int(input("enter how many student"))
i=1
while(i<num):
  roll_no=int(input("enter roll no."))
  stu_name=input("enter student name")
  
  eng=int(input("enter english mark"))
  tam=int(input("enter tamil mark"))
  math=int(input("enter math mark"))
  sci=int(input("enter sci mark"))
  social=int(input("enter social mark"))
  
  total_mark=eng+tam+math+sci+social
  average=total_mark/5
  print("student name:",stu_name)
  print("student roll num",roll_no)
  print(f"total mark of student{i}:{total_mark}")
  print("average",average)
  
  i=i+1
  print("enter next student",i)

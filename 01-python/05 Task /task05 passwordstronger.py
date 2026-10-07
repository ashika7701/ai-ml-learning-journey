#•	Password strength checker 
password=input("enter your password")
has_upper = 0
has_lower = 0
has_number = 0
has_special= 0
has_length= 0

for char in password:
  if char.isupper():
      
      has_upper=1
      

  elif char.islower():
      has_lower=1
       
     

  elif char.isdigit():
      has_number=1
      


  elif not char.isalnum():
      has_special=1
      
if len(password)>=8:
  has_length=1
      
      
if has_upper==1 and has_lower==1 and has_number==1 and has_special==1 and has_length==1:
  print("strong pass")
else:
  print("make sure password contain number, uppercase, special symbol")
  
  
 

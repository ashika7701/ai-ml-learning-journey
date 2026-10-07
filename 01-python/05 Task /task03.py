```python
print("date format should be ex:- 01/01/2027")

dob = input("enter your date of birth")
cdate = input("enter date to calculate")

cdate = cdate.split("/")
dob = dob.split("/")

# Convert day, month and year to integers
cdate[0] = int(cdate[0])
cdate[1] = int(cdate[1])
cdate[2] = int(cdate[2])

dob[0] = int(dob[0])
dob[1] = int(dob[1])
dob[2] = int(dob[2])

year = cdate[2] - dob[2]

if cdate[1] < dob[1]:
    year = year - 1

elif cdate[1] == dob[1] and cdate[0] < dob[0]:
    year = year - 1

print("your current age", year)
```


import numbers
from tokenize import Number


students=["cash money","hero","developer"]

# access individual value

print(students[0])
# print whre you want to stop
print(students[1:2])

numbers=[2,14,67,1]
# list function
students.extend(numbers)
students.append("kali")
students.insert(1,"mariyam")
students.remove("hero")
numbers.sort()  #make in normall arrangements
numbers.reverse()
print(students)
print(numbers)

# copy() function used to copy the same one detils and put to other section
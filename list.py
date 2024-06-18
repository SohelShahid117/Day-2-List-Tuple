marks =[72,84,33.6,88,99,56,78.5]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))
marks[0]=89.7
print(marks)

student =["sohel",2.83,"EEE"]
print(student)
print(type(student))
print(student[1])
student[0]="Sumi"
print(student)

std =["shahid"]
# std =["shahid",]
print(std)

# list slicing
print(marks[2:])
print(marks[:2])
print(marks[:-2])
print(marks[-5:])
print(marks[-5:-1])

# print(marks.sort())
marks.append(99)
print(marks)
marks.sort()
print(marks)
# marks.sort(reverse=True)
# print(marks)
marks.reverse()
print(marks)


fruit = ["litchi","banana","mango","apple","orange"]
fruit.sort()
print(fruit)
fruit.reverse()
print(fruit)
fruit.append("papya")
print(fruit)
fruit.insert(1,"tanana")
# fruit.insert(indx,element)
print(fruit)

# fruit.remove(4)
fruit.pop(4)
print(fruit)
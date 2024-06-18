# Lecture 3 : List & Tuple in Python | Python Full Course
# https://youtu.be/qVyvmzFxF_o?si=0KgKnMjaLZFhtA_e
t=(66,44,55,77)
print(t)
print(type(t))
print(t[0])
# t[0]=99
print(t)

# list:mutable
# tuple:immutable
print(t[1:])
print(t[:3])

t2 = ()
print(t2)
print(type(t2))

# t3 = (1)
t3 = (1+5)
print(t3)
print(type(t3))

t4=(9,2,2,4,2,1,5,4)
print(t4.count(2))
print(t4.index(2))
print(t4.index(1))

# palindrom
"""
Given a string, write a python function to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.
RADAR,
ABBA
AMMA
121
787
"""

movies = []
mov1 = input("Enter 1st Movie name :")
mov2 = input("Enter 2nd Movie name :")
mov3 = input("Enter 3rd Movie name :")
mov4 = input("Enter 4th Movie name :")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
movies.append(mov4)
print(movies)

# list1 = [1,2,2,1]
list1 = ["a","m","m","a","s"]
list2 = [1,2,3,4]

copy_list1=list1.copy()
print(copy_list1)
copy_list1.reverse()
print(copy_list1)
if(list1 == copy_list1):
    print("palindrom")
else:
    print("not palindrom")

grade = ["A","B","F","D","C","A","D"]
print(grade.count("A"))
grade.sort()
print(grade)

# list vs tuple
# https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/
"""
Lists and Tuples in Python are two classes of Python Data Structures. The list structure is dynamic, and readily changed whereas the tuple structure is static and cannot be changed. This means that the tuple is generally faster than the list. Lists are denoted by square brackets and tuples are denoted with parenthesis.
"""
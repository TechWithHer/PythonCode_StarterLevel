#Task1 
#Creating a list of even numbers

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_num = [n * n for n in num]  # Corrected list comprehension
print(new_num)

#Task2
#Manipulate the fruit list 

fruits = ['apple', 'banana', 'cherry', 'kiwi']

#replace 'banana'  with 'mango'
print(fruits)
fruits[1] = 'mango'
print(fruits)

#adding orange at the end 
fruits.append('orange')

print(fruits)
fruits.remove('cherry')
print(fruits)

#Task3 Playing around with List 

names = ['John', 'Mia', 'Alexandra', 'Sam', 'Chris']

for name in names:
	if(len(name)<4):
	  names.remove(name)

print(names)

#Task4 Square of the list

num1= range(1,11)
new_num1= [n * n for n in num1]  # Corrected list comprehension
print(new_num1)

# Given lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Create a new list of tuples using list comprehension
combined_list = [(list1[i], list2[i]) for i in range(len(list1))]

# Print the output
print(combined_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

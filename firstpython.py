print("Hello World")
name = "List"
numbers = [1,2,3,4,5,6,7]
squares = [num**2 for num in numbers if num%2==0]      #list comprehension
print(squares)
print(name)

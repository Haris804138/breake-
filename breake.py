# 1
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
    print(f"Checking: {num}")

# 2
i = 0 
while i < 10:
    if i == 5:
        break
    print(i)
    i +=1
    
# 3
fruits = ['apple', 'banana', 'cherry', 'date']
for fruit in fruits:
    if fruit == 'cherry':
        print("Cherry found, stopping the loop.")
        break
    print(f"Current fruit: {fruit}")
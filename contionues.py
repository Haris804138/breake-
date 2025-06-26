# 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")

# 2
for i in range(5):
    if i == 3:
        continue
    print(f"Current number: {i}")

# 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(f"Current value of i: {i}")
    
    # 4
    
fruits = ['apple', 'banana', 'cherry', 'date']
for fruit in fruits:
    if fruit == 'cherry':
        continue
    print(f"Current fruit: {fruit}")
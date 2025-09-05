print("Even numbers from 0 to 50:")
print("Odd numbers from 0 to 50:")

for number in range(51):  
    if number % 2 == 0: 
        print(f"Even: {number}")
    else:  
        print(f"Odd: {number}")
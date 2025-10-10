
def lion():
    alnst = ["mizisua", "ivantill", "racoon", "gabu", "nenene"]
    print(alnst.index("lion")) 

def lion2():
    numbers = [1,1,1,1,1,1,1,2]
    nenene = numbers.index(2)  
    print(nenene)

def lion3(name):
    print("I am " + name + " lomi :p")

def lion4():
    odd_num = []
    for i in range(1, 21):   
        if i % 2 != 0:      
            odd_num.append(i)
    print(odd_num)

def lion5():
    True_password = "21112142069"  
    while True:
        user_input = input("Enter password: ")
        if user_input == True_password:
            print("Password is correct!")
            break
        else:
            print("Password is incorrect!")
# An array is a collection that can store multiple values in one variable.
# def is used to define a function. A function is a reusable block of code that performs a specific task.

color = ["periwinke-pink", "blue", "orange", "periwinke-pink", "yellow", "periwinke-pink", "blue"]
print(color.count("periwinke-pink")) 

def multiply(a, b):
    return a * b
print(multiply(5, 3)) 


animals = ["Lion", "Tiger", "Frog", "Panda", "kitty", "kasper", "toy"]
print(animals[1])  
print(animals[3])  
print(animals[5])  

print(animals[2])  
print(animals[5]) 

print(animals[-6])  
print(animals[-4])  
print(animals[-2])  

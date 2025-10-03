family = ["maya", "zamir"]

family.append("ano")
print(family)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num:
    if i % 2 == 0:
        print (i, "is odd")
    else:
        print (i, "is even")


list = ["saga of the tanyna the evil", "aleqsa", 'shaurma', 'gabu', 'haloween', 'haakon', 'taso', 'atack on titan', 'spotify', 'demon slayer']

for i in list:
    print(list[::2])

toy= "bored"

for index in range(len(toy)):
    print({toy[index]}-{index + 1})

list = ["anano", "aleqsa"]
print(list[::-1])
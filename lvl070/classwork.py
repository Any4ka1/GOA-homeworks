#Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.
#a = [x*10 __ x range ( __, 9)]
a = [x * 10 for x in range(5, 10)]
print(a)

num = [1,2,3,4,5,6,6,7,8,9,9,9,0,99,9,9,9,9,9,9,12312123,123,123,123,5,123,4,5,5,4]
def even_or_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
result = map(even_or_odd, num)
print(list(result))
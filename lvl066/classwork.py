#givng a list [ 2, 3,4,5,6,7,89,222,3,1,1,5,8]
#use list comperhention and fillter ony odd elements
wonderhoy = [2, 3, 4, 5, 6, 7, 89, 222, 3, 1, 1, 5, 8]
odd_wonderhoy = [num for num in wonderhoy if num % 2 != 0]
print(odd_wonderhoy)
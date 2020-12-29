# take an input
a = input("enter a number to check it is palindrome or not:")
# create two lists
b = []
c = []
# store all the value of given input to lists one by one form 0 index to nth
for i in range(0, len(a)):
    b.append(a[i])
    c.append(a[i])
# reverse the order of the list b
b.reverse()
# check if b == c for palindrome condition
if b == c:
    print("palindrome")
# otherwise print not palindrome
else:
    print("not palindrome")

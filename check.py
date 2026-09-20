# #greatest among 3 nos using logical operators
# while True:
#     a = int(input("Enter your first no : "))
#     b = int(input("Enter your second no : "))
#     c = int(input("Enter your third no : "))
#     if(a>b and a>c):
#        print("First num is rhe greatest")
#     elif(b>a and b>c):
#        print("second num is rhe greatest")
#     elif(c>a and c>b):
#        print("third num is rhe greatest")
#     else:
#        print("hmmm some error")
#     ag = input("do you want to cotinue?(Y/N)") 
#     if ag not in ("y","yes"):
#        print("Thank you for using")
#        break

#make a star triangle
# for i in range(1,6):
#     for j in range(1,i+1):
#        print("*", end = " ")
#     print()

#make a centre Triangle

rows = 5
for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
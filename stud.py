#to find the possible combinations 'n' number of students can shuffle their answer sheets without them having their own answer sheets.
#example : if 3 students (A,B,C) have a,b,c as their answer sheets, then student A should not have 'a', student B should not have 'b' and student C should not have 'c'.

n = int(input("Enter the number of students: "))
a = 0
b = 1

for i in range(1,n+1):
    c = (a+b)*(i-1)
    a = b
    b = c
print("Possible combinations: ", end="")
print(c)
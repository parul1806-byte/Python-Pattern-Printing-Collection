'''
# pattern 1
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
n = int(input("enter no of row needed:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print()

#pattern 2
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
n = int(input("enter the no of row:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#pattern 3
#1
#2 1
#3 2 1
#4 3 2 1
#5 4 3 2 1
n = int(input("enter the no of row:"))
for i in range(2,n+1):
    for j in range(2,i+1):
        i-=1
        print(i,end=" ")
    print()

#pattern 4
#4
#3 3
#2 2 2
#1 1 1 1
n = int(input("enter the no of row needed:"))
for i in range(1,n):
    for j in range(1,i+1):
        print(n-i,end=" ")
    print()
'''
#pattern5:
#5
#5 4
#5 4 3
#5 4 3 2
#5 4 3 2 1
n = int(input("enter the no of row needed:"))
for i in range(n):
    for j in range(i+1):
        print(n-j,end=" ")
    print()

'''pattern 6
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5
'''
n = int(input("enter the no of row needed:"))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j,end=" ")
    print()

'''patter:7

'''

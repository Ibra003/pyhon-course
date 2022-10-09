# left pattern
# m=5
# for k in range(1,m+1):
#     for s in range(1,k+1):
#         print("*",end="")
#     print()

# right pattern
n=5
for i in range(n):
    for j in range(1,n-1):
        print("",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()


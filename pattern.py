#rectangular pattern

n = int(input('Enter the number: '))

for i in range(n):
    for j in range(n):
        print('*',end = ' ')
    print()


# Here the number of column is equal to i in each line
# triangular pattern 

n = int(input('Enter the number '))

for i in range(n):   
    for j in range(i+1):
        print('*',end = ' ')
    print()
        

# inverted triangular pattern

n = int(input('Enter the number: '))

for i in range(n):
    for j in range(n-i):
        print('*',end = ' ')
    print()
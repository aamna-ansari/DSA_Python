#   * * * * 
#   * * * * 
#   * * * * 
#   * * * * 

for i in range(4):  # Outer loop for rows
    for j in range(4):  # Inner loop for columns
        print("*", end=" ")  # Print '*' without a newline
    print()  # Move to the next line after each row


#   * 
#   * *  
#   * * * 
#   * * *

for i in range(4):
    for j in range(i+1):
        print("*", end=" ")
    print()
# Pattern 3
for i in range(4):  # Controls the rows
    for j in range(i + 1):  # Controls the numbers in each row
        print(j + 1, end=" ")  # Print numbers starting from 1
    print()  # Move to the next line



# Pattern 4
for i in range(4):  # Controls the rows
    for j in range(i+1):  # Controls the numbers in each row
        print(i+1, end=" ")  # Print numbers starting from 1
    print()


    
# Pattern 5
    for i in range(4):  # Controls the rows
        for j in range(4 - i):  # Controls the numbers in each row
            print(j+1, end=" ")  # Print numbers starting from 1
        print()


# Pattern 7
for i in range(6): # outer loop 
    # space inner 
    for j in range(6-i): # inner loop
        print(" ", end=" ")
    # Star 
    for j in range(2* i+1):
        print("*", end=" ")
    # Space
    for j in range(6-i):
        print(" ", end=" ")
    print()
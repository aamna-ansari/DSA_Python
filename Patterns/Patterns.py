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
# Upper pyramid
for i in range(6):  # Outer loop (rows)
    for j in range(6 - i):  # Leading spaces
        print(" ", end=" ")
    
    for j in range(2 * i + 1):  # Stars
        print("*", end=" ")

    print()

# Lower inverted pyramid
for i in range(5, -1, -1):  # Start from 5 to match the upper pyramid
    for j in range(6 - i):  # Leading spaces
        print(" ", end=" ")

    for j in range(2 * i + 1):  # Stars
        print("*", end=" ")

    print()


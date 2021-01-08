#1.2.3
#Create a list of all even integers 1-1000.
# Write a loop that prints all numbers in the above list, separated by commas.

def main():
    #Code goes here
    list_3 = []

    # Write a loop that prints all numbers in the above list, separated by commas.
    # iterating each number in list
    for num in range(2,1001,2):
     list_3.append(num)

    print("Prints all numbers of a list of all even integers 1-1000:",list_3)



if __name__ == '__main__':
    main()
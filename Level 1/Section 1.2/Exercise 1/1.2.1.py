#1.2.1
#Write a program that does the following:
#Keeps asking the user for a number, until the user enters the letter s.
#Once the user finishes entering numbers, calculate and display the average of the numbers.
#You should do this using a loop.

def main():
    #Code goes here
    numList=[]

    # Keeps asking the user for a number, until the user enters the letter s.
    while (True):
        num = input('Enter a number (s to stop): ')
        if num == 's':
            break
        elif num =='':
            continue
        else:
            numList.append(float(num))
    # Once the user finishes entering numbers, calculate and display the average of the numbers.
    print("Average of the numbers:",sum(numList)/len(numList))


if __name__ == '__main__':
    main()
#Student Name: Jianwei Su
#Date: 04/23/2022
#4.1.1


def main():
    # Code goes here
    print('\n==========Exercise 4.1.1==========')
    print('Testing about Python Strings.\n')

    print('------Testing block 1-----')
    print('Display the length of the string.')

    #Set a is the string
    a=' The Python course is the best course that I have ever taken. '

    print('The length of string a is',len(a))

    print('\n------Testing block 2-----')
    print('Find the index of the first ‘o’ in the string.')

    #Method 1
    print('The index of the first ‘o’ in the string(using .find()):',a.find('o'))

    #Method 2
    print('The index of the first ‘o’ in the string(using .index()):', a.index('o'))

    print('\n------Testing block 3-----')
    print('Trim off the leading spaces only.')

    #lstrip() method removes whitespace at the beginning of a string.
    print('Trim off the leading spaces:',a.lstrip())

    print('\n------Testing block 4-----')
    print('Trim off the trailing spaces only.')

    # rstrip() method removes whitespace at the end of a string.
    print('Trim off the trailing spaces:', a.rstrip())

    print('\n------Testing block 5-----')
    print('Trim off both the leading and trailing spaces.')

    #strip() method removes whitespace at the beginning and end (both sides) of a string.
    b=a.strip()

    print('Trim off both the leading and trailing spaces:', b)

    print('\n------Testing block 6-----')
    print('Fully capitalize the string.')

    print('String after capitalizing:',b.upper())

    print('\n------Testing block 7-----')
    print('Fully lowercase the string.')

    print('String after lowercasing:', b.lower())

    print('\n------Testing block 8-----')
    print('Display the number of occurrence of the letter ‘d’ and of the word ‘the’.')

    print('The number of occurrence of the letter ‘d’:',b.count('d'))
    print('The number of occurrence of the letter ‘the’:', b.count('the'))

    print('\n------Testing block 9-----')
    print('Display the first 15 characters of the string.')

    print('The first 15 characters of the string:',b[:15])

    print('\n------Testing block 10-----')
    print('Display the last 10 characters of the string.')

    print('The last 10 characters of the string:', b[-10:])

    print('\n------Testing block 11-----')
    print('Display characters 5-23 of the string.')

    print('The characters 5-23 of the string:', b[4:23])

    print('\n------Testing block 12-----')
    print('Find the index of the first occurrence of the word ‘course’. ')

    print('The index of the first occurrence of the word ‘course’(via .find()):', b.find('course'))
    print('The index of the first occurrence of the word ‘course’(via .index()):', b.index('course'))

    print('\n------Testing block 13-----')
    print('Find the index of the second occurrence of the word ‘course’.')

    #Method 1
    print('The index of the second occurrence of the word ‘course’(method 1):', b.find('course',b.find('course')+1))

    #Method 2
    #Set the position after the first one.
    print('The index of the second occurrence of the word ‘course’(method 2):', b.find('course', 12))

    print('\n------Testing block 14-----')
    print('Find the index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd characters in the string.')

    #Set c is the enumerate list of the string from 7th to 33rd
    c=list(enumerate(b[6:33]))

    print('The enumerate list of the string from 7th to 33rd',c)

    #x+6 because we want to know the index from 7th to 33rd
    d=[x+6 for (x,y) in c if y=='t']
    print('The index of the first to last occurrence of the letter ‘t’, between the 7th and 33rd characters in the string:',d)
    print('The index of the second to last occurrence of the letter ‘t’, between the 7th and 33rd characters in the string:',d[1:])

    print('\n------Testing block 15-----')
    print('Replace the period (.) with an exclamation point (!).')

    print('Replace the period (.) with an exclamation point (!):',b.replace('.','!'))

    print('\n------Testing block 16-----')
    print('Replace all occurrences of the word ‘course’ with ‘class’.')

    print('Replace all occurrences of the word ‘course’ with ‘class’:', b.replace('course', 'class'))


    print('\n***Program Complete***')




if __name__ == '__main__':
    main()
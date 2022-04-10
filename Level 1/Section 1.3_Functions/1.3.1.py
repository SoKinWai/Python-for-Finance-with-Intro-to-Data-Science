#Student name: Jianwei Su
#Date: 04/05/2022
#1.3.1



#A week day function that takes integer from 1 to 7 as input,
# then prints out the day of the week for a given number. I.e. Sunday is 1, Monday is 2, etc.
#It returns a tuple of the original number and the corresponding name of the day.
def week_day_function(num):
       # A list of 7 weekdays
       weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

       #It prints out the day of the week for a given number. I.e. Sunday is 1, Monday is 2, etc.
       print(weekdays[num-1],"is",num)

       # It returns a tuple of the original number and the corresponding name of the day.
       return (num,weekdays[num-1])


def main():
    # Code goes here
    print('\n==========Exercise 1.3.1===========')

    #It takes integer from 1 to 7 as input
    #They print out the day of the week for a given number. I.e. Sunday is 1, Monday is 2, etc and
    #then print out a tuple of the original number and the corresponding name of the day.
    print('Print out the whole function of week day function:')
    print(week_day_function(1),'\n')
    print(week_day_function(2),'\n')
    print(week_day_function(3),'\n')

    #It takes integer from 1 to 7 as input
    #They just print out the day of the week for a given number. I.e. Sunday is 1, Monday is 2, etc
    print('Run the week day function for a given number:')
    week_day_function(4)
    week_day_function(5)
    week_day_function(6)
    week_day_function(7)

    print('\n***Program Complete***')

if __name__ == '__main__':
    main()

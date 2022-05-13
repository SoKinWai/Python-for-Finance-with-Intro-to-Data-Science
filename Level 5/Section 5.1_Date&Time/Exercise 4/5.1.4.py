#Student Name: Jianwei Su
#Date: 05/09/2022
#5.1.4

import logging
import datetime
import operator

opDict={'+':operator.add,
        '-':operator.sub}


def date_calculator(d_1,d_2,op):

    date=datetime.datetime.strptime(d_1,'%Y-%m-%d %H:%M:%S:%f')

    delta_time=datetime.datetime.strptime(d_2,'%d %H:%M:%S:%f')

    date_calcu=op(date,datetime.timedelta(days=delta_time.day, hours=delta_time.hour, minutes=delta_time.minute, seconds=delta_time.second, microseconds=delta_time.microsecond))

    date_result=date_calcu.strftime('%Y-%m-%d %H:%M:%S:%f')

    logging.info(f'The time result is:{date_result}')




def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\n==========Exercise 5.1.4==========')

    logging.info('\n------Testing block-----')
    logging.info('Display the calculated resulting date and time.')

    # Prompt the user to enter any date and time.
    d_1 = input('Please enter the date in the following format(YYYY-mm-dd HH:MM:SS:fffff e.g.2016-09-25 18:23:14:012342):')

    # Prompt the user to enter a delta time that is used to add or subtract from the original.
    d_2 = input('Please enter a delta time that is used to add or subtract from the original(dd HH:MM:SS:ffff):')

    op=input('Enter the operator to perform(+,-):')

    try:
        date_calculator(d_1,d_2,opDict.get(op))
    except Exception as ex:
        logging.exception(ex)
        logging.error('Invalid date info entered.')







    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()




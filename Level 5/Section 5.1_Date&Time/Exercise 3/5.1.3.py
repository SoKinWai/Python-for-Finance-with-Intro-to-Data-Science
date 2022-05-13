#Student Name: Jianwei Su
#Date: 05/09/2022
#5.1.3

import logging
import datetime

def main():
    # Code goes here

    # This line of codes will make sure those information to be displayed.
    logging.getLogger().setLevel(logging.INFO)


    logging.info('\n==========Exercise 5.1.3==========')

    logging.info('\n------Testing block 1-----')
    logging.info('\nAsks the user to input year, month, day, hour, minute, second, microsecond (one after another):')

    date=input('Please enter the date in the following format(YYYY Month_name dd HH:MM:SS:fffff e.g.2016 September 25 06:24:14:12342 PM):')


    logging.info('\n')


    logging.info('\n------Testing block 2-----')
    logging.info('\nCreate a datetime variable with the entered info')
    try:
        date_time=datetime.datetime.strptime(date,'%Y %B %d %I:%M:%S:%f %p')

        logging.info(f'The datetime variable with the entered info: {date_time}')



        logging.info('\n')

        logging.info('\n------Testing block 3-----')
        logging.info('\nExtract the datetime into year, month, day, hour, minutes, second, and microsecond.')

        logging.info(f'year: {date_time.year}')
        logging.info(f'month: {date_time.month}')
        logging.info(f'day: {date_time.day}')
        logging.info(f'hour: {date_time.hour}')
        logging.info(f'minute: {date_time.minute}')
        logging.info(f'second: {date_time.second}')
        logging.info(f'microsecond: {date_time.microsecond}')

        logging.info('\n')

        logging.info('\n------Testing block 4-----')
        logging.info('\n Display the entered datetime with the following format: 2016-09-25 18:23:14:12342')

        d_1=date_time.strftime('%Y-%m-%d %H:%M:%S:%f')

        logging.info(f'Display the entered datetime with the following format: 2016-09-25 18:23:14:12342: {d_1}')

        logging.info('\n')

        logging.info('\n------Testing block 5-----')
        logging.info('\n Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM')

        d_2 = date_time.strftime('%Y %B %d %I:%M:%S:%f %p')

        logging.info(f'Display the entered datetime with the following format: 2016 September 25 06:24:14:12342 PM:{d_2}')

        logging.info('\n')

        logging.info('\n------Testing block 6-----')
        logging.info('\n Do parts 4-5 with the current local time.')


        d_local_1 = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S:%f')
        d_local_2 = datetime.datetime.today().strftime('%Y %B %d %I:%M:%S:%f %p')

        logging.info(f'Part 4 with the current local time:{d_local_1}')
        logging.info(f'Part 5 with the current local time:{d_local_2}')

        logging.info('\n')

        logging.info('\n------Testing block 7-----')
        logging.info('\n Do parts 4-5 with the current UTC time.')

        d_UTC_1 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S:%f')
        d_UTC_2 = datetime.datetime.utcnow().strftime('%Y %B %d %I:%M:%S:%f %p')

        logging.info(f'Part 4 with the current UTC time:{d_UTC_1}')
        logging.info(f'Part 5 with the current UTC time:{d_UTC_2}')

        logging.info('\n')









    except Exception as ex:
        logging.exception(ex)
        logging.error('Invalid date info entered.')















    logging.info('\n***Program Complete***')

if __name__ == '__main__':
    main()
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


cities_typos = {'New York' : {'newyork','ny','nyc','newyorkcity','newyorks','new','newy','newyo','newyor'},
                'Washington' : {'washington','w','wa','was','wash','washi','washin','washing','washingt','washingto',
                               'dc','washingtondc'},
                'Chicago' : {'chicago','c','ch','chi','chic','chica','chicag','cicago','cago','chiccago'}
               }


months_typos = {'January' : {'january','jan','jaun','janu','janua','januar','jamuary','janauary','jauary','janyary',
                  'jaunary','janurary','janaury'},
                'February' : {'february','feb','fer','febr','ferb','ferbu','febru','februa','febrau','februar',
                    'febrary','febraury','februaury','februrary','februray','febuary','feburary','febaury','fervary'},
                'March' : {'march','mar','mars','marc'},
                'April' : {'april','ap','apr','arpil','apirl','apri','aprill'},
                'May' : {'may','ma','mayy','mmay','maay'},
                'June' : {'june','jun','ju','jue','jjune','junee','jjne'},
                'July' : {'july','jul','jjuly','juuly','jly'},
                'August' : {'august','auguat','ausust','au','aug','augu','augus'},
                'September' : {'september','sectember','seotember','sepember','septembrer','septmber','septermber',
                    'se','sep','sept','septe','septem','septemb','septembe','setpember'},
                'October' : {'october','oc','oct','octo','octob','octobe','ocober','ocotber','octoebr','octber',
                  'octoer','octomber','octuber'},
                'November' : {'november','no','nov','nove','novem','novemb','novembe','nobember','novemeber','novemeber',
                   'novemebr','novemer','novemver','novermber','novmber','novmeber'},
                'December' : {'december','de','dec','dece','decem','decemb','decembe','decemeber','decemer','decmeber',
                   'decemver'},
                'all' : {'all','aal','aall','alll','al','aalll','alls'}
               }


days_typos = {'Monday' : {'monday','m','mo','mon','mond','monda','munday','momday','minday','mondays'},
              'Tuesday' : {'tuesday','tu','tue','tues','tuesd','tuesda','teusday','tusday','tuesdays'},
              'Wednesday' : {'wednesday','w','we','wed','wedn','wedne','wednes','wednesd','wednesda','wensday','wendsday',
                            'wendsay','wednesdays'},
              'Thursday' : {'thursday','th','thu','thur','thurs','thursd','thursda','thursdaye','thrudsay','thrudsar',
                           'trusday','thrusday','thursdays'},
              'Friday' : {'friday','f','fr','fri','frid','frida','fridae', 'froday','fridays'},
              'Saturday' : {'saturday','sa','sat','satu','satur','saturd','saturda','saterday','saterdays'},
              'Sunday' : {'sunday','su','sun','sund','sunda','sundays'},
              'all' : {'all','aal','aall','alll','al','aalll','alls'}
             }


answer_typos = {'yes' : {'yes','y','ye','yeah','yea','yees','yeees','yay','ys','yas','yaas','ya','yaa','yap','yup','yep'},
               'no' : {'no','noo','nooo','nope','n','na','naa','naaa'}}

convert = {'New York' : 'new york city', 'Chicago' : 'chicago', 'Washington' : 'washington',
          'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9,
          'October' : 10, 'November' : 11, 'December' : 12,
          'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5, 'Sunday' : 6}


def notypos(word,wordict):
    if word.capitalize() in wordict.keys():
        return(word.capitalize())
    else:
        word = ''.join(letter for letter in word if letter.isalpha()).lower()
        for key in wordict.keys():
            if word in wordict[key]:
                return(key)
        return('Not found.')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')

    b = True
    c = True

    while True:
        try:
            city = notypos(str(input('\nChoose a city by typing in Chicago, Washington or New York. ')),cities_typos)
            if city == 'Not found.':
                print('\nOops, the program was not able to recognise what you wrote. Please try again.\n')
            else:
                print('\nSo you\'ve chosen {}, is that right?\n'.format(city))
                answer = notypos(str(input('Answer by typing in yes or no. ')),answer_typos)
                while answer == 'Not found.':
                    print('\nOops, the program was not able to recognise what you wrote. Did you mean to enter {}?\n'.format(city))
                    answer = notypos(str(input('\nAnswer by entering yes or no only. \n')),answer_typos)
                if answer == 'yes':
                    print('\nThank you for choosing {}.\n'.format(city))
                    break
                else:
                    print('\nNo problem, you can try again right now if you want.\n')
        except KeyboardInterrupt:
            print('\n\nYou\'ve exited the program.\n\n')
            b = False
            c = False
            break
        except:
            print('\nThe program ran into a technical issue. Please try again.\n')

    while b:
        try:
            month = notypos(str(input('Type in a specific month name from January up to June or enter all instead to display information about the first six months of the year. ')),months_typos)
            if month == 'Not found.':
                print('\nOops, the program was not able to recognise what you wrote. Please try again.\n')
            elif month in {'July','August','September','October','November','December'}:
                print('\nNo data availble for {}. Please choose a month between January and June or choose all for all first six months of the year.\n'.format(month))
            else:
                if month != 'all':
                    print('\nSo you\'ve chosen {}, is that right?\n'.format(month))
                else:
                    print('\nSo you\'ve chosen all of the months from January to June, is that right?\n')
                answer = notypos(str(input('Answer by typing in yes or no. ')),answer_typos)
                while answer == 'Not found.':
                    print('\nOops, the program was not able to recognise what you wrote. Did you mean to enter {}?\n'.format(month))
                    answer = notypos(str(input('\nAnswer by entering yes or no only. \n')),answer_typos)
                if answer == 'yes':
                    if month != 'all':
                        print('\nThank you for choosing {}.\n'.format(month))
                        break
                    else:
                        print('\nThank you for choosing all the months from January to June.\n')
                        break
                else:
                    print('\nNo problem, you can try again right now if you want.\n')
        except KeyboardInterrupt:
            print('\n\nYou\'ve exited the program.\n\n')
            c = False
            break
        except:
            print('\nThe program ran into a technical issue. Please try again.\n')

    while c:
        try:
            day = notypos(str(input('Type in a specific day of the week or enter all instead to display information about the entire week. ')),days_typos)
            if day == 'Not found.':
                print('\nOops, the program was not able to recognise what you wrote. Please try again.\n')
            else:
                if day != 'all':
                    print('\nSo you\'ve chosen {}, is that right?\n'.format(day))
                else:
                    print('\nSo you\'ve chosen all the days of the week, is that right?\n')
                answer = notypos(str(input('Answer by typing in yes or no. ')),answer_typos)
                while answer == 'Not found.':
                    print('\nOops, the program was not able to recognise what you wrote. Did you mean to enter {}?\n'.format(day))
                    answer = notypos(str(input('\nAnswer by entering yes or no only. \n')),answer_typos)
                if answer == 'yes':
                    if day != 'all':
                        print('\nThank you for choosing {}.\n'.format(day))
                        print('-'*40)
                        return city, month, day
                    else:
                        print('\nThank you for choosing all the days of the week.\n')
                        print('-'*40)
                        return city, month, day
                else:
                    print('\nNo problem, you can try again right now if you want.\n')
        except KeyboardInterrupt:
            print('\n\nYou\'ve exited the program.\n\n')
            break
        except:
            print('\nThe program ran into a technical issue. Please try again.\n')


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.DataFrame(pd.read_csv(CITY_DATA[convert[city]]))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['month'] = df['Start Time'].dt.month

    if day != 'all' and month != 'all':
        df = df[(df['day_of_week'] == convert[day]) & (df['month'] == convert[month])]
        return df
    elif day == 'all' and month != 'all':
        df = df[df['month'] == convert[month]]
        return df
    elif day != 'all' and month == 'all':
        df = df[df['day_of_week'] == convert[day]]
        return df
    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    num_to_month = {1 : 'January', 2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May', 6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September',
                    10 : 'October', 11 : 'November', 12 : 'December'}

    num_to_day = {0 : 'Monday', 1 : 'Tuesday', 2 : 'Wednesday', 3 : 'Thursday', 4 : 'Friday', 5 : 'Saturday', 6: 'Sunday'}

    # TO DO: display the most common month
    if month == 'all':
        most_common_month = num_to_month[df['month'].mode()[0]]
        print('The most common month is ' + most_common_month + '.')
    else:
        print('The most common month does not exist as you chose to view ' + month + ' data only.')

    # TO DO: display the most common day of week
    if day == 'all':
        most_common_day = num_to_day[df['day_of_week'].mode()[0]]
        print('The most common day of the week is ' + most_common_day + '.')
    else:
        print('The most common day of the week does not exist as you chose to view ' + day + ' data only.')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is ' + str(most_common_hour) + ':00.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station is ' + popular_start_station + '.')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station is ' + popular_end_station + '.')

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + """ (start) - """ + df['End Station'] + """ (end)"""
    popular_start_end_combo = df['start_end_combo'].mode()[0]
    print('The most common start and end station combination is ' + popular_start_end_combo + '.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    to_hour_min = lambda seconds: str(int((seconds//3600))) + ' hours and ' + str(int(((seconds/3600)-(seconds//3600))*60)) + ' minutes.'
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is ' + to_hour_min(total_travel_time))

    # TO DO: display mean travel time
    to_min_sec = lambda seconds: str(int(seconds//60)) + ' minutes and ' + str(int(round(((seconds/60)-(seconds//60))*60,1))) + ' secondes.'
    average_travel_time = df['Trip Duration'].mean()
    print('The average travel time is ' + to_min_sec(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('There are ' + str(df['User Type'].value_counts()['Customer']) + ' customers and '
          + str(df['User Type'].value_counts()['Subscriber']) + ' subscribers.')

    # TO DO: Display counts of gender
    if city != 'Washington':
        print('There are ' + str(df['Gender'].value_counts()['Male']) + ' male users and '
          + str(df['Gender'].value_counts()['Female']) + ' female users.')

    # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is ' + str(int(df['Birth Year'].min())) + '.')
        print('The most recent year of birth is ' + str(int(df['Birth Year'].max())) + '.')
        print('The most common year of birth is ' + str(int(df['Birth Year'].mode()[0])) + '.')
    else:
        print('Gender and birth year data not available for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Displays five rows at a time from the dataframe if the user wills it. """
    i = 0
    raw = notypos(str(input("Would you like to view individual trip data (five rows at a time)? Answer by entering yes or no. ")),answer_typos)
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])
            raw = notypos(str(input("Would you like to view more individual trip data (five rows at a time)? Answer by entering yes or no. ")),answer_typos)
            i += 5
        else:
            raw = notypos(str(input("\nYour input is invalid. Please enter yes or no only. \n")),answer_typos)


def main():
    while True:
        try:
            global city, month, day
            city, month, day = get_filters()
            print('\nCHOICE REMINDER\n')
            print(city,month,day)
            global df
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            display_raw_data(df)

            restart = notypos(str(input('\nWould you like to restart? Enter yes or no. \n')),answer_typos)
            while restart == 'Not found.':
                print('\nOops, the program was not able to recognise what you wrote.\n')
                restart = notypos(str(input('\nPlease try again with yes or no only. \n')),answer_typos)
            if restart == 'no':
                break
        except:
            restart = notypos(str(input('\nWould you like to restart? Enter yes or no. \n')),answer_typos)
            while restart == 'Not found.':
                print('\nOops, the program was not able to recognise what you wrote.\n')
                restart = notypos(str(input('\nPlease try again with yes or no only. \n')),answer_typos)
            if restart == 'no':
                break



if __name__ == "__main__":
	main()

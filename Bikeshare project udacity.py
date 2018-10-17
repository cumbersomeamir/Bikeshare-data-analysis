import time
import pandas as pd
import numpy as np
from datetime import datetime
from statistics import mode
from statistics import StatisticsError
from collections import Counter

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def Most_Common(lst):
        data = Counter(lst)
        return data.most_common(1)[0][0]

def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for chicago, new york or washington ?").title()
    temp = True
    while temp:
        if city == 'Chicago' or city == 'New York City' or city == 'Washington':
            temp = False
        else:
            print("Please enter right city")
            city = input("Would you like to see data for chicago, new york city or washington ?").title()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month? January, February, March, April, May or June, All ?").title()
    temp = True
    nameOfMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    while temp:
        if month in nameOfMonths:
            temp = False
        else:
            print("Please enter correct month")
            month = input("Which month? January, February, March, April, May or June, All ?").title()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? Monday, Tuesday,.....Sunday, All ?").title()
    nameOfDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All']
    temp = True
    while temp:
        if day in nameOfDays:
            temp = False
        else:
            print("Please enter correct name of day")
            day = input("Which day? monday, tuesday,.....sunday, all ?").title()

    print('-'*40)
    return city, month, day


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

    city_dataFrame = pd.read_csv(CITY_DATA[city])
    df = ""

    Start_time = city_dataFrame['Start Time']

    convert_to_dateTime = pd.to_datetime(Start_time)

    months = convert_to_dateTime.dt.strftime("%B")

    days = convert_to_dateTime.dt.strftime("%A")

    city_dataFrame['month'] = months

    city_dataFrame['day'] = days

    if month == 'All':
        df = city_dataFrame

        return df

    if day == 'All':
        grouped_by_months = city_dataFrame.groupby('month')
        for i,j in grouped_by_months:
            if i == month:
                df = j
                break

        return df


    if day != 'All' and month != 'All':
        grouped_by_monthsDays = city_dataFrame.groupby(['month','day'])
        for i,j in grouped_by_monthsDays:
                if i[0] == month:
                    if i[1] == day:
                        df = j
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(Most_Common(df['month']))

    # TO DO: display the most common day of week
    print(Most_Common(df['day']))

    # TO DO: display the most common start hour
    Start_time = df['Start Time']
    convert_to_dateTime = pd.to_datetime(Start_time)
    hours = convert_to_dateTime.dt.hour
    print(Most_Common(hours))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print(Most_Common(df['Start Station']))
    print(Most_Common(df['End Station']))
    print(Most_Common(df['Start Station']+df['End Station']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration']

    print(np.sum(travel_time))

    # TO DO: display total mean time
    print(np.mean(travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

     # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(int(np.min(df['Birth Year'])), int(np.max(df['Birth Year'])), int(mode(df['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    temp = True
    inputValue = input("do you want to see raw data?").title()
    if inputValue == "Yes":
        print(df.head())
    else :
        print("No")



def main():
    while True:

         city, month, day = get_filters()
         df = load_data(city, month, day)
         time_stats(df)
         station_stats(df)
         trip_duration_stats(df)
         user_stats(df)
         display_data(df)
         restart = input('\nWould you like to restart? Enter yes or no.\n')
         if restart.lower() != 'yes':
             break


if __name__ == "__main__":
	main()

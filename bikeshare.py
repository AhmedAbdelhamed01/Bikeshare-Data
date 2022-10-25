import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle
    while True:
        city = input("\nEnter the name of city you need (chicago, new york city, washington):").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("\n Ops,Please Enter valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\n Enter which month you need ( january, february, march, april, may, june) Or (all) to all monthes  :").lower()
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            print("\n Ops,Please Enter valid month name")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Enter which day you need (monday, tuesday, wednesday, thursday, friday, saturday, sunday) Or (all) to all days  :").lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            print("\n Ops,Please Enter valid day name")

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
# i used it  from project 3
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month , day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(" \nMost common month is:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print(" \nMost common day is:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print(" \nMost common  start hour is:", df['start hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print("\n Most commonly used start station is:",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("\n Most commonly used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['start_to_end'] = df['Start Station']+' ' + df['End Station']
    most_start_toend = df['start_to_end'].mode()[0]
    print("\n Most frequent combination of start station and end station trip:", most_start_toend)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\n Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("\n Mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print("\n Gender", df['Gender'].value_counts())
    except:
        print("\n Ops,there is no data about gender in this city")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("\nEarliest common year of birth", int(df['Birth Year'].min()))
    except:
        print("\n Ops,there is no data about year of birth in this city")

    try:
        print("\nMost recent common year of birth",int(df['Birth Year'].max()))
    except:
        print("\n Ops,there is no data about year of birth in this city")

    try:
        print("\nMost common  common year of birth",int(df['Birth Year'].mode()[0]))
    except:
        print("\n Ops, there is no data about year of birth in this city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_rows(df):
    # ask user to display 5 rowes of data
    x = 0
    while True:
        ask = input("Are you need to display next 5 rows of data?\n choice(yes or no):").lower()
        if ask != 'yes' and ask != 'no':
            print("\n Ops ,wrong choice,pleas choice (yes or not)")
        elif ask == 'no':
            break
        else:
            if x+5 < df.shape[0]:
                print(df.iloc[x:x+5])
                x += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

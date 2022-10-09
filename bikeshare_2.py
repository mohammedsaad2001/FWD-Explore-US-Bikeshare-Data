import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}

"""this dictionary for the while loops in get_filterr function to check 
if the names of cities,months,days are founded"""
complex_dict = {'cities': ['chicago', 'new york', 'washington'],
                'months': ['january','february', 'march', 'april', 'may', 'june'],
                'days': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']}


"""this dictionary for the while loops in load_data function to get the value
of key (month name)"""
mon_dict={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("the name of the city is :\n")
    city = city.lower()
    while city not in complex_dict['cities']:
        city = input("the name of the city is not valid !. Please enter a valid name ('chicago','new york','washington'):\n")
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month=input("the name of the month is ?,you can choose all :\n")
    month = month.lower()
    while (month not in complex_dict['months']) and (month != "all"):
        month = input("the name of the month is not valid !. Please enter a valid name ('january','february',....) :\n")
        month = month.lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("the name of the day is ?,you can choose all :\n")
    day = day.lower()
    while (day not in complex_dict['days']) and (day != "all"):
        day = input("the name of the day is not valid !. Please enter a valid name ('sunday', 'monday',....):\n")
        day = day.lower()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['mon_filter'] = df['Start Time'].dt.month
    df['day_filter'] = df['Start Time'].dt.day_name()
    if month in complex_dict['months']:
        month = mon_dict[month]
        df = df[df['mon_filter'] == month]
    if day in complex_dict['days']:
        df = df[df['day_filter'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    mode_mon = df['mon_filter'].mode()[0]
    mode_day = df['day_filter'].mode()[0]
    mode_hour = df['Start Time'].dt.hour.mode()[0]

    # display the most common month
    print("the most common month : ", mode_mon, "\n")

    # display the most common day of week
    print("the most common day : ", mode_day, "\n")

    # display the most common start hour
    print("the most common start hour : ", mode_hour, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    mode_start_station = df['Start Station'].mode()[0]
    mode_end_station = df['End Station'].mode()[0]
    mode_compin = (df['Start Station'] + " " + df['End Station']).mode()[0]

    # display most commonly used start station
    print('most common start station is :', mode_start_station, "\n")

    # display most commonly used end station
    print('most common end station is :', mode_end_station, "\n")

    # # display most frequent combination of start station and end station trip
    print("most common frequent combination of start station and end station trip is :", mode_compin, "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    trip_sum = df['Trip Duration'].sum()
    trip_mean = df['Trip Duration'].mean()

    # display total travel time
    print("total travel time is :",trip_sum, "\n")

    # display mean travel time
    print("mean travel time is :", trip_mean, "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type = df["User Type"].value_counts().to_frame()

    # Display counts of user types
    print("count of user types is : \n", user_type, "\n")

    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts().to_frame()

        # Display counts of gender
        print("count of gender types is : \n", count_gender, "\n")

    if 'Birth Year' in df.columns:
        most_earliest, most_recent,most_common = df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]

        # Display earliest, most recent, and most common year of birth
        print("most earliest year of birth is :", round(most_earliest), "\n")
        print("most recent year of birth is :", round(most_recent), "\n")
        print("most common year of birth is :", round(most_common), "\n")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_data(df):
    """Raw data is displayed upon request by the user"""
    see = input("if you want to see 5 rows of data ,please enter 'yes' else 'no'. \n").lower()
    rows = 5
    #df.equals(df.head(rows)) is not True
    while see == 'yes' and rows != len(df.index):
        print(df.head(rows))
        see = input("if you want to see +5 rows of data ,enter 'yes' else 'no'. \n").lower()
        rows += 5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  main()
